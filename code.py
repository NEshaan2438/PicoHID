import board
import digitalio

import time

switchOutput = digitalio.DigitalInOut(board.GP0)
switchOutput.direction = digitalio.Direction.OUTPUT
switchOutput.value = True

switchInput = digitalio.DigitalInOut(board.GP1)
switchInput.direction = digitalio.Direction.INPUT
switchInput.pull = digitalio.Pull.DOWN

while True:
    print(not switchInput.value)
    time.sleep(0.75)