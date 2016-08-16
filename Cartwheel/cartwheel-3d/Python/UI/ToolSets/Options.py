'''
Created on 2009-09-26

@author: beaudoin
'''

import UI, wx
from ToolsetBase import ToolsetBase

class Options(ToolsetBase):
    
    def __init__(self, toolPanel):
        """Adds a tool set for various options information to a toolpanel."""
        
        super(Options, self).__init__()
        
        self._toolPanel = toolPanel
        self._toolSet = toolPanel.createToolSet( "Options" )

        app = wx.GetApp()

        self.addOption( "Show collision volumes", app.getDrawCollisionVolumes, app.drawCollisionVolumes )
        self.addOption( "Capture screenshots", app.getCaptureScreenShots, app.captureScreenShots )
        self.addOption( "Kinematic motion", app.getKinematicMotion, app.setKinematicMotion)
        

        options = [('Show abstract view', '_showAbstractView'),
             ('Show abstract view skeleton', '_showAbstractViewSkeleton'),
             ('Show body frame', '_showBodyFrame'),
             ('Show CD primitives', '_showCDPrimitives'),
             ('Show colors', '_showColors'),
             ('Show friction particles', '_showFrictionParticles'),
             ('Show joints', '_showJoints'),
             ('Show mesh', '_showMesh'),
             ('Show min BDG Sphere', '_showMinBDGSphere'),
             ('Show center of mass', '_showCenterOfMass')]
        
        for (print_name, attribute_name) in options:
            self.addOption(print_name, app.getOption(attribute_name), app.setOption(attribute_name))

        # Add this as an observer
        app.addOptionsObserver(self)
        
        # Initial update
        self.update()        