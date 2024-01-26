"""

A quick utility to clear console/terminal screen based on Operating System.
For Windows/MacOS/Linux.


"""

__version__ = "1.0.0"


import platform
import os
import subprocess


def clearscreen():
    """Clears the console/terminal screen based on detected OS.
    """
    
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        # MacOS and Linux
        subprocess.run('clear', shell=True, check=False)
