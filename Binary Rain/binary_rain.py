'''
Binary Matrix Rain
'''
import os
import sys
import time
from random import randint
TERM_COLORS = ['\033[95m',
               '\033[94m',
               '\033[92m',
               '\033[93m',
               '\033[91m',
               '\033[0m',
               '\033[1m',
               '\033[4m']
def binary_rain():
    '''
    Executes the binary rain based on the TERM_COLORS constants.
    '''
    while True:
        term_height, term_width = os.popen("stty size", 'r').read().split()
        term_height, term_width = int(term_height), int(term_width)
        for col in xrange(term_height):
            for row in xrange(term_width):
                color = TERM_COLORS[randint(0, len(TERM_COLORS) - 1)]
                character = [str(randint(0, 1)), ' '][randint(0, 1)]
                sys.stdout.write(color + character)
                time.sleep(1 / (10 ** randint(9, 10)))
            print

if __name__ == "__main__":
    binary_rain()
