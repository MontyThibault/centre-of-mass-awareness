'''
Created on 2009-08-25

Basic controller editor

@author: beaudoin
'''
import sys
sys.path += ['.']

import wx, App, math

movieResolution = (1280,720)
movieSetup = False # True if we want a movie
glMovie = False    # True if we're only interested in recording the GL canvas
                   # False if we want a "screen cast"

glCanvasSize = wx.DefaultSize
size = wx.DefaultSize
showConsole = True
if movieSetup:
    if glMovie:
        glCanvasSize = movieResolution
    else:
        size = movieResolution
        showConsole = False


app = App.SNMApp("Style Editor", size = size, glCanvasSize=glCanvasSize, showConsole = showConsole, fps=24)

import UI, Utils, GLUtils, Physics, Core, MathLib, PyUtils
from App import InstantChar, KeyframeEditor

# Create the desired tool sets
toolPanel = app.getToolPanel()
animationToolSet = UI.ToolSets.Animation(toolPanel)
if not movieSetup:
    optionsToolSet = UI.ToolSets.Options(toolPanel)
    optionsToolSet._toolSet.setOpen(False)
cameraToolSet = UI.ToolSets.Camera(toolPanel)
cameraToolSet._toolSet.setOpen(False)
instantChar = InstantChar.Model()
if not movieSetup:
    controllerSnapshotToolSet = UI.ToolSets.SnapshotTree(toolPanel)
    controllerSnapshotToolSet._toolSet.setOpen(False)
    controllerTreeToolSet = UI.ToolSets.ControllerTree(toolPanel)
    controllerTreeToolSet._toolSet.setOpen(False)


app.COMPanel = UI.ToolSets.CoMSliders(toolPanel)

glCanvas = app.getGLCanvas()
glCanvas.addGLUITool( UI.GLUITools.CurveEditorCollection )

#from Data.Frameworks import DefaultFramework
#from Data.Frameworks import DanceFramework
#from Data.Frameworks import WalkFramework


#####################
## BEGIN Custom for Instant Character

character = instantChar.create()
#controller = PyUtils.load( "Characters.BipV3.Controllers.CartoonySneak", character )
#controller = PyUtils.load( "Characters.BipV3.Controllers.ZeroWalk", character )

# This shows off the balance controller well
controller = PyUtils.load( "Characters.BipV3.Controllers.jerome2", character )

#controller = PyUtils.load( "Characters.BipV3.Controllers.emps", character )
#controller = PyUtils.load( "Characters.BipV3.Controllers.run_21-57_0-38_0-10", character )
#controller = PyUtils.load( "Characters.BipV3.Controllers.FastWalk_3-7_0-53", character )
#controller = PyUtils.load( "Characters.BipV3.Controllers.EditableWalking", character )
#controller = PyUtils.load( "Temp.Cartoony", character )
#controller = PyUtils.load( "Temp.TipToe", character )
controller.setStance( Core.LEFT_STANCE );
instantChar.connectController(False)

#character.loadReducedStateFromFile( "Data/Characters/BipV3/Controllers/runState.rs" )

keyframeEditor = KeyframeEditor.Model()

## END
#####################

######################
## BEGIN DUMMY STUFF

#staircase = App.Scenario.Staircase( position=(0,0,5), rightRampHeight = 1, stepCount = 22, leftRampHeight = 1, angle = math.pi/4.0 )
#staircase.load()


#PyUtils.convertController("../../scoros5/data/controllers/bipV3/fWalk_3.sbc")

#ctrl2 = PyUtils.copy( app.getController(0), char )

## END DUMMY STUFF
######################

# Initial snapshot
app.takeSnapshot()

app.MainLoop()
app.Destroy()
