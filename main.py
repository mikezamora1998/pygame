import pyglet
from pyglet.window import key
from pyglet.window import mouse

window = pyglet.window.Window(fullscreen=False, caption='pygame')
label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width // 2, y=window.height // 2,
                          anchor_x='center', anchor_y='center')


@window.event
def on_key_press(symbol, modifiers):
    label.text = key.symbol_string(symbol) + ' key was pressed'


@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        label.text = 'The left mouse button was pressed.'
    if button == mouse.RIGHT:
        label.text = 'The right mouse button was pressed.'


@window.event
def on_draw():
    window.clear()
    label.draw()


win_event_logger = pyglet.window.event.WindowEventLogger()
window.push_handlers(win_event_logger)

pyglet.app.run()
