import pyautogui
from pywinauto import *

""" only the opening functions are carried out"""

def open_this_pc():
    pyautogui.hotkey('winleft', 'd')
    pyautogui.doubleClick(39,127)

def open_notepad():
    pyautogui.hotkey('win', 'r')
    pyautogui.typewrite('notepad')
    pyautogui.hotkey('\n')


def open_browser():
    pyautogui.hotkey('win', 'r')
    pyautogui.typewrite('chrome')
    pyautogui.hotkey('\n')


def open_cmd():
    pyautogui.hotkey('win', 'r')
    pyautogui.typewrite('cmd')
    pyautogui.hotkey('\n')

open_cmd()
