import pyautogui
import time

def click_match_found():
    while True:
        try:
            button_location = pyautogui.locateCenterOnScreen('match_found.png', confidence=0.5)
            if button_location:
                print("Button found! Clicking...")
                pyautogui.click(button_location)
                break  
            else:
                print("Button not found, trying again...")       
        except Exception as e:
            print(The screen is being scanned.., e)        
        time.sleep(3)
click_match_found()
