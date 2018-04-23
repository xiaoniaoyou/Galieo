#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
此界面用于上传指定目录的文件夹，打包该文件夹并压缩，然后上传到远程服务器上指定目录（默认桌面下）
版本3.0.0，此版本用于上传打包压缩后的文件
版本2.0.0,此版本用于上传文件夹

'''
__version__ = '3.0.2'
__author__ = 'Eric'




import MainFrame as mainFrame
import wx
from wx.lib.pubsub import pub

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import model
import view

class Controller:
    def __init__(self, app):
        self.model = model.Model()
        self.main_view = view.MainView(None)
        self.main_view.Show()

        self.main_view.m_button_config.Bind(wx.EVT_BUTTON, self.on_show_config_dlg)
        self.main_view.m_button_choose_dir.Bind(wx.EVT_BUTTON, self.on_choose_dir)
        self.main_view.m_button_choose_single_file.Bind(wx.EVT_BUTTON, self.on_choose_file)
        self.main_view.m_button_upload.Bind(wx.EVT_BUTTON, self.on_upload_file)
        self.main_view.m_button_quit.Bind(wx.EVT_BUTTON, self.on_quit_main_frame)

        self.config_view = None
        pub.subscribe(self.show_main_msg, 'show_main_msg')
        pub.subscribe(self.show_dlg_msg, 'show_dlg_msg')

        # msg = self.model.display_main_msg()
        # self.show_main_msg(str=msg)
        self.model.display_main_msg()


    def on_show_config_dlg(self, evt):
        self.config_view = view.ConfigView(None)
        self.config_view.m_button_ip.Bind(wx.EVT_BUTTON, self.on_config_ip)
        self.config_view.m_button_file_path.Bind(wx.EVT_BUTTON, self.on_config_file_path)
        self.config_view.m_button_password.Bind(wx.EVT_BUTTON, self.on_config_password)
        self.config_view.m_button_quit_dlg.Bind(wx.EVT_BUTTON, self.on_quit_config_dlg)

        # msg = self.model.display_dlg_msg()
        # self.show_dlg_msg(str=msg)
        self.model.display_dlg_msg()
        self.config_view.ShowModal()

    def on_quit_main_frame(self, evt):
        self.main_view.Destroy()


    def on_choose_dir(self, evt):
        self.model.on_choose_dir()


    def on_choose_file(self, evt):
        self.model.on_choose_file()


    def on_upload_file(self, evt):
        self.model.on_upload_file()

    # --------------------------------------------


    def on_config_ip(self, evt):
        server_address = self.config_view.m_textCtrl_server_address.GetValue()
        self.model.on_config_ip(server_address)

    def on_config_file_path(self, evt):
        server_file_dir = self.config_view.m_textCtrl_server_file_dir.GetValue()
        self.model.on_config_file_path(server_file_dir)

    def on_config_password(self, evt):
        password = self.config_view.m_textCtrl_password.GetValue()
        self.model.on_config_password(password)

    def on_quit_config_dlg(self, evt):
        self.config_view.Destroy()
        self.model.display_main_msg()

    # --------------------------------------------

    def show_main_msg(self, str):
        self.main_view.show_main_msg(str)

    def show_dlg_msg(self, str):
        self.config_view.show_dlg_msg(str)





if __name__ == '__main__':
    app = wx.App()
    frame = Controller(app)
    app.MainLoop()


























