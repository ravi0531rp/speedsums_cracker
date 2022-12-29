import pyautogui
import time
import pyperclip
import webbrowser

webbrowser.open("https://speedsums.com/")

time.sleep(3)

while True:
    pyautogui.tripleClick(988,443)
    pyautogui.hotkey('ctrl', 'c')
    pyperclip.copy(eval(pyperclip.paste().replace("x","*").replace("÷","//").replace("=","")))
    pyautogui.click(987,508)
    pyautogui.hotkey('ctrl', 'v')
