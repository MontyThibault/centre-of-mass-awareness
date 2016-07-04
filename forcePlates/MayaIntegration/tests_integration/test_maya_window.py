from plugin.window import Window
import maya.cmds as cmds


def test_open_and_close_window():
	
	# Window should not exist

	assert not cmds.window('test', exists = True)

	w = Window('test', cmds)

	assert cmds.window('test', exists = True)

	w2 = Window('test', cmds)

	# w should not exist anymore since it was overwritten


	w2.delete(cmds)

	assert not cmds.window('test', exists = True)


def test_add_button_and_text():

	w = Window('test', cmds)

	def f():
		w.delete(cmds)

	w.button('click me', f, cmds)
	w.text('hey, ma', cmds)

	f()