from RPi import GPIO
import math
import time

class LightArray:
    def __init__(self, pins, leds, include_zero = False):
        self.DELAY = 0.001 # 1 millisecond
        self.led_array = led_array
        self.pins = pins
        self.include_zero = include_zero

        GPIO.setmode(GPIO.BCM)
        for pin in pins:
            GPIO.setup(pin, GPIO.IN)

        if include_zero:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pins[led_array[0][0]], GPIO.HIGH)
            GPIO.output(pins[led_array[0][1]], GPIO.LOW)

    def set_value(self, percentage):
        value_leds = len(self.led_array)
        if self.include_zero:
            value_leds-=1;

        n_pins = int(math.floor(percentage / value_leds))
        for i in range(len(self.led_array)):
            if i <= n_pins:
                self.light_led(self.led_array[i])

    def light_led(self, led_pins):
        pinX = self.pins[led_pins[0]]
        pinY = self.pins[led_pins[1]]

        GPIO.setup(pinX, GPIO.OUT)
        GPIO.setup(pinY, GPIO.OUT)

        GPIO.output(pinX, GPIO.HIGH)
        GPIO.output(pinY, GPIO.LOW)

        time.sleep(self.DELAY)

        GPIO.output(pinX, GPIO.LOW)

        GPIO.setup(pinX, GPIO.IN)
        GPIO.setup(pinY, GPIO.IN)
