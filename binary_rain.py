'''
Binary Matrix Rain
'''
import os
import sys
import random
import time
TERM_HEIGHT, TERM_WIDTH = os.popen("stty size", 'r').read().split()
TERM_HEIGHT, TERM_WIDTH = int(TERM_HEIGHT), int(TERM_WIDTH)
TERM_COLORS = ['\033[95m',
               '\033[94m',
               '\033[92m',
               '\033[93m',
               '\033[91m',
               '\033[0m',
               '\033[1m',
               '\033[4m']
while True:
    # os.system("cls" if os.name == "nt" else "clear")
    for x in xrange(TERM_HEIGHT):
        for y in xrange(TERM_WIDTH):
            color = TERM_COLORS[random.randint(0, len(TERM_COLORS) - 1)]
            character = [str(random.randint(0, 1)), ' '][random.randint(0, 1)]
            sys.stdout.write(color + character)
            time.sleep(1 / (10 ** random.randint(9, 10)))
        print
