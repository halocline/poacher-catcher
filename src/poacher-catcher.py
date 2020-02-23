#!/usr/bin/env python3
# poacher-catcher.py
#

import datetime

from aiy.board import Board, Led
from aiy.leds import (Leds, Pattern, PrivacyLed, RgbLeds, Color)


def main():
    print('Press Button to get started. Ctrl-C to quit.')

    count = 0

    def onButtonPress(count):
        print('Button Pressed')
        print(count)
        return count

    with Board() as board:
        while True:
            board.button.wait_for_press()
            pressTime = datetime.datetime.now()
            board.led.state = Led.ON
            print('ON')
            count = onButtonPress(count)

            board.button.wait_for_release()
            releaseTime = datetime.datetime.now()
            board.led.state = Led.OFF
            print('OFF')

            pressDuration = releaseTime - pressTime
            print('Button pressed for ' + str(pressDuration.seconds) + ' seconds')
            if pressDuration.seconds >= 5:
                break

        print('Done')


if __name__ == '__main__':
    main()
