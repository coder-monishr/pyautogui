import pyautogui as pg
import time

print("startin in 5 seconds~")
time.sleep(5)

for i in range(50):
    pg.write("Hello")
    pg.press("Enter")
