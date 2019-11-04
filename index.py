import time
from rotary_encoder import RotaryEncoder
from light_array import LightArray
import signal
import subprocess
import sys
import math

ROTARY_PIN_A = 19
ROTARY_PIN_B = 26
ROTARY_PIN_BUTTON = 13

LED_PINS = [ 5, 6, 13, 19, 26 ]  # 29, 31, 33, 35, 37
LED_ARRAY = [ [ 1, 2 ], [ 2, 1 ], [ 2, 3 ], [ 3, 2 ], [ 1, 3 ], [ 3, 1 ], [ 0, 2 ], [ 2, 0 ], [ 0, 3 ], [ 3, 0 ], [ 0, 1 ], [ 1, 0 ], [ 0, 4 ], [ 4, 0 ], [ 1, 4 ], [ 4, 1 ], [ 2, 4 ], [ 4, 2 ], [ 3, 4 ], [ 4, 3 ] ]

if __name__ == "__main__":
    print "start"

    initial_percentage = 0
    counter = Counter(initial_percentage)
    light_array = LightArray(LED_PINS, LED_ARRAY)

    def on_turn(delta):
        counter.count(delta)
        print counter.percentage

    def on_click(value):
        print("Button Press")

    def on_exit(a, b):
        print("Exiting...")
        encoder.destroy()
        sys.exit(0)

    encoder = RotaryEncoder(ROTARY_PIN_A, ROTARY_PIN_B, callback=on_turn,
                            buttonPin=ROTARY_PIN_BUTTON, buttonCallback=on_click)
    signal.signal(signal.SIGINT, on_exit)

    while True:
        light_array.set_value(counter.percentage)
