import time
import pyautogui
import keyboard
import threading
from tkinter import *

pyautogui.hotkey('alt', 'tab')

def find_image_on_screen(image_path, confidence=0.9):
    try:
        position = pyautogui.locateOnScreen(image_path, confidence=confidence)
    except TypeError:
        print("Image not found on the screen.")
        return None

    return position

def move_mouse_to_image(image_path, confidence=0.9):
    image_position = find_image_on_screen(image_path, confidence)
    if image_position:
        # Get the center coordinates of the image
        x, y, width, height = image_position
        image_center_x = x + width / 2
        image_center_y = y + height / 2

        # Move the mouse to the center of the image
        pyautogui.moveTo(image_center_x, image_center_y, duration=0.5)
        time.sleep(2)
        return True
    else:
        print("Image not found. Mouse not moved.")
        return False

def on_esc_press(event):
    global stop_flag
    if event.name == "esc":
        if stop_flag:
            stop_flag = False
            print("Script resumed by user.")
        else:
            stop_flag = True
            print("Script paused by user.")
    time.sleep(0.0001)

stop_flag = False

if __name__ == "__main__":
    # Replace 'newlikeButton.png' with the actual path to the image you want to find
    image_path = "D:/pyScripts/Onlyfans/newlikeButton.png"

    # Register the callback for the "Esc" key press
    keyboard.on_press_key("esc", on_esc_press)

    for z in range(0, 100):
        if stop_flag == False:
            if find_image_on_screen(image_path, confidence=0.9):
            # Image found, move the mouse to it
                if move_mouse_to_image(image_path, confidence=0.9):
                    time.sleep(1)
                    pyautogui.press('l')
                    pyautogui.click()  # Click at the current mouse position
                    time.sleep(1)

            time.sleep(1)
            pyautogui.press('right')
            time.sleep(1)
        else:
            time.sleep(1)

    # Unregister the "Esc" key press callback
    keyboard.unhook_all()

