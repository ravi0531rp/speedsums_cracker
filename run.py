import pyautogui
import webbrowser
import time
import pyperclip
from collections import namedtuple

url = "https://speedsums.com/index.html"

time.sleep(3)

Point = namedtuple("Point", "x y")

# question_coordinates_start = Point(800,445)
# question_coordinates_end = Point(960,445)

question_coordinates_start = Point(820,445)
question_coordinates_end = Point(930,445)

answer_coordinates = Point(882,511)

while True:
    pyautogui.moveTo(question_coordinates_start.x, question_coordinates_start.y)
    pyautogui.click()
    pyautogui.dragTo(question_coordinates_end.x,question_coordinates_end.y, button='left')
    pyautogui.hotkey('command', 'c')
    pyperclip.copy(eval(pyperclip.paste().replace("x","*").replace("÷","//").replace("=","")))
    pyautogui.click(answer_coordinates.x, answer_coordinates.y)
    pyautogui.hotkey('command', 'v')
