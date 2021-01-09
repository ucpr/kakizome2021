import time
import sys
import shutil


template = """
┏━━━━━━━┓
┃ ━ ╋━╋ ┃
┃ ━ ┏┳┓ ┃
┃ ━ ┗╋┛ ┃
┃ ━ ━╋━ ┃
┃ ┏┓━╋━ ┃
┃ ┗┛━┻━ ┃
┃       ┃
┃ ╋┓┏┓  ┃
┃ ┃┃┗┛  ┃
┃ ┏━━┓  ┃
┃ ┣━━┫  ┃
┃ ┣━━┫  ┃
┃ ┗┳┳┛  ┃
┃       ┃
┃ ┳┻┳┏━ ┃
┃ ┻━┻┃　┃
┃ ━╋━┣┳ ┃
┃ ┏╋┓┃┃ ┃
┃ ┃┃┃┃┃ ┃
┃ ┃┃┃┃┃ ┃
┃       ┃
┃ ┣━━┳━ ┃
┃ ┛　┃　┃
┃  ┏━╋━ ┃
┃  ┃ ┃  ┃
┃  ┻━╋━ ┃
┃　　┃  ┃
┗━━━━━━━┛ 
"""

lines = template.strip().split("\n")

pos = 0
columns = shutil.get_terminal_size().columns

while True:
    for i in range(16):
        for j in range(16):
            sys.stdout.write("\x1B[2J\x1B[H")
            sys.stdout.flush()

            v = i * 16 + j
            for line in lines:
                sys.stdout.write(f"\033[{pos}C")
                sys.stdout.write(f"\033[38;5;{v}m{line}\033[0m\n")
                #print(f"\033[38;5;{v}m{k}\033[0m", end="")
            sys.stdout.flush()

            pos += 1
            if pos + 9 > columns:
                pos = 0

        time.sleep(0.2) 
