import pyautogui
import pytesseract
import PIL
import sys
import os

screenshot = pyautogui.screenshot()

text = str(pytesseract.image_to_string(screenshot))
text = text.replace("-\n", "fallo")

print(text)