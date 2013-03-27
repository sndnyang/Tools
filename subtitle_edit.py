#!/usr/env python
# -*- coding: cp936 -*-

import wx, os

class MainFrame(wx.Frame):

    def __init__(self):
        self.title = 'Main Frame'
        wx.Frame.__init__(self, None, -1, 'Main Frame', size = (300,300))
        panel = wx.Panel(self, -1)
        
        self.InitStatusBar()
        self.CreateMenuBar()

        self.filename = ''

    def InitStatusBar(self):
        self.statusbar = self.CreateStatusBar()
        #��״̬���ָ�Ϊ3������,����Ϊ1:2:3
        self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-1, -2, -3])

    def OnPaintMotion(self, event):
        
        #����״̬��1����
        self.statusbar.SetStatusText(u"���λ�ã�" + str(event.GetPositionTuple()), 0)
        
        #����״̬��2����
        self.statusbar.SetStatusText(u"��ǰ�������ȣ�%s" % len(self.paint.curLine), 1)
        
        #����״̬��3����
        self.statusbar.SetStatusText(u"������Ŀ��%s" % len(self.paint.lines), 2)   
             
        event.Skip()

    def MenuData(self):
        '''
                   �˵�����
        '''
        #��ʽ���˵����ݵĸ�ʽ������(��ǩ, (��Ŀ))�����У���Ŀ���Ϊ����ǩ, ��������, ������, ��ѡ��kind
        #��ǩ����Ϊ2����Ŀ�ĳ�����3��4
        return [("&File", (             #һ���˵���
                           ("&New", "New paint file", self.OnNew),             #�����˵���
                           ("&Open", "Open paint file", self.OnOpen),
                           ("&Save", "Save paint file", self.OnSave),
                           ("", "", ""),                                       #�ָ���
                           ("", "", ""),
                           ("&Quit", "Quit", self.OnCloseWindow)))
               ]
    
    def CreateMenuBar(self):
        '''
        �����˵�
        '''
        menuBar = wx.MenuBar()
        for eachMenuData in self.MenuData():
            menuLabel = eachMenuData[0]
            menuItems = eachMenuData[1]
            menuBar.Append(self.CreateMenu(menuItems), menuLabel) 
        self.SetMenuBar(menuBar)
        
    def CreateMenu(self, menuData):
        '''
        ����һ���˵�
        '''
        menu = wx.Menu()
        for eachItem in menuData:
            if len(eachItem) == 2:
                label = eachItem[0]
                subMenu = self.CreateMenu(eachItem[1])
                menu.AppendMenu(wx.NewId(), label, subMenu) #�ݹ鴴���˵���
            else:
                self.CreateMenuItem(menu, *eachItem)
        return menu
    
    def CreateMenuItem(self, menu, label, status, handler, kind = wx.ITEM_NORMAL):
        '''
        �����˵�������
        '''
        if not label:
            menu.AppendSeparator()
            return
        menuItem = menu.Append(-1, label, status, kind)
        self.Bind(wx.EVT_MENU, handler,menuItem)
    
    def OnNew(self, event):
        pass
    
    def OnOpen(self, event):
        '''
        �򿪿��ļ��Ի���
        '''
        file_wildcard = "Paint files(*.paint)|*.paint|All files(*.*)|*.*" 
        dlg = wx.FileDialog(self, "Open paint file...",
                            os.getcwd(), 
                            style = wx.OPEN,
                            wildcard = file_wildcard)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetPath()
            self.ReadFile()
            self.SetTitle(self.title + '--' + self.filename)
        dlg.Destroy()
        
        
    
    def OnSave(self, event): 
        '''
        �����ļ�
        '''
        if not self.filename:
            self.OnSaveAs(event)
        else:
            self.SaveFile()
            
    def OnSaveAs(self, event):
        '''
        �����ļ�����Ի���
        '''
        file_wildcard = "Paint files(*.paint)|*.paint|All files(*.*)|*.*" 
        dlg = wx.FileDialog(self, 
                            "Save paint as ...",
                            os.getcwd(),
                            style = wx.SAVE | wx.OVERWRITE_PROMPT,
                            wildcard = file_wildcard)
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetPath()
            if not os.path.splitext(filename)[1]: #���û���ļ�����׺
                filename = filename + '.paint'
            self.filename = filename
            self.SaveFile()
            self.SetTitle(self.title + '--' + self.filename)
        dlg.Destroy()

    def OnCloseWindow(self, event):
        self.Destroy()

    def SaveFile(self):
        '''
        �����ļ�
        '''
        if self.filename:
            data = self.paint.GetLinesData()
            f = open(self.filename, 'w')
            cPickle.dump(data, f)
            f.close()
                     
    def ReadFile(self):
        if self.filename:
            try:
                f = open(self.filename, 'r')
                data = cPickle.load(f)
                f.close()
                self.paint.SetLinesData(data)
            except cPickle.UnpicklingError:
                wx.MessageBox("%s is not a paint file."
                              % self.filename, "error tip",
                              style = wx.OK | wx.ICON_EXCLAMATION)
                
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MainFrame()
    frame.Show(True)
    app.MainLoop()
