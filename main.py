import pyglet

window = pyglet.window.Window()

missing = pyglet.resource.image(


@window.event
def on_draw():
	window.clear()
	image.draw()

pyglet.app.run()
