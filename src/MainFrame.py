# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Dec 21 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class GeneratedFrame
###########################################################################

class GeneratedFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 496,167 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button_config = wx.Button( self.m_panel1, wx.ID_ANY, u"配置", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button_config, 0, wx.ALL, 5 )
		
		self.m_button_choose_dir = wx.Button( self.m_panel1, wx.ID_ANY, u"选择文件夹", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button_choose_dir, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.m_button_choose_single_file = wx.Button( self.m_panel1, wx.ID_ANY, u"选择文件", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button_choose_single_file, 0, wx.ALL, 5 )
		
		self.m_button_upload = wx.Button( self.m_panel1, wx.ID_ANY, u"上传", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button_upload, 0, wx.ALL, 5 )
		
		self.m_button_quit = wx.Button( self.m_panel1, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button_quit, 0, wx.ALL, 5 )
		
		
		bSizer3.Add( bSizer5, 0, 0, 5 )
		
		self.m_staticline6 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer3.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText_mian_msg = wx.StaticText( self.m_panel1, wx.ID_ANY, u"传输文件信息如下:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_mian_msg.Wrap( -1 )
		bSizer7.Add( self.m_staticText_mian_msg, 0, wx.ALL, 5 )
		
		
		bSizer3.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		
		self.m_panel1.SetSizer( bSizer3 )
		self.m_panel1.Layout()
		bSizer3.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button_choose_dir.Bind( wx.EVT_BUTTON, self.on_choose_file )
		self.m_button_choose_single_file.Bind( wx.EVT_BUTTON, self.on_upload_single_file )
		self.m_button_upload.Bind( wx.EVT_BUTTON, self.on_upload_file )
		self.m_button_quit.Bind( wx.EVT_BUTTON, self.on_quit_main_frame )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def on_choose_file( self, event ):
		event.Skip()
	
	def on_upload_single_file( self, event ):
		event.Skip()
	
	def on_upload_file( self, event ):
		event.Skip()
	
	def on_quit_main_frame( self, event ):
		event.Skip()
	

###########################################################################
## Class ConfigDialog
###########################################################################

class ConfigDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 617,469 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"配置传送目标,主机名@IP,例如usename@192.168.16.164", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer14.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_textCtrl_server_address = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.m_textCtrl_server_address, 1, wx.ALL, 5 )
		
		self.m_button_ip = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.m_button_ip, 0, wx.ALL, 5 )
		
		
		bSizer14.Add( bSizer15, 1, wx.EXPAND, 5 )
		
		
		bSizer10.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		
		bSizer8.Add( bSizer10, 1, wx.EXPAND, 5 )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer20 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"配置传输文件的存放位置,默认/home/usename/Desktop", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		bSizer20.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_textCtrl_server_file_dir = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_textCtrl_server_file_dir, 1, wx.ALL, 5 )
		
		self.m_button_file_path = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_button_file_path, 0, wx.ALL, 5 )
		
		
		bSizer20.Add( bSizer12, 1, wx.EXPAND, 5 )
		
		
		bSizer11.Add( bSizer20, 1, wx.EXPAND, 5 )
		
		
		bSizer8.Add( bSizer11, 1, wx.EXPAND, 5 )
		
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"输入目标主机的登录密码,默认123456", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		bSizer16.Add( self.m_staticText15, 0, wx.ALL, 5 )
		
		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_textCtrl_password = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		bSizer22.Add( self.m_textCtrl_password, 1, wx.ALL, 5 )
		
		self.m_button_password = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.m_button_password, 0, wx.ALL, 5 )
		
		
		bSizer16.Add( bSizer22, 1, wx.EXPAND, 5 )
		
		
		bSizer13.Add( bSizer16, 1, wx.EXPAND, 5 )
		
		
		bSizer8.Add( bSizer13, 1, wx.EXPAND, 5 )
		
		bSizer23 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer24 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText_msg = wx.StaticText( self, wx.ID_ANY, u"提示信息", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_msg.Wrap( -1 )
		bSizer24.Add( self.m_staticText_msg, 0, wx.ALL, 5 )
		
		self.m_button_quit_dlg = wx.Button( self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.m_button_quit_dlg, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		bSizer23.Add( bSizer24, 1, wx.EXPAND, 5 )
		
		
		bSizer8.Add( bSizer23, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer8 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button_ip.Bind( wx.EVT_BUTTON, self.on_config_ip )
		self.m_button_file_path.Bind( wx.EVT_BUTTON, self.on_config_file_path )
		self.m_button_password.Bind( wx.EVT_BUTTON, self.on_config_password )
		self.m_button_quit_dlg.Bind( wx.EVT_BUTTON, self.on_quit_config_dlg )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def on_config_ip( self, event ):
		event.Skip()
	
	def on_config_file_path( self, event ):
		event.Skip()
	
	def on_config_password( self, event ):
		event.Skip()
	
	def on_quit_config_dlg( self, event ):
		event.Skip()
	

