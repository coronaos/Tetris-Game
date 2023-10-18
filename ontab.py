import os
import sys
import platform
import select
#import tty
#import termios
import time

def wait_for_input(timeout):
    if platform.system() == 'Windows':
        import msvcrt
        start_time = time.time()
        while time.time() - start_time < timeout:
            if msvcrt.kbhit():
                return msvcrt.getch().decode()
        return None

    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            rlist, _, _ = select.select([sys.stdin], [], [], timeout)
            if rlist:
                return sys.stdin.read(1)
            return None
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
