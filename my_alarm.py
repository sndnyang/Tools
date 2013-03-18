#!/usr/env python
# -*- coding: cp936 -*-

import wx, os

class my_frame(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'my frame',
                          size = (400, 300))
        panel = wx.Panel(self)

        #get ready for timer
        self.last_time = 0
        self.timer = wx.Timer(self, wx.ID_ANY)
        self.Bind(wx.EVT_TIMER, self.TimeOver, self.timer)

        #add button'''
        exit_button = wx.Button(panel, label = "exit",
                                pos = (50, 200), size = (50, 25))
        self.event_button = wx.Button(panel, label = 'Start',
                              pos = (150, 200), size = (50, 25))

        self.Bind(wx.EVT_BUTTON, self.OnCloseButton, exit_button)
        self.Bind(wx.EVT_BUTTON, self.onBtTimer, self.event_button)
        self.Bind(wx.EVT_CLOSE, self.CloseWindow)

        
        #add bar and menu
        status_bar = self.CreateStatusBar()
        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        file_menu.Append(wx.NewId(), 'New File', 'New file')
        file_menu.Append(wx.NewId(), 'Open File', 'Open file')

        edit_menu = wx.Menu()

        menu_bar.Append(file_menu, 'File')
        menu_bar.Append(edit_menu, 'Edit')
        self.SetMenuBar(menu_bar)
        

        #add input text
        self.input_text = wx.TextCtrl(panel, -1, "30",
                                 size = (150, 30))
        self.input_text.SetInsertionPoint(0)        

       
    def OnCloseButton(self, event):
        self.Close(True)

    def TimeOver(self, event):
        self.timer.Stop()
        self.timer.Destroy()
        self.event_button.SetLabel("Start")
        self.input_text.SetValue('30')

        cmd = r'''"C:\Program Files\Windows Media Player\wmplayer.exe" /play E:\music\chinese\海阔天空.mp3'''
        os.popen(cmd)

    def onBtTimer(self, event):
        
        if self.timer.IsRunning():
            self.timer.Stop()
            self.event_button.SetLabel("Start")
            self.input_text.SetValue('30')
            
        else:
            
            content =  self.input_text.GetValue()

            try :

                #get the input time to count down
                self.last_time = float(content) * 60
                if self.last_time <= 0:
                    raise ValueError

                #set button text
                self.event_button.SetLabel('Stop')

                self.timer.Start(self.last_time * 1000)      #an EVT_TIMER every 1 second
                 
            except ValueError:
                message = wx.MessageDialog(None, "Error Input Type", 'Warnning',
                                       wx.YES_NO)
                
                if message.ShowModal():
                    pass
                message.Destroy()

    def CloseWindow(self, event):
        self.Destroy()

        
if __name__ == '__main__':

    app = wx.PySimpleApp()
    frame = my_frame(parent = None, id = -1)
    frame.Show()
    app.MainLoop()
