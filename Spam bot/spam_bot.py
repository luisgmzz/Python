import time
from pynput import keyboard
import pyautogui as pg

# Type the number you want to display
num = 4637


def press(key):
    n = num
    if key.char == ("t"):
        pg.press("backspace")
        pg.typewrite(str(n))
        pg.press("enter")

    return False


def on_release(key):

    print('{0} released'.format(
        key))

    if key == keyboard.Key.esc:
        return False


while True:

    with keyboard.Listener(
        on_press=press,
        on_release=on_release
    ) as listener:
        listener.join()

    num += 2
