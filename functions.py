import pyautogui as sistema
from time import sleep
import pyperclip as copy_text
import pygetwindow as gw

def openWebService(url):
  sistema.press('win')
  sleep(0.3)
  sistema.write('edge')
  sleep(0.3)
  sistema.press('enter')
  copy_text.copy(url)
  sleep(1)
  sistema.hotkey('Ctrl', 'v')
  sistema.press('enter')
  sleep(3)

  return True

def openSystemService(appname):
  sistema.press('win')
  sleep(0.3)
  sistema.write(appname)
  sleep(0.3)
  sistema.press('enter')
  sleep(3)

  return True

