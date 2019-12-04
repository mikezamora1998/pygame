import pyglet
from pyglet.window import key
from asteroids.game import load, resources, player

# Set up a window
game_window = pyglet.window.Window(800, 600)

# Set up drawing batch
main_batch = pyglet.graphics.Batch()

# Set up the two top labels
score_label = pyglet.text.Label(text="Score: 0", x=10, y=575, batch=main_batch)
level_label = pyglet.text.Label(text="Asteroids Version: 1",
                                x=400, y=575, anchor_x='center', batch=main_batch)

# Initialize the player sprite
player_ship = player.Player(img=resources.player_image, x=400, y=300, batch=main_batch)
game_window.push_handlers(player_ship)
game_window.push_handlers(player_ship.key_handler)

# Init the player lives sprites
player_lives = load.player_lives(2, main_batch)

# Make three asteroids so we have something to shoot at
asteroids = load.asteroids(3, player_ship.position, main_batch)

game_objects = [player_ship] + asteroids
key_hander = key.KeyStateHandler()
game_window.push_handlers(key)


def update(dt):
    for obj in game_objects:
        obj.update(dt)

    for i in range(len(game_objects)):
        for j in range(i + 1, len(game_objects)):
            obj_1 = game_objects[i]
            obj_2 = game_objects[j]
            if not obj_1.dead and not obj_2.dead:
                if obj_1.collides_with(obj_2):
                    obj_1.handle_collision_with(obj_2)
                    obj_2.handle_collision_with(obj_1)

    to_add = []
    for obj in game_objects:
        obj.update(dt)
        to_add.extend(obj.new_objects)
        obj.new_objects = []

    for to_remove in [obj for obj in game_objects if obj.dead]:
        to_remove.delete()
        game_objects.remove(to_remove)

    game_objects.extend(to_add)
    if key_hander[key.ESCAPE]:
        ship = player.Player(img=resources.player_image, x=400, y=300, batch=main_batch)
        game_window.push_handlers(ship)
        game_window.push_handlers(ship.key_handler)


pyglet.clock.schedule_interval(update, 1/120.0)

@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()


if __name__ == "__main__":
    # Tell pyglet to do its thing
    pyglet.app.run()
