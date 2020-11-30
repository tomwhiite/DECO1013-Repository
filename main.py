from microbit import *
from gesture import *
from ultrasonic import *
import music
import neopixel
import random
from random import randint

rf = Rangefinder(pin2)
threshold = 100

gesture = Gesture()
np = neopixel.NeoPixel(pin1, 29)

words = ["Hey there!", "How're you going?", "Got a study plan?", "Time for a break"]
right_words = ["Go you", "You got this!", "You're doing amazing!", "Look at you go!"]
left_words = [
    "Are you doing work?",
    "Be sure not to overwork",
    "Have you taken a break?",
]
down_words = ["Have a nice day!"]

display.scroll(random.choice(words))


clockwise = Image("99999:" "00009:" "09009:" "99990:" "09000:")
anticlockwise = Image("99999:" "90000:" "90090:" "09999:" "00090:")
forward = Image("09090:" "99099:" "00000:" "99099:" "09090:")
backward = Image("99099:" "90009:" "00000:" "90009:" "99099:")
wave = Image("00090:" "99999:" "00000:" "99999:" "09000:")

gesture_map = {
    "up": Image.FABULOUS,
    "down": Image.SAD,
    "left": Image.SURPRISED,
    "right": Image.CHESSBOARD,
    "forward": forward,
    "backward": backward,
    "clockwise": clockwise,
    "anticlockwise": anticlockwise,
    "wave": wave,
}

display.show(Image.YES)
sleep(500)

while True:

    g = gesture.read()
    dist = rf.distance_cm()

    if g == "none":
        display.clear()

    else:
        print(g)
        display.show(gesture_map[g])
        sleep(300)

    if dist < threshold:
        display.show(Image.HAPPY)

    if g == "up":
        for pixel_id in range(0, len(np)):
            red = randint(0, 60)
            green = randint(0, 60)
            blue = randint(0, 60)
            np[pixel_id] = (red, green, blue)
            np.show()

        music.play(music.POWER_UP)

    elif g == "right":
        display.scroll(random.choice(right_words))
        pin0.analog_write(10)

    elif g == "left":
        display.scroll(random.choice(left_words))

    elif g == "down":
        np.clear()
        music.play(music.POWER_DOWN)
        display.scroll(random.choice(down_words))
        sleep(150)
