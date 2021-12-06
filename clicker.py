from typing import Tuple
import keyboard
import mouse
import time

isClicking = False
def set_clicker():
    global isClicking
    if isClicking:
        isClicking = False
        print("Кликкер отключен")
    else:
        isClicking = True
        print("Кликкер включен")

keyboard.add_hotkey('Alt + z', set_clicker)

while True:
    if isClicking:
        mouse.double_click(button = 'left')
        time.sleep(0.01)