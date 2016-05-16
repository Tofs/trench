import pyglet

window = pyglet.window.Window()

image = pyglet.resource.image("resources/images/resourceNotFound.png")
print(image)


@window.event
def on_draw():
	window.clear()
	image.blit(10, 10)

pyglet.app.run()
