#!/usr/bin/env python3
# poacher-catcher.py
#
#
#

from aiy.board import Board, Led
from aiy.leds import (Leds, Pattern, PrivacyLed, RgbLeds, Color)


def main():
    print('Press Button to get started. Ctrl-C to quit.')

    count = 0

    def onButtonPress(count):
        print('Button Pressed')
        count += 1
        print(count)
        return count

    with Board() as board:
        while True:
            board.button.wait_for_press()
            count = onButtonPress(count)
            print('ON')
            board.led.state = Led.ON
            board.button.wait_for_release()
            print('OFF')
            board.led.state = Led.OFF

        print('Done')


if __name__ == '__main__':
    main()
