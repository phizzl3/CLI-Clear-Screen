__version__ = "1.1.0"

import platform
import os


def clear_screen():
    os.system(f"{'cls' if platform.system() == 'Windows' else 'clear'}")


if __name__ == "__main__":
    clear_screen()
