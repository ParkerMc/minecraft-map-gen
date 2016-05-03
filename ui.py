#-------------------------------------------------------------------------------
# Name:        ui
# Purpose:     To store and handle the gui
#
# Author:      ParkerMc
#
# Created:     03/05/2016
# Copyright:   (c) ParkerMc 2016
# Licence:     MIT
#-------------------------------------------------------------------------------

# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Start
###########################################################################

class Start ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Minecraft Map Gen", pos = wx.DefaultPosition, size = wx.Size( 215,75 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHintsSz( wx.Size( 215,75 ), wx.Size( 215,75 ) )

		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.new = wx.Button( self, wx.ID_ANY, u"New Config", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.new, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.load = wx.Button( self, wx.ID_ANY, u"Load Config", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.load, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		self.SetSizer( gbSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.new.Bind( wx.EVT_BUTTON, self.new)
		self.load.Bind( wx.EVT_BUTTON, self.load)

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def new( self, event ):
		print "new"

	def load( self, event ):
		print "load"


