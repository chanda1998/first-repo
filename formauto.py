import pyautogui
import automation
pyautogui.PAUSE = 0.5
automation.open_browser()
pyautogui.hotkey('win', 'up')
pyautogui.typewrite('irctc')
pyautogui.hotkey('\n')



pyautogui.PAUSE = 3

pyautogui.click(217,362)
pyautogui.PAUSE = 2
pyautogui.typewrite('dbg')
pyautogui.hotkey('\n')
pyautogui.hotkey ('tab')
pyautogui.typewrite ('ndls')
