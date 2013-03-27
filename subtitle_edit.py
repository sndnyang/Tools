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
        #将状态栏分割为3个区域,比例为1:2:3
        self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-1, -2, -3])

    def OnPaintMotion(self, event):
        
        #设置状态栏1内容
        self.statusbar.SetStatusText(u"鼠标位置：" + str(event.GetPositionTuple()), 0)
        
        #设置状态栏2内容
        self.statusbar.SetStatusText(u"当前线条长度：%s" % len(self.paint.curLine), 1)
        
        #设置状态栏3内容
        self.statusbar.SetStatusText(u"线条数目：%s" % len(self.paint.lines), 2)   
             
        event.Skip()

    def MenuData(self):
        '''
                   菜单数据
        '''
        #格式：菜单数据的格式现在是(标签, (项目))，其中：项目组成为：标签, 描术文字, 处理器, 可选的kind
        #标签长度为2，项目的长度是3或4
        return [("&File", (             #一级菜单项
                           ("&New", "New paint file", self.OnNew),             #二级菜单项
                           ("&Open", "Open paint file", self.OnOpen),
                           ("&Save", "Save paint file", self.OnSave),
                           ("", "", ""),                                       #分隔线
                           ("", "", ""),
                           ("&Quit", "Quit", self.OnCloseWindow)))
               ]
    
    def CreateMenuBar(self):
        '''
        创建菜单
        '''
        menuBar = wx.MenuBar()
        for eachMenuData in self.MenuData():
            menuLabel = eachMenuData[0]
            menuItems = eachMenuData[1]
            menuBar.Append(self.CreateMenu(menuItems), menuLabel) 
        self.SetMenuBar(menuBar)
        
    def CreateMenu(self, menuData):
        '''
        创建一级菜单
        '''
        menu = wx.Menu()
        for eachItem in menuData:
            if len(eachItem) == 2:
                label = eachItem[0]
                subMenu = self.CreateMenu(eachItem[1])
                menu.AppendMenu(wx.NewId(), label, subMenu) #递归创建菜单项
            else:
                self.CreateMenuItem(menu, *eachItem)
        return menu
    
    def CreateMenuItem(self, menu, label, status, handler, kind = wx.ITEM_NORMAL):
        '''
        创建菜单项内容
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
        打开开文件对话框
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
        保存文件
        '''
        if not self.filename:
            self.OnSaveAs(event)
        else:
            self.SaveFile()
            
    def OnSaveAs(self, event):
        '''
        弹出文件保存对话框
        '''
        file_wildcard = "Paint files(*.paint)|*.paint|All files(*.*)|*.*" 
        dlg = wx.FileDialog(self, 
                            "Save paint as ...",
                            os.getcwd(),
                            style = wx.SAVE | wx.OVERWRITE_PROMPT,
                            wildcard = file_wildcard)
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetPath()
            if not os.path.splitext(filename)[1]: #如果没有文件名后缀
                filename = filename + '.paint'
            self.filename = filename
            self.SaveFile()
            self.SetTitle(self.title + '--' + self.filename)
        dlg.Destroy()

    def OnCloseWindow(self, event):
        self.Destroy()

    def SaveFile(self):
        '''
        保存文件
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
