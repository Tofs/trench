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
cocos.director.director.init()


logger.info("Create test layer.")
hello_layer = HelloWorld()
hello_layer.do(RotateBy(360, duration=10))


logger.info("now showe stuff on the screen")
main_scene = cocos.scene.Scene(hello_layer)
cocos.director.director.run(main_scene)
