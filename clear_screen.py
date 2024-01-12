"""

A quick utility to clear console/terminal screen based on Operating System.
For Windows/MacOS/Linux.

VERSION = 0.1.1

"""

import platform
import os
import subprocess


def clear_screen():
    """Clears the console/terminal screen based on detected OS.
    """
    
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        # MacOS and Linux
        subprocess.run('clear', shell=True)
