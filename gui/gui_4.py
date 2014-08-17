import wx

class form(wx.Dialog):

  def __init__(self, parent, id, title):
      wx.Dialog.__init__(self, parent, id, title, size=(150, 60))
      self.button = wx.Button(self, -1, 'Change Color', (0, 0))

      self.panel  = wx.Panel(self, -1, (120, 2), (20, 20))
      self.panel.SetBackgroundColour('RED')

      self.Bind(wx.EVT_BUTTON, self.Change, self.button)

      self.Center()
      self.Show()

  def Change(self,event):
      self.panel.SetBackgroundColour('BLUE')
      self.panel.Refresh()

app = wx.App()
form(None, -1, 'Color Changer')
app.MainLoop()