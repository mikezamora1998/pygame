import pyglet
import math
from pyglet.window import key
from . import physicalobject, resources


class Bullet(physicalobject.PhysicalObject):
    """Bullets fired by the player"""

    def __init__(self, *args, **kwargs):
        x = args[0]
        y = args[1]
        super(Bullet, self).__init__(resources.bullet_image, int(x), int(y),  batch=kwargs.get("batch"))
        pyglet.clock.schedule_once(self.die, 0.5)

    def die(self, dt):
        self.dead = True
