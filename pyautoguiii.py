"""
PYAUTOGUI -> Simula cliques de rato e toques de teclado para automatizar tarefas repetitivas

"""

import pyautogui
import time

time.sleep(2)

pyautogui.press("win")
time.sleep(1)

pyautogui.write("calculadora")
time.sleep(1)

pyautogui.press("enter")
time.sleep(2)

pyautogui.write("10*10")
time.sleep(1)

pyautogui.press("=")
time.sleep(1)


