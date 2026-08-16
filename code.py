import board
import digitalio

import usb_hid
from adafruit_hid.mouse import Mouse

import time

USBMouse = Mouse(usb_hid.devices)

# connected pins with a jumper wire that i can unplug/plug in when i want to debug
switchOutput = digitalio.DigitalInOut(board.GP0)
switchOutput.direction = digitalio.Direction.OUTPUT
switchOutput.value = True

switchInput = digitalio.DigitalInOut(board.GP1)
switchInput.direction = digitalio.Direction.INPUT
switchInput.pull = digitalio.Pull.DOWN

# right and down are positive
# dx,dy in pixels; t in milliseconds
def moveMouse(dX, dY, t):
    i = 0
    steps = t / 50
    vX = dX / steps
    vY = dY / steps

    while i < steps:
        USBMouse.move(vX, vY, 0)
        time.sleep(0.05)

# how much is one unit?? docs don't say
# dZ in scrolling units; t in milliseconds
def scrollMouse(dZ, t):
    i = 0
    steps = t / 100
    vZ = dZ / steps
    while i < (t / 100):
        USBMouse.move(0, 0, vZ)
        time.sleep(0.1)

# t in milliseconds
def holdLCMouse(t):
    USBMouse.press(Mouse.LEFT_BUTTON)
    time.sleep(t / 1000)
    USBMouse.release(Mouse.LEFT_BUTTON)

# t in milliseconds
def holdRCMouse(t):
    USBMouse.press(Mouse.RIGHT_BUTTON)
    time.sleep(t / 1000)
    USBMouse.release(Mouse.RIGHT_BUTTON)

while True:
    if switchInput.value:
        print(switchInput.value)
    time.sleep(0.75)