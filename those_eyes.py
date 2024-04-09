import sys
from time import sleep
import time 

def print_colored_text(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m", end='')

def print_lyrics():
    lines = [
        ("cause all of the small", 0.1),
        ("things that you do", 0.1),
        ("are what remind me", 0.1),
        ("why I fell for you", 0.1),
        ("And when we're apart", 0.1),
        ("and I'm missing you", 0.1),
        ("I close my eyes and all I see is you",0.2),
    ]

    delays = [1, 1, 1, 1, 1, 1, 1]
    colors = [97, 97, 97, 97, 97, 97 , 91 ]

    for i, ((line, char_delay), color) in enumerate(zip(lines, colors)):
        for char in line:
            print_colored_text(char, color)
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics(
