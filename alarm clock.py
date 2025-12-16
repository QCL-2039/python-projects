import pygame
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(total_time):
    print(CLEAR)
    while total_time > 0:
        hours = total_time // 3600
        minutes = (total_time % 3600) // 60
        seconds = total_time % 60

        print(f"{CLEAR_AND_RETURN}Alarm will ring in {hours:02d}:{minutes:02d}:{seconds:02d}")
        time.sleep(1)
        total_time -= 1

    pygame.mixer.init()
    pygame.mixer.music.load("birds.wav")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pass

try:
    h, m, s = map(int, input("Enter hours minutes seconds: ").split())
    total_time = h * 3600 + m * 60 + s
    print("Total seconds:", total_time)
    alarm(total_time)

except ValueError:
    print("Please enter exactly 3 integers separated by spaces.")
