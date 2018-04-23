#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
此界面用于上传指定目录的文件夹，打包该文件夹并压缩，然后上传到远程服务器上指定目录（默认桌面下）
版本3.0.0，此版本用于上传打包压缩后的文件
版本2.0.0,此版本用于上传文件夹

'''
__version__ = '4.0.2'
__author__ = 'Eric'


import MainFrame as mainFrame
import wx
from wx.lib.pubsub import pub
import re
import yaml
import paramiko
import os
import time
import subprocess
import getpass
import datetime


import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class Model:
    def __init__(self):
        self.send_cmd = []
        self.client_file_dir = ''
        self.client_file = ''
        self.choose_dir = None
        self.server_address = None
        self.server_file_dir = None
        self.server_address = None
        self.server_file_dir = None
        self.password = None
        self.user = None
        self.ip = None
        self.port = None
        self.yaml_file = './config.yml'

        self.msg = {'0': u'选择本机的文件:\n',
                    '1': u'选择本机的文件夹:\n',
                    '2': u'请先选择文件夹或文件,再上传\n',
                    '3': u'连接服务器失败,请确定输入地址是否正确或网络是否正常\n',
                    '4': u'一些文件未能传输成功,请看终端\n',
                    '5': u'上传成功\n',
                    }


    def on_choose_dir(self):
        dlg = wx.DirDialog(None, u"选择文件夹", style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            self.client_file_dir = dlg.GetPath()
        dlg.Destroy()
        self.choose_dir = True
        self.display_main_msg()


    def on_choose_file(self):
        wildcard = 'All files|**'
        dlg = wx.FileDialog(None, u'选择文件', os.getcwd(), '', wildcard, wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.client_file = dlg.GetPath()
        dlg.Destroy()
        self.choose_dir = False
        self.display_main_msg()


    def on_upload_file(self):
        # 读取配置文件
        f = open(self.yaml_file)
        all_data = yaml.load(f)
        f.close()
        self.server_address = all_data['ip']
        self.port = all_data['port']
        self.password = all_data['password']
        self.server_file_dir = all_data['file_path']
        (self.user, self.ip) = self.extract_user_and_ip(self.server_address)

        print '---->', self.client_file_dir
        print '++++>', self.client_file
        if self.user is None:  # 异常处理
            msg = u''
            pub.sendMessage('show_main_msg', str=msg)
            return
        if self.client_file_dir == '' and self.choose_dir is True:
            msg = self.msg['2']
            pub.sendMessage('show_main_msg', str=msg)
            return
        if self.client_file == '' and self.choose_dir is False:
            msg = self.msg['2']
            pub.sendMessage('show_main_msg', str=msg)
            return

        # 选择上传文件夹，需先打包压缩，然后再上传
        if self.choose_dir == True:
            package_file_name = os.path.basename(self.client_file_dir)
            package_file_unique_name = '{}_{}-{}'.format(package_file_name, getpass.getuser(), \
                                                         datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
            self.server_file_dir = os.path.join(self.server_file_dir, package_file_name)
            last_dir = os.path.dirname(self.client_file_dir)
            # tar_cmd = 'tar -czvf %s.tar.gz -C %s %s ' % (package_file_name, last_dir, package_file_name)
            tar_cmd = 'tar -czvf %s.tar.gz -C %s %s' % (package_file_unique_name, last_dir, package_file_name)
            print 'tar_cmd={}'.format(tar_cmd)
            try:
                ret = subprocess.check_call(tar_cmd, shell=True)
            except subprocess.CalledProcessError, e:
                print e
                msg = u'打包压缩文件夹失败，请确定文件夹名字不能有包含空格或其他标点符号'
                pub.sendMessage('show_main_msg', str=msg)
                return

            # 　上传压缩后的文件
            if ret == 0:
                # current_tar_file = '%s/%s.tar.gz' % (os.getcwd(), package_file_name)
                current_tar_file = '%s/%s.tar.gz' % (os.getcwd(), package_file_unique_name)
                # cost_time = self.upload_file(current_tar_file, self.server_file_dir + '.tar.gz')
                server_filepath = os.path.join(os.path.dirname(self.server_file_dir), package_file_unique_name)
                server_filepath += '.tar.gz'
                cost_time = self.upload_file(current_tar_file, server_filepath)
                if cost_time > 0:
                    msg = u'上传成功,耗费时间%f秒' % cost_time
                    pub.sendMessage('show_main_msg', str=msg)
                elif cost_time == -1:
                    msg = u'上传失败,请检测服务器是否已开启openssh-server'
                    pub.sendMessage('show_main_msg', str=msg)
                elif cost_time == -2:
                    msg = u'读取上传文件夹失败'
                    pub.sendMessage('show_main_msg', str=msg)
                # 删除打包后的文件
                # rm_cmd = 'rm %s.tar.gz ' % (package_file_name)
                rm_cmd = 'rm %s.tar.gz ' % (package_file_unique_name)
                ret = subprocess.check_output(rm_cmd, shell=True)

        # 上传单一文件，直接上传，不用打包压缩
        else:
            client_file_name = os.path.basename(self.client_file)
            self.server_file_dir = os.path.join(self.server_file_dir, client_file_name)
            cost_time = self.upload_file(self.client_file, self.server_file_dir)
            if cost_time > 0:
                msg = u'上传成功,耗费时间%f秒' % cost_time
                pub.sendMessage('show_main_msg', str=msg)
            elif cost_time == -1:
                msg = u'上传失败,请检测服务器是否已开启openssh-server'
                pub.sendMessage('show_main_msg', str=msg)
            elif cost_time == -2:
                msg = u'读取上传文件夹失败'
                pub.sendMessage('show_main_msg', str=msg)


    def on_config_ip(self, server_address):
        f = open(self.yaml_file)
        all_data = yaml.load(f)
        f.close()
        (self.user, self.ip) = self.extract_user_and_ip(server_address)
        if self.user is not None:
            all_data['ip'] = server_address
            # all_data['port'] = 22
            # 设置默认的上传目录
            all_data['file_path'] = '/home/' + self.user + '/Desktop'
            with open(self.yaml_file, 'wb+') as fw:
                yaml.dump(all_data, fw, default_flow_style=False, encoding='utf8')
                fw.close()
            self.display_dlg_msg()
        else:
            msg = u'请输入正确格式的IP,必须是主机名@IP'
            pub.sendMessage('show_dlg_msg', str=msg)


    def on_config_file_path(self, server_file_dir):
        f = open(self.yaml_file)
        all_data = yaml.load(f)
        f.close()
        if server_file_dir != '':
            all_data['file_path'] = server_file_dir
            with open(self.yaml_file, 'wb+') as fw:
                yaml.dump(all_data, fw, default_flow_style=False, encoding='utf8')
                fw.close()
            self.display_dlg_msg()
        else:
            temp_list = [
                u'当前设置的目标地址:    ', all_data['ip'], '\n',
                u'当前设置的目标存放路径:  ', all_data['file_path'], '\n',
                u'不能输入空文件路径\n'
            ]
            temp = ''.join(temp_list)
            msg = temp
            pub.sendMessage('show_dlg_msg', str=msg)


    def on_config_password(self, password):
        f = open(self.yaml_file)
        all_data = yaml.load(f)
        f.close()
        all_data['password'] = password
        if password != '':
            with open(self.yaml_file, 'wb+') as fw:
                yaml.dump(all_data, fw, default_flow_style=False, encoding='utf8')
                fw.close()
            temp_list = [
                u'当前设置的目标地址:    ', all_data['ip'], '\n',
                u'当前设置的目标存放路径:  ', all_data['file_path'], '\n',
                u'已保存登录密码\n'
            ]
            temp = ''.join(temp_list)
            msg = temp
            pub.sendMessage('show_dlg_msg', str=msg)
        else:
            temp_list = [
                u'当前设置的目标地址:    ', all_data['ip'], '\n',
                u'当前设置的目标存放路径:  ', all_data['file_path'], '\n',
                u'请输入登录密码\n'
            ]
            temp = ''.join(temp_list)
            msg = temp
            pub.sendMessage('show_dlg_msg', str=msg)


    def extract_user_and_ip(self, msg):
        pattern = re.compile(r'(.*)(@)(.+)')
        try:
            m = re.match(pattern, msg)
            user = m.groups()[0]
            ip = m.groups()[2]
        except Exception as e:
            # print u'正则表达式匹配错误'
            msg = u'请检查配置的IP是否正确,必须是主机名@IP'
            pub.sendMessage('show_main_msg', str=msg)
            return None, None
        return user, ip

    # 上传单一文件，本地文件名与远程文件名必须相同
    def upload_file(self, local_file, remote_dir):
        cost_time = None
        try:
            start = time.time()
            client = paramiko.Transport((self.ip, self.port))
            client.connect(username=self.user, password=self.password)
            sftp = paramiko.SFTPClient.from_transport(client)
            # print '>>>>>>>>>>>>>', local_file
            # print '<<<<<<<<<<<<<', remote_dir
            sftp.put(local_file, remote_dir)
            client.close()
            end = time.time()
            cost_time = end - start

        except paramiko.ssh_exception.SSHException, e:
            print '-->', e
            cost_time = -1
        except IOError, e:
            print '-->', e
            cost_time = -2

        finally:
            return cost_time


    def display_main_msg(self):
        f = open(self.yaml_file)
        all_data = yaml.load(f)
        f.close()
        self.server_address = all_data['ip']
        self.server_file_dir = all_data['file_path']
        temp_list = [
            u'当前设置的目标地址:    ', self.server_address, '\n',
            u'当前设置的目标存放路径:  ', self.server_file_dir, '\n',
            u'当前选择本机的文件夹:   ', self.client_file_dir, '\n',
            u'当前选择本机的文件:    ', self.client_file, '\n'
        ]
        temp = ''.join(temp_list)
        pub.sendMessage('show_main_msg', str=temp)

    def display_dlg_msg(self):
        f = open(self.yaml_file)
        all_data = yaml.load(f)
        f.close()
        self.server_address = all_data['ip']
        self.server_file_dir = all_data['file_path']
        temp_list = [
            u'当前设置的目标地址:    ', self.server_address, '\n',
            u'当前设置的目标存放路径:  ', self.server_file_dir, '\n',
        ]
        temp = ''.join(temp_list)
        pub.sendMessage('show_dlg_msg', str=temp)
































