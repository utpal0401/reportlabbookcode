import configparser

import wx


class ConfigDialog(wx.Dialog):
    
    def __init__(self):
        wx.Dialog.__init__(self, None, 
                           title='Edit Configuration',
                           size=(400, 400))
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        config = configparser.ConfigParser()
        config.read('config.ini')
        config_dict = dict(config.items('General'))
        
        self.logo = wx.TextCtrl(
            self, value=config_dict['logo_path'])
        self.layout('Logo Path:', self.logo)
        
        self.left_margin = wx.TextCtrl(
            self, value=config_dict['left_margin'])
        self.layout('Left Margin:', self.left_margin)
        
        self.right_margin = wx.TextCtrl(
            self, value=config_dict['right_margin'])
        self.layout('Right Margin:', self.right_margin)
        
        self.top_margin = wx.TextCtrl(
            self, value=config_dict['top_margin'])
        self.layout('Top Margin:', self.top_margin)
        
        self.bottom_margin = wx.TextCtrl(
            self, value=config_dict['bottom_margin'])
        self.layout('Bottom Margin:', self.bottom_margin)
        
        self.style = wx.TextCtrl(
            self, value=config_dict['style'])
        self.layout('Style:', self.style)
        
        save_btn = wx.Button(self, label='Save')
        self.main_sizer.Add(save_btn, 0, wx.ALL|wx.CENTER, 5)
        
        self.SetSizer(self.main_sizer)
        
    def layout(self, lbl, txt):
        """
        Layout the label and text control widgets
        """
        size = (80, -1)
        hsizer = wx.BoxSizer()
        hsizer.Add(wx.StaticText(self, label=lbl, size=size),
                   0, wx.ALL, 5)
        hsizer.Add(txt, 1, wx.ALL|wx.EXPAND, 5)
        self.main_sizer.Add(hsizer, 0, wx.EXPAND)
        
    def save(self, event):
        """
        Save the config to disk
        """
        config = configparser.ConfigParser()
        config.add_section('General')
        config.set('General', 'logo_path', 
                   self.logo.GetValue())
        config.set('General', 'left_margin', 
                   self.left_margin.GetValue())
        config.set('General', 'right_margin', 
                   self.right_margin.GetValue())
        config.set('General', 'top_margin', 
                   self.top_margin.GetValue())
        config.set('General', 'bottom_margin', 
                   self.bottom_margin.GetValue())
        config.set('General', 'style', 
                   self.style.GetValue())
        
        with open('config.ini', 'wb') as config_file:
            config_file.write(config)
            
        dlg = wx.MessageDialog(
            parent=None,
            message='Config saved',
            caption='Config Saved',
            style=wx.OK|wx.ICON_INFORMATION
        )
        dlg.ShowModal()
        dlg.Destroy()
        
if __name__ == '__main__':
    app = wx.App(False)
    dlg = ConfigDialog()
    dlg.ShowModal()
    dlg.Destroy()
    app.MainLoop()