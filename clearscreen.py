__version__ = "1.0.0"

import platform
import os


def clear_screen():
    """Clears the console/terminal screen based on detected OS.
    """
    
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        # MacOS and Linux
        subprocess.run('clear', shell=True, check=False)
