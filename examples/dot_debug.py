from bluedot import BlueDot
from bluedot.dot import MockBlueDot
from time import sleep

dot = MockBlueDot(auto_start_server = False)

def pressed(pos):
    print("Pressed: x-{} y-{} angle-{} distance-{} middle-{} top-{} bottom-{} left-{} right-{}".format(pos.x, pos.y, pos.angle, pos.distance, pos.middle, pos.top, pos.bottom, pos.left, pos.right))

def released():
    print("Released: x-{} y-{}".format(dot.position.x, dot.position.y))
    print()

def moved(pos):
    print("Moved: x-{} y-{}".format(pos.x, pos.y))

dot.when_pressed = pressed
dot.when_released = released
dot.when_moved = moved
dot.start()
dot.server.mock_client_connected()
dot.wait_for_connection()

try:
    while True:
        dot.server.mock_blue_dot_pressed(1.0,1.0)
        sleep(0.1)
finally:
    dot.stop()
