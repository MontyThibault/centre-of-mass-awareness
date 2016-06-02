import UI, wx
from ToolsetBase import ToolsetBase
import threading

class CoMSliders(ToolsetBase):
    
    def __init__(self, toolPanel):
        """Adds a tool set for camera information to a toolpanel."""
        
        super(CoMSliders, self).__init__()
        
        self._toolPanel = toolPanel
        self._toolSet = toolPanel.createToolSet( "Centre of Mass" )
        app = wx.GetApp()
        
        self.addSlider("X Position", -0.2, 0.2, 0.01, app.getCOMX, app.setCOMX)
        self.addSlider("Y Position", -0.2, 0.2, 0.01, app.getCOMY, app.setCOMY)
        self.addSlider("Z Position", -0.2, 0.2, 0.01, app.getCOMZ, app.setCOMZ)
        
        self.addSlider("Error Scale", 0, 0.05, 0.001, app.getOption('_COMErrorScale'), app.setOption('_COMErrorScale'))
        
        # Add this as an observer
        app.addCOMObserver(self)
        
        # Initial update
        self.update()