#!/usr/bin/env python3
# poacher-catcher.py
#

import datetime
import time

from gpiozero import OutputDevice, Buzzer, LED

from aiy.board import Board, Led
from aiy.leds import (Leds, Pattern, PrivacyLed, RgbLeds, Color)
from aiy.pins import PIN_A, PIN_B
from aiy.toneplayer import TonePlayer
from aiy.vision.inference import CameraInference
from aiy.vision.models import face_detection

from picamera import PiCamera

# device = OutputDevice(PIN_A)
bz = Buzzer(PIN_B)
led = LED(PIN_A)


def printPressDuration():
    print('pressDuration')
    time.sleep(1)


def facedetect():
    with PiCamera() as camera, Leds() as leds:
        # Configure camera
        camera.resolution = (1640, 922)  # Full Frame, 16:9 (Camera v2)
        camera.start_preview()
        leds.update(Leds.privacy_on())

        # Do inference on VisionBonnet
        with CameraInference(face_detection.model()) as inference:
            for result in inference.run():
                if len(face_detection.get_faces(result)) >= 1:
                    camera.capture(
                        'faces_' + str(datetime.datetime.now()) + '.jpg')
                    # print(device.is_active)
                    print(led.is_active)
                    # device.on()
                    # bz.on()
                    led.on()
                    print(led.is_active)
                    time.sleep(3)
                    # print(device.is_active)
                    continue
            Board().button.wait_for_press()

        # Stop preview
        camera.stop_preview()
        leds.update(Leds.privacy_on())


def startup():
    with Board() as board, Leds() as leds:
        colors = [Color.RED, Color.YELLOW, Color.GREEN, Color.CYAN,
                  Color.BLUE, Color.PURPLE, Color.BLACK, Color.WHITE]
        board.led.state = Led.ON
        leds.pattern = Pattern.breathe(1000)
        for color in colors:
            leds.update(Leds.rgb_pattern(color))
            time.sleep(2)
        TonePlayer(22).play(*[
            'Be',
            'rs',
            'C5e',
            'rs',
            'D5e',
        ])
        board.led.state = Led.OFF


def main():
    print('Press Button start. Press Button to stop camera.'
          + 'Press Button again (or press Ctrl-C) to quit.')
    startup()

    pressDuration = 0

    with Board() as board, Leds() as leds:
        while True:
            board.button.wait_for_press()
            pressTime = datetime.datetime.now()
            board.led.state = Led.ON
            print('ON')
            print('Running facedetect')
            facedetect()

            leds.update(Leds.rgb_on((107, 255, 0)))

            board.button.wait_for_release()
            releaseTime = datetime.datetime.now()
            board.led.state = Led.OFF
            print('OFF')

            pressDuration = releaseTime - pressTime
            print('Program ran for ' + str(pressDuration.seconds) + ' seconds')
            if pressDuration.seconds >= 5:
                leds.update(Leds.rgb_on(Color.PURPLE))
                time.sleep(3)
                TonePlayer(22).play(*[
                    'D5e',
                    'rq',
                    'C5e',
                    'rq',
                    'Be',
                    'rq',
                    'Be',
                    'C5e',
                    'D5e'
                ])
                break
            print('Done')


if __name__ == '__main__':
    main()
