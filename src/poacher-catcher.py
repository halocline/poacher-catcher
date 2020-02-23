#!/usr/bin/env python3
# poacher-catcher.py
#
#
#

import math
import time

from aiy.leds import (Board, Led, Leds, Pattern, PrivacyLed, RgbLeds, Color)


def main():
    print('Press Button to get started. Ctrl-C to quit.')

    with Board() as board:
        while True:
            board.button.wait_for_press()
            print('ON')
            board.led.state = Led.ON
            board.button.wait_for_release()
            print('OFF')
            board.led.state = Led.OFF

        print('Done')


if __name__ == '__main__':
    main()
