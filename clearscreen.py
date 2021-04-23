"""Clear console/terminal screen based on Operating System.
For Windows/MacOS/Linux
"""
import platform


def clear():
    if platform.system() == 'Windows':
        import os
        os.system('cls')
    else:
        import subprocess
        subprocess.run('clear', shell=True)
