# Alex Farley
# arf2846@rit.edu
# This program locks the workstation at random time intervals
# between 30 and 180 seconds.

import ctypes
import time
import sys
import random
import os

# ctypes.windll.user32.LockWorkStation()

# define variables
bindows = sys.platform          # for getting OS
rando = 0

# be annoying
while True:
    rando = random.randint(30, 180)
    time.sleep(rando)
    if bindows == "win32":
        user32 = ctypes.windll.user32   # for Windows
        user32.LockWorkStation()
    elif bindows == "linux":
        os.system("xdg-screensaver lock")