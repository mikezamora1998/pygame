import pyglet
import random
from . import physicalobject, resources, util


def asteroids(num_asteroids, player_position, batch=None):
    """Generate asteroid objects with random positions and velocities,
    not close to the player"""
    asteroids_array = []
    for i in range(num_asteroids):
        asteroid_x, asteroid_y = player_position
        while util.distance((asteroid_x, asteroid_y), player_position) < 100:
            asteroid_x = random.randint(0, 800)
            asteroid_y = random.randint(0, 600)
        new_asteroid = physicalobject.PhysicalObject(img=resources.asteroid_image,
                                            x=asteroid_x, y=asteroid_y, batch=batch)
        new_asteroid.rotation = random.randint(0, 360)
        asteroids_array.append(new_asteroid)
    return asteroids_array


def player_lives(num_icons, batch=None):
    player_lives_array = []
    for i in range(num_icons):
        new_sprite = pyglet.sprite.Sprite(img=resources.player_image,
                                          x=785-i*30, y=585, batch=batch)
        new_sprite.scale = 0.5
        player_lives_array.append(new_sprite)
    return player_lives_array
