#!/usr/bin/env python3
# poacher-catcher.py
#

import datetime
import time

from aiy.board import Board, Led
from aiy.leds import (Leds, Pattern, PrivacyLed, RgbLeds, Color)
from aiy.pins import PIN_A
from aiy.toneplayer import TonePlayer
from aiy.vision.inference import CameraInference
from aiy.vision.models import face_detection

from gpiozero import OutputDevice

from picamera import PiCamera

device = OutputDevice(PIN_A)


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
                    print(device.is_active)
                    device.on()
                    print(device.is_active)
                    # device.on()
                    # time.sleep(200)
                    # device.off()
                    # break
                    Board().button.wait_for_press()
                    break

        # Stop preview
        camera.stop_preview()
        leds.update(Leds.privacy_on())


def main():
    print('Press Button start. Hold Button for 5 seconds (or press Ctrl-C) to quit.')

    pressDuration = 0

    with Board() as board, Leds() as leds:
        while True:
            board.button.wait_for_press()
            pressTime = datetime.datetime.now()
            board.led.state = Led.ON
            print('ON')
            print('Running facedetect')
            facedetect()

            leds.update(Leds.rgb_on((255, 20, 147)))

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
