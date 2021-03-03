import pyautogui
import time

time.sleep(5)

i=1
while i>0:
    f = open("spammerino", "r")
    for words in f:
        pyautogui.typewrite(words)
        pyautogui.press("enter")
    f.close()




