import pyautogui
import time


time.sleep(3)
f = open("text.txt", "r")
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    time.sleep(1) 

""" time.sleep(3)

for i in range(10):
    pyautogui.typewrite("Spain the biggest country")
    pyautogui.press("enter")
 """