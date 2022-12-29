import pyautogui
import time
import pyperclip

time.sleep(3)

while True:
    pyautogui.moveTo(820,445)
    pyautogui.click()
    pyautogui.dragTo(930,445, button='left')
    pyautogui.hotkey('command', 'c')
    pyperclip.copy(eval(pyperclip.paste().replace("x","*").replace("÷","//").replace("=","")))
    pyautogui.click(882,511)
    pyautogui.hotkey('command', 'v')
