#getting region for pyautogui
import keyboard
from pynput.mouse import Listener
import time

i=0
top = list(range(1, 5))
bottom = list(range(1, 5))


def on_click(x, y, button, pressed):
    if pressed:
        if i==0:
            top[0]=x
            bottom[0]=y
            print('Taking initial value.')
        if i==1:
            top[1]=x;bottom[1]=y
            top[2]=top[1]-top[0];bottom[2]=bottom[1]-bottom[0]
            print('Output complete: region=(',top[0],',',bottom[0],',',top[2],',',bottom[2],')')
            print(' ')
            print(' ')
        listener.stop()
while True:
    if keyboard.is_pressed('`'):
        print('***********Waiting for you click!**********')
        if i == 2:
            i=0
        with Listener(on_click= on_click ) as listener:
            listener.join()
            i=i+1

    #region=( 893 , 548 , 335 , 116 ) Resume video button
 


