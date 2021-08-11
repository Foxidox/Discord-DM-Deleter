import time
from pynput.keyboard import Key, Controller

kb = Controller()

time.sleep(10) 

while True:
    kb.press(Key.up)
    kb.release(Key.up)
    time.sleep(0.2)
    kb.press(Key.ctrl)
    kb.press('a')
    kb.release(Key.ctrl)
    kb.release('a')
    time.sleep(0.2)
    kb.press(Key.delete)
    kb.release(Key.delete)
    time.sleep(0.3)
    kb.press(Key.enter)
    kb.release(Key.enter)
    time.sleep(0.3)
    kb.press(Key.enter)
    kb.release(Key.enter)
    time.sleep(0.5)
    kb.press(Key.delete)
    kb.release(Key.delete)
    time.sleep(0.5)
    








