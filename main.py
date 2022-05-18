# This is a main file that autolikes the Weekly Basketball page
# Anil Yesilkaya | MathWorks | 13.05.2022
###############################################################################
from pynput.keyboard import Key, Controller
import time
import webbrowser 
import pyautogui
###############################################################################
def main():
    keyboard = Controller()
    #
    url = "https://www.facebook.com/groups/1219950278020463?sorting_setting=CHRONOLOGICAL" # any Facebook URL
    webbrowser.open_new_tab(url) # open a new tab
    # RUN WHILE LOOP 
    #while True:
    if True:
        time.sleep(8.0) # to pause
        keyboard.press('j')
        keyboard.release('j')
        keyboard.press('l')
        keyboard.release('l')
        pyautogui.press('enter')
        keyboard.press(Key.f5)
        keyboard.release(Key.f5)
###############################################################################
if __name__ == '__main__':
    main()


