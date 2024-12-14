import pygame
import time
import datetime
from colorama import Fore

def set_alarm():
    print("*"*40)
    print(Fore.GREEN + "           Python Alarm Clock")
    alarm_time = input(Fore.LIGHTWHITE_EX + "Set alarm for (HH:MM:SS): ").strip()
    is_running = True
    print("*"*40)
    print(Fore.GREEN + f"Alarm set successfully for {alarm_time}.")
    sound_file = 'Alarmsound.mp3'
    print("---")
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(Fore.YELLOW + "    " + current_time)
        time.sleep(1)

        if current_time == alarm_time:
            print(Fore.RED + "---\nTIME UP!!")
            pygame.mixer.music.play()
            input("Press ENTER to stop the music...")
            pygame.mixer.music.stop()
            print("*"*40)
            is_running = False

if __name__ == "__main__":
    set_alarm()