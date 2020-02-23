#!/usr/bin/env python3
# poacher-catcher.py
#

import datetime

from aiy.board import Board, Led
from aiy.leds import (Leds, Pattern, PrivacyLed, RgbLeds, Color)


def main():
    print('Press Button start. Hold Button for 5 seconds (or press Ctrl-C) to quit.')

    Leds().update(Leds.rgb_on(Color.PURPLE))

    with Board() as board:
        while True:
            board.button.wait_for_press()
            pressTime = datetime.datetime.now()
            board.led.state = Led.ON
            print('ON')

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
