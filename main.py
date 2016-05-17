import pyglet
import logging
from pyglet.window import key


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

logger.debug("Creating the window")
window = pyglet.window.Window()
logger.debug("The window has now been created")

image = pyglet.resource.image("resources/images/resourceNotFound.png")

x = 10
y = 10
keys = key.KeyStateHandler()


@window.event
def on_key_press(symbol, modifiers):
	logger.debug("Mod: {0} Key: {1}".format(modifiers, symbol))


@window.event
def on_draw():
	global x
	window.clear()
	image.blit(x, y)
	if keys[key.A]:
		x = x - 1
		logger.debug("troll")

pyglet.app.run()
