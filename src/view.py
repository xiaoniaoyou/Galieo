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



import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class MainView(mainFrame.GeneratedFrame):
    def __init__(self, parent):
        mainFrame.GeneratedFrame.__init__(self, parent)


    def show_main_msg(self, str):
        self.m_staticText_mian_msg.SetLabel(str)


class ConfigView(mainFrame.ConfigDialog):
    def __init__(self, parent):
        mainFrame.ConfigDialog.__init__(self, parent)


    def show_dlg_msg(self, str):
        self.m_staticText_msg.SetLabel(str)









































