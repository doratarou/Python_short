#Input Key_press and Key_Output . use pynput and PyAutoGui.

from curses.ascii import ctrl
from time import sleep
from pynput import keyboard

import pyautogui

isSpace = 0
isRightShift = 0
isLeftShift =0


def on_press(key):
    global isSpace
    global isRightShift
    global isLeftShift

    try:

        if key == keyboard.Key.shift_l:
            isLeftShift = 1

        if key == keyboard.Key.shift_r:
            isRightShift = 1
        if key == keyboard.Key.space:
            isSpace = 1

    except AttributeError:#念の為

        if key == keyboard.Key.shift_l:
            isLeftShift = 1
            
        if key == keyboard.Key.shift_r:
            isRightShift = 1
        if key == keyboard.Key.space:
            isSpace = 1
        


        
def on_release(key):
    
    global isSpace
    global isRightShift
    global isLeftShift
    global pyautogui


    if key == keyboard.Key.esc:
        # Stop listener
        return False
    
    if isSpace ==1 and isRightShift ==1:#This is a Shortcat's command
        #Pleas Write action

        pyautogui.press("backspace")
        pyautogui.hotkey("shift",'ctrl',';')

        
    elif isSpace ==1 and isLeftShift ==1:
        pyautogui.press("backspace")
        pyautogui.hotkey("shift",'ctrl','j')

    if key == keyboard.Key.shift:
        isLeftShift = 0

    if key == keyboard.Key.shift_r:
        isRightShift = 0
    if key == keyboard.Key.space:
        isSpace = 0

 

# Collect events until released
with keyboard.Listener(on_press=on_press , on_release=on_release) as listener:#Keyboard.listener() = キーボードの動きを検知して　それにともない関数（on_press　など）を実行
        listener.join()#特殊な文字を許可する的な　変換する的な　そんな感じ　のと　スタートの意を併せ持ってる感じだと思われる

    

