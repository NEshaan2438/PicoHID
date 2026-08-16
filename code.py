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

while True:
    if switchInput.value:
        USBMouse.move(x=5, y=5)
        print(switchInput.value)
    time.sleep(0.75)