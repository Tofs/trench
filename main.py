import logging
import cocos
from cocos.actions import *


class HelloWorld(cocos.layer.ColorLayer):

	def __init__(self):
		super(HelloWorld, self).__init__(200, 200, 200, 255)

		label = cocos.text.Label("Hello world!")
		label.position = 320, 240
		self.add(label)

		sprite = cocos.sprite.Sprite('resources/images/resourceNotFound.png')
		sprite.position = 500, 500
		sprite.scale = 5
		self.add(sprite, z=1)

		scale = ScaleBy(3, duration=2)
		label.do(Repeat(scale + Reverse(scale)))


class KeyHandler(cocos.layer.Layer):

	# Retrive director.window events
	is_event_hanlder = True

	def __init_(self):
		super(KeyHandler, self).__init__()

		# output
		self.text = cocos.text.Label("", x=100, y=300)

		# input
		self.keys_pressed = set()
		self.update_text()
		self.add(self.text)

	def update_text():
		key_names = [pyglet.window.key.symbol_string(k) for k in self.keys_pressed]
		text = "Keys: {0}".format(",".join(key_names))

		self.text.element.text = text

	# This function is called when a key is pressed
	def on_key_press(self, key, modifiers):
		self.key_pressed.add(key)
		self.update_text()

	# This function is called upon key release
	def on_key_release(self, key, modifiers):
		self.key_pressed.remove(key)
		self.update_text()


class MouseHandler(cocos.layer.Layer):
	# this layer listens to events
	is_event_hanlder = True

	def __init__(self):
		super(MouseHandler, self).__init__()
		self.logger = logging.getLogger("MouseHandler")

		self.posx = 100
		self.posy = 240
		self.text = cocos.text.Label("Durp", font_size=18, x=self.posx, y=self.posy)
		self.add(self.text)

	def update_text(self, x, y):
		text = "Mouse @ %d, %d" % (x, y)
		self.text.element.text = text
		self.text.element.x = self.posx
		self.text.element.y = self.posy

	# Called when the mouse is moved over the layer
	def on_mouse_motion(self, x, y, dx, dy):
		self.update_text(x, y)

	# listen for when the mouse button is pressed

	def on_mouse_press(self, x, y, buttons, modifiers):
		line1 = "---- Mouse Event ----"
		self.logger.debug(line1)
		self.posy, self.posy = director.get_virtual_coordinates(x, y)
		self.update_text(x, y)


def configLogging(debug):
	if debug:
		debugLevel = logging.DEBUG
	else:
		debugLevel = logging.INFO
	logging.basicConfig(level=debugLevel, filename="trench.log")
	logger = logging.getLogger("logging_util")
	logger.info("The logger has now been Initiated")

configLogging(True)
logger = logging.getLogger("main")
logger.info("Program Start")

logger.info("init cocos")
cocos.director.director.init(resizable=True)


scene = cocos.scene.Scene(KeyHandler(), MouseHandler())


logger.info("Create test layer.")
hello_layer = HelloWorld()
hello_layer.do(RotateBy(360, duration=10))

logger.info("now showe stuff on the screen")
main_scene = cocos.scene.Scene(hello_layer)
cocos.director.director.run(scene)
