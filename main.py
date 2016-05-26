import logging
import cocos


class HelloWorld(cocos.layer.Layer):

	def __init__(self):
		super(HelloWorld, self).__init__()

		label = cocos.text.Label("Hello world!")
		label.position = 320, 240

		self.add(label)


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

cocos.director.director.init()

hello_layer = HelloWorld()

main_scene = cocos.scene.Scene(hello_layer)

cocos.director.director.run(main_scene)
