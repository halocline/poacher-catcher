#!/usr/bin/env python3
# poacher-catcher.py
#

import datetime
import time

from aiy.board import Board, Led
from aiy.leds import (Leds, Pattern, PrivacyLed, RgbLeds, Color)
from aiy.toneplayer import TonePlayer


def printPressDuration():
    print('pressDuration')
    time.sleep(1)


def main():
    print('Press Button start. Hold Button for 5 seconds (or press Ctrl-C) to quit.')

    pressDuration = 0
    pressed = False

    with Board() as board:
        while True:
            board.button.wait_for_press()
            pressed = True
            pressTime = datetime.datetime.now()
            board.led.state = Led.ON
            print('ON')

            board.button.wait_for_release()
            pressed = False
            releaseTime = datetime.datetime.now()
            board.led.state = Led.OFF
            print('OFF')

            while pressed:
                printPressDuration()

            pressDuration = releaseTime - pressTime
            print('Button pressed for ' + str(pressDuration.seconds) + ' seconds')
            if pressDuration.seconds >= 5:
                Leds().pattern = Pattern.blink(500)
                Leds().update(Leds.rgb_pattern(Color.PURPLE))
                time.sleep(3)
                TonePlayer(22).play(*['E5q',
                                      'Be',
                                      'C5e',
                                      'D5e'])
                break

        print('Done')


if __name__ == '__main__':
    main()
