import pyglet


def center_image(image):
    """Sets an image's anchor to its center"""
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2


# Tell pyglet where to find the resources
pyglet.resource.path = ['game/resources']
pyglet.resource.reindex()

# Load the three main resources and get them to draw centered
player_image = pyglet.resource.image("player.png")
bullet_image = pyglet.resource.image("bullet.png")
asteroid_image = pyglet.resource.image("asteroid.png")
engine_image = pyglet.resource.image("engine_flame.png")

engine_image.anchor_x = engine_image.width * 1.5
engine_image.anchor_y = engine_image.height / 2

center_image(player_image)
center_image(bullet_image)
center_image(asteroid_image)
