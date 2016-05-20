# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:		ui
# Purpose:	 To store and handle the gui
#
# Author:	  ParkerMc
#
# Created:	 03/05/2016
# Copyright:   (c) ParkerMc 2016
# Licence:	 MIT
#-------------------------------------------------------------------------------

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import os
import core
import subprocess
import wx.richtext

f = open("os","r")
global osc
osc = f.readline()
f.close()
global configa
configa = ["",1,"",[],[]]
#configa = ["K:\\test",1, "K:\\test\\test.cfg", [u'C:\\Users\\SchoolWInternet\\AppData\\Roaming\\.minecraft\\saves\\World1'], [(u'test', 0, 0, 0, 0, u'', 3, 95)]]

###########################################################################
## Class Start
###########################################################################

class Start ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Minecraft Map Gen", pos = wx.DefaultPosition, size = wx.Size( 210,75 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHintsSz( wx.Size( 210,75 ), wx.Size( 210,75 ) )
		self.SetBackgroundColour( wx.Colour( 160, 160, 160 ) )

		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.new = wx.Button( self, wx.ID_ANY, u"New Config", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.new, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.load = wx.Button( self, wx.ID_ANY, u"Load Config", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.load, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		self.load.Enable(False)

		self.SetSizer( gbSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.new.Bind( wx.EVT_BUTTON, self.newf )
		self.load.Bind( wx.EVT_BUTTON, self.loadf )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def newf( self, event ):
		 mset = MainSet(None)
		 mset.Show(True)
		 self.HideWithEffect(0)
		 self.Destroy()
		 event.Skip()

	def loadf( self, event ):
		event.Skip()


###########################################################################
## Class load
###########################################################################

class load ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Minecraft Map Gen", pos = wx.DefaultPosition, size = wx.Size( 272,135 ), style = wx.CAPTION|wx.MAXIMIZE_BOX|wx.MINIMIZE|wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

		self.SetSizeHintsSz( wx.Size( 272,135 ), wx.Size( 272,135 ) )
		self.SetBackgroundColour( wx.Colour( 160, 160, 160 ) )

		gbSizer8 = wx.GridBagSizer( 0, 0 )
		gbSizer8.SetFlexibleDirection( wx.BOTH )
		gbSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.next = wx.Button( self, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer8.Add( self.next, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.can = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer8.Add( self.can, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		gbSizer8.AddSpacer( ( 0, 0 ), wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		self.configfile = wx.StaticText( self, wx.ID_ANY, u"Config", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.configfile.Wrap( -1 )
		self.configfile.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )

		gbSizer8.Add( self.configfile, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_filePicker3 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.cfg", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		gbSizer8.Add( self.m_filePicker3, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		self.m_staticText15.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )

		gbSizer8.Add( self.m_staticText15, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.edit = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer8.Add( self.edit, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		self.SetSizer( gbSizer8 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.next.Bind( wx.EVT_BUTTON, self.nextp )
		self.can.Bind( wx.EVT_BUTTON, self.quit )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def nextp( self, event ):
		event.Skip()

	def quit( self, event ):
		 mset = arequit(None,self)
		 mset.Show(True)
		 event.Skip()


###########################################################################
## Class MainSet
###########################################################################

class MainSet ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Minecraft Map Gen", pos = wx.DefaultPosition, size = wx.Size( 340,195 ), style = wx.CAPTION|wx.MAXIMIZE_BOX|wx.MINIMIZE|wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

		self.SetSizeHintsSz( wx.Size( 340,195 ), wx.Size( 340,195 ) )
		self.SetBackgroundColour( wx.Colour( 160, 160, 160 ) )

		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.out = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Output", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		gbSizer2.Add( self.out, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 3 ), wx.ALL, 5 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Output", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )

		gbSizer2.Add( self.m_staticText1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Processes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		self.m_staticText2.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )

		gbSizer2.Add( self.m_staticText2, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.pro = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 10, 1 )
		self.pro.SetMaxSize( wx.Size( 50,-1 ) )

		gbSizer2.Add( self.pro, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.save = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Save As", u"*.cfg", wx.DefaultPosition, wx.DefaultSize, wx.FLP_SAVE|wx.FLP_USE_TEXTCTRL )
		gbSizer2.Add( self.save, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 3 ), wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Save As", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		self.m_staticText6.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )

		gbSizer2.Add( self.m_staticText6, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		gbSizer2.AddSpacer( ( 0, 20 ), wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		self.can = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.can, wx.GBPosition( 4, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.next = wx.Button( self, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.next, wx.GBPosition( 4, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		self.SetSizer( gbSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.can.Bind( wx.EVT_BUTTON, self.quit )
		self.next.Bind( wx.EVT_BUTTON, self.nextp )

		global configa
		self.out.SetPath(configa[0])
		self.pro.SetValue(configa[1])
		self.save.SetPath(configa[2])

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def quit( self, event ):
		 mset = arequit(None,self)
		 mset.Show(True)
		 event.Skip()


	def nextp( self, event ):
		 global configa
		 configa[0] = self.out.GetPath()
		 configa[1] = self.pro.GetValue()
		 configa[2] = self.save.GetPath()
		 world = Worlds(None)
		 world.Show(True)
		 self.HideWithEffect(0)
		 self.Destroy()
		 event.Skip()
		 event.Skip()


###########################################################################
## Class Worlds
###########################################################################

class Worlds ( wx.Frame ):

	def __init__( self, parent ):
		global configa
		self.listChoices = []
		for i in configa[3]:
		  if i != "":
			  self.listChoices.append(i)
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Minecraft Map Gen", pos = wx.DefaultPosition, size = wx.Size( 365,385 ), style = wx.CAPTION|wx.MAXIMIZE_BOX|wx.MINIMIZE|wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

		self.SetSizeHintsSz( wx.Size( 365,385 ), wx.Size( 365,385 ) )
		self.SetBackgroundColour( wx.Colour( 160, 160, 160 ) )

		gbSizer3 = wx.GridBagSizer( 0, 0 )
		gbSizer3.SetFlexibleDirection( wx.BOTH )
		gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.Worlds = wx.StaticText( self, wx.ID_ANY, u"Worlds", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Worlds.Wrap( -1 )
		self.Worlds.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )

		gbSizer3.Add( self.Worlds, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.list = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, self.listChoices, 0 )
		self.list.SetMinSize( wx.Size( 340,200 ) )

		gbSizer3.Add( self.list, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 4 ), wx.ALL, 5 )

		self.addw = wx.Button( self, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.addw, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		gbSizer3.AddSpacer( ( 50, 0 ), wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		self.re = wx.Button( self, wx.ID_ANY, u"Remove", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.re, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.worlddir = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder with a world", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		gbSizer3.Add( self.worlddir, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 3 ), wx.ALL, 5 )

		self.can = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.can, wx.GBPosition( 4, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.next = wx.Button( self, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.next, wx.GBPosition( 4, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		self.SetSizer( gbSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.addw.Bind( wx.EVT_BUTTON, self.add )
		self.re.Bind( wx.EVT_BUTTON, self.dela )
		self.can.Bind( wx.EVT_BUTTON, self.quit )
		self.next.Bind( wx.EVT_BUTTON, self.nextp )


	def __del__( self ):
		pass

	# Virtual event handlers, overide them in your derived class
	def add( self, event ):
		 if os.path.isfile(self.worlddir.GetPath()+"/level.dat"):
			self.listChoices.append(self.worlddir.GetPath())
			self.list.Set(self.listChoices)
			self.worlddir.SetPath("")
			self.listChoices.sort()
		 event.Skip()

	def dela( self, event):
		 self.listChoices.pop(self.list.GetSelection())
		 self.list.Set(self.listChoices)
		 event.Skip()

	def quit( self, event ):
		 mset = arequit(None,self)
		 mset.Show(True)
		 event.Skip()

	def nextp( self, event ):
		 global configa
		 configa[3] = self.listChoices
		 mapsf = maps(None)
		 mapsf.Show(True)
		 self.HideWithEffect(0)
		 self.Destroy()
		 event.Skip()


###########################################################################
## Class maps
###########################################################################

class maps ( wx.Frame ):

	def __init__( self, parent ):
		global configa
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Minecraft Map Gen", pos = wx.DefaultPosition, size = wx.Size( 305,345 ), style = wx.CAPTION|wx.MAXIMIZE_BOX|wx.MINIMIZE|wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

		self.SetSizeHintsSz( wx.Size( 305,345 ), wx.Size( 305,345 ) )
		self.SetBackgroundColour( wx.Colour( 160, 160, 160 ) )

		gbSizer3 = wx.GridBagSizer( 0, 0 )
		gbSizer3.SetFlexibleDirection( wx.BOTH )
		gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.renders = wx.StaticText( self, wx.ID_ANY, u"Maps", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.renders.Wrap( -1 )
		self.renders.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )

		gbSizer3.Add( self.renders, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.listChoices = []
		self.list = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, self.listChoices, 0 )
		self.list.SetMinSize( wx.Size( 280,200 ) )

		gbSizer3.Add( self.list, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 4 ), wx.ALL, 5 )

		self.addw = wx.Button( self, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.addw, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.ed = wx.Button( self, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.ed, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.re = wx.Button( self, wx.ID_ANY, u"Remove", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.re, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.can = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.can, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.next = wx.Button( self, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.next, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		self.SetSizer( gbSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.addw.Bind( wx.EVT_BUTTON, self.add )
		self.ed.Bind( wx.EVT_BUTTON, self.edit )
		self.re.Bind( wx.EVT_BUTTON, self.dela )
		self.can.Bind( wx.EVT_BUTTON, self.quit )
		self.next.Bind( wx.EVT_BUTTON, self.nextp )
		for i, j, k, l, m, n, o, p in configa[4]:
		  self.listChoices.append(i)
		self.list.Set(self.listChoices)

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def add( self, event ):
		editf = edit(None, ["",0,0,0,0,"",0,95], False, self)
		editf.Show()
		event.Skip()

	def edit( self, event ):
		settings = []
		q = 0
		for i, j, k, l, m, n, o, p in configa[4]:
		  if i == self.listChoices[self.list.GetSelection()]:
		      settings[0] = i
		      settings[1] = j
		      settings[2] = k
		      settings[3] = l
		      settings[4] = m
		      settings[5] = n
		      settings[6] = o
		      settings[7] = p
		  q += 1
		self.dela(event)
		editf = edit(None, settings, True, self)
		editf.Show()
		event.Skip()

	def dela( self, event ):
		 q = 0
		 for i, j, k, l, m, n, o, p in configa[4]:
		  if i == self.listChoices[self.list.GetSelection()]:
			  configa[4].pop(q)
		  q += 1

		 self.listChoices.pop(self.list.GetSelection())
		 self.list.Set(self.listChoices)
		 event.Skip()

	def quit( self, event ):
		 mset = arequit(None,self)
		 mset.Show(True)
		 event.Skip()

	def nextp( self, event ):
		 outf = out(None)
		 outf.Show(True)
		 self.HideWithEffect(0)
		 self.Destroy()
		 event.Skip()
	def reload(self):
		 self.listChoices = []
		 for i, j, k, l, m, n, o, p in configa[4]:
		  self.listChoices.append(i)
		 self.list.Set(self.listChoices)


###########################################################################
## Class edit
###########################################################################

class edit ( wx.Frame ):
	def __init__( self, parent, settings, editb , self2):
		self.self = self2
		self.settings = settings
		self.editbool = editb
		global configa
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Minecraft Map Gen", pos = wx.DefaultPosition, size = wx.Size( 316,318 ), style = 0|wx.TAB_TRAVERSAL )

		self.SetSizeHintsSz( wx.Size( 316,318 ), wx.Size( 316,318 ) )
		self.SetBackgroundColour( wx.Colour( 160, 160, 160 ) )

		gbSizer6 = wx.GridBagSizer( 0, 0 )
		gbSizer6.SetFlexibleDirection( wx.BOTH )
		gbSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"World", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		self.m_staticText6.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )

		gbSizer6.Add( self.m_staticText6, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		worldChoices = configa[3]
		self.world = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, worldChoices, 0 )
		self.world.SetSelection( 0 )
		gbSizer6.Add( self.world, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Dimension", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		self.m_staticText8.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )

		gbSizer6.Add( self.m_staticText8, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		dimensionChoices = [ u"Overworld", u"Nether", u"End" ]
		self.dimension = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, dimensionChoices, 0 )
		self.dimension.SetSelection( 0 )
		gbSizer6.Add( self.dimension, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Rendermode", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		self.m_staticText9.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )

		gbSizer6.Add( self.m_staticText9, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		rmodeChoices = [ u"Normal", u"Lighting", u"Smooth Lighting", u"Night", u"Smooth Night", u"Nether", u"Nether Lighting", u"Nether Smooth Lighting", u"Cave" ]
		self.rmode = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, rmodeChoices, 0 )
		self.rmode.SetSelection( 0 )
		gbSizer6.Add( self.rmode, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"North Direction", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		self.m_staticText10.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )

		gbSizer6.Add( self.m_staticText10, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		northChoices = [ u"Upper Left", u"Upper Right", u"Lower Left", u"Lower Right" ]
		self.north = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, northChoices, 0 )
		self.north.SetSelection( 0 )
		gbSizer6.Add( self.north, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Texture Pack", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		self.m_staticText11.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )

		gbSizer6.Add( self.m_staticText11, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_filePicker2 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a Texture Pack", u"*.zip", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		gbSizer6.Add( self.m_filePicker2, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )
		self.m_filePicker2.Enable(False)

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Image Format", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		self.m_staticText12.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )

		gbSizer6.Add( self.m_staticText12, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		iformatChoices = [ u"Png", u"Jpg", u"Jpeg" ]
		self.iformat = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, iformatChoices, 0 )
		self.iformat.SetSelection( 0 )
		gbSizer6.Add( self.iformat, wx.GBPosition( 6, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Image Quality", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		self.m_staticText13.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )

		gbSizer6.Add( self.m_staticText13, wx.GBPosition( 7, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_spinCtrl2 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 95 )
		gbSizer6.Add( self.m_spinCtrl2, wx.GBPosition( 7, 1 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		self.m_staticText7.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )

		gbSizer6.Add( self.m_staticText7, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer6.Add( self.name, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )

		self.can = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer6.Add( self.can, wx.GBPosition( 8, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.add = wx.Button( self, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer6.Add( self.add, wx.GBPosition( 8, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		self.SetSizer( gbSizer6 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.can.Bind( wx.EVT_BUTTON, self.quit )
		self.add.Bind( wx.EVT_BUTTON, self.addm )

		self.name.SetValue(settings[0])
		self.world.SetSelection(settings[1])
		self.dimension.SetSelection(settings[2])
		self.rmode.SetSelection(settings[3])
		self.north.SetSelection(settings[4])
		self.m_filePicker2.SetPath(settings[5])
		self.iformat.SetSelection(settings[6])
		self.m_spinCtrl2.SetValue(settings[7])

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def quit( self, event ):
		global configa
		if self.editbool==True:
		  configa[4].append((self.settings[0], self.settings[1], self.settings[2], self.settings[3], self.settings[4], self.settings[5], self.settings[6], self.settings[7]))
		  configa[4].sort()
		  maps.reload(self.self)
		self.HideWithEffect(0)
		self.Destroy()
		event.Skip()

	def addm( self, event ):
		global configa
		configa[4].append((self.name.GetValue(),self.world.GetSelection(),self.dimension.GetSelection(),self.rmode.GetSelection(),self.north.GetSelection(),self.m_filePicker2.GetPath(),self.iformat.GetCount(),self.m_spinCtrl2.GetValue()))
		configa[4].sort()
		maps.reload(self.self)
		self.HideWithEffect(0)
		self.Destroy()
		event.Skip()


###########################################################################
## Class out
###########################################################################

class out ( wx.Frame ):

	def __init__( self, parent ):
		self.time = 0

		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Minecraft Map Gen", pos = wx.DefaultPosition, size = wx.Size( 475,380 ), style = wx.CAPTION|wx.MAXIMIZE_BOX|wx.MINIMIZE|wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

		self.SetSizeHintsSz( wx.Size( 475,380 ), wx.Size( 475,380 ) )
		self.SetBackgroundColour( wx.Colour( 160, 160, 160 ) )

		gbSizer7 = wx.GridBagSizer( 0, 0 )
		gbSizer7.SetFlexibleDirection( wx.BOTH )
		gbSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		gbSizer7.AddSpacer( ( 350, 0 ), wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		self.Cancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer7.Add( self.Cancel, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		self.outt = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 450,300 ), 0|wx.TE_READONLY|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		gbSizer7.Add( self.outt, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )

		self.SetSizer( gbSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_ACTIVATE, self.runcfg )
		self.Cancel.Bind( wx.EVT_BUTTON, self.canc )


		global configa
		output = "#Made with a generator by ParkerMc\n"
		for i in configa:
		  output += "#"+str(i)+"\n"
		j = 0
		output +="\n \n"
		for i in configa[3]:
		  k = i.replace("\\","/")
		  output += 'worlds["world'+str(j)+'"] = "'+ k +'"\n'
		  j+=1
		for i, j, k, l, m, n, o, p in configa[4]:
		  if l == 0:
		      l = "normal"
		  if l == 1:
		      l = "lighting"
		  if l == 2:
		      l = "smooth_lighting"
		  if l == 3:
		      l = "night"
		  if l == 4:
		      l = "smooth_night"
		  if l == 5:
		      l = "nether"
		  if l == 6:
		      l = "nether_lighting"
		  if l == 7:
		      l = "nether_smooth_lighting"
		  if l == 8:
		      l = "cave"
		  if k == 0:
		      k = "overworld"
		  if k == 1:
		      k = "nether"
		  if k == 2:
		      k = "end"
		  if m == 0:
		      m = "upper-left"
		  if m == 1:
		      m = "upper-right"
		  if m == 2:
		      m = "lower-left"
		  if m == 3:
		      m = "lower-right"
		  if o == 3:
		      o = "png"
		  if o == 1:
		      o = "jpg"
		  if o == 2:
		      o = "jpeg"

		  output += 'renders["'+str(i)+'"] = {\n    "world": "world'+str(j)+'",\n    "title": "'+str(i)+'",\n    "rendermode": "'+str(l)+'",\n    "dimension": "'+str(k)+'",\n    "northdirection" : "'+str(m)+'",\n    "imgformat" : "'+str(o)+'",\n    "imgquality" : "'+str(p)+'",\n } \n \n'
		output += 'outputdir = "'+configa[0].replace("\\","/")+'"'
		f = open(configa[2].replace("\\","/"),"w")
		f.write(output)
		f.close()

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def canc( self, event ):
		 mset = arequit(None,self)
		 mset.Show(True)
		 event.Skip()

   	def runcfg( self, event ):
		self.time += 1
		global osc
		if osc == "win32" and self.time == 1:
		  proc = subprocess.Popen("32bit\\overviewer.exe --config="+configa[2].replace("\\","/"), shell=True,
                            stdout=subprocess.PIPE)
		  print "32"
		if osc == "win64" and self.time == 1:
		  proc = subprocess.Popen("64bit\\overviewer.exe --config="+configa[2].replace("\\","/"), shell=True,
                            stdout=subprocess.PIPE)
		if osc == "linux" and self.time == 1:
		  proc = subprocess.Popen("./linux/overviewer.py --config="+configa[2].replace("\\","/"), shell=True,
                            stdout=subprocess.PIPE)
		while True:
		  line = proc.stdout.readline()
		  if line.strip() == "":
		      pass
		  else:
		      self.outt.AddParagraph(line.strip())
		  if not line: break
		proc.wait()
		event.Skip()


###########################################################################
## Class arequit
###########################################################################

class arequit ( wx.Frame ):

	def __init__( self, parent, self2 ):
		 wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 210,93 ), style = 0|wx.TAB_TRAVERSAL )
		 self.self2 = self2
		 self.SetSizeHintsSz( wx.Size( 210,93 ), wx.Size( 210,93 ) )
		 self.SetBackgroundColour( wx.Colour( 160, 160, 160 ) )

		 gbSizer9 = wx.GridBagSizer( 0, 0 )
		 gbSizer9.SetFlexibleDirection( wx.BOTH )
		 gbSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		 self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Are you sure you would like to\nClose with out saveing?", wx.DefaultPosition, wx.DefaultSize, 0 )
		 self.m_staticText16.Wrap( -1 )
		 self.m_staticText16.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )

		 gbSizer9.Add( self.m_staticText16, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )

		 self.m_button19 = wx.Button( self, wx.ID_ANY, u"Yes", wx.DefaultPosition, wx.DefaultSize, 0 )
		 gbSizer9.Add( self.m_button19, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		 self.m_button20 = wx.Button( self, wx.ID_ANY, u"No", wx.DefaultPosition, wx.DefaultSize, 0 )
		 gbSizer9.Add( self.m_button20, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		 self.SetSizer( gbSizer9 )
		 self.Layout()

		 self.Centre( wx.BOTH )

		 # Connect Events
		 self.m_button19.Bind( wx.EVT_BUTTON, self.clo )
		 self.m_button20.Bind( wx.EVT_BUTTON, self.nocl )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def clo( self, event ):
		 self.HideWithEffect(0)
		 self.Destroy()
		 self.self2.HideWithEffect(0)
		 self.self2.Destroy()
		 event.Skip()

	def nocl( self, event ):
		 self.HideWithEffect(0)
		 self.Destroy()
		 event.Skip()



###########################################################################
## Class Splach
###########################################################################

class Splach(wx.SplashScreen):
	"""
Create a splash screen widget.
	"""
	def __init__(self, parent=None):
		# This is a recipe to a the screen.
		# Modify the following variables as necessary.
		aBitmap = wx.Image(name = "splach.png").ConvertToBitmap()
		splashStyle = wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_TIMEOUT
		splashDuration = 2500 # milliseconds
		# Call the constructor with the above arguments in exactly the
		# following order.
		wx.SplashScreen.__init__(self, aBitmap, splashStyle,
								 splashDuration, parent)
		self.Bind(wx.EVT_CLOSE, self.OnExit)

		wx.Yield()
#----------------------------------------------------------------------#

	def OnExit(self, evt):
		self.HideWithEffect(0)
		# The program will freeze without this line.
		evt.Skip()  # Make sure the default handler runs too...