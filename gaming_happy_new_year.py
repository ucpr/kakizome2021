from argparse import ArgumentParser
import time
import sys
import shutil



template_en = """
##
##
#####   ####  #####  #####  ##  ##   #####   ####  ##   ##   ##  ##  ####   ####  #####
##  ##     ## ##  ## ##  ## ##  ##   ##  ## ##  ## ## # ##   ##  ## ##  ##     ## ##  ##
##  ##  ##### ##  ## ##  ## ##  ##   ##  ## ###### #######   ##  ## ######  ##### ##
##  ## ##  ## #####  #####   #####   ##  ## ##      #####     ##### ##     ##  ## ##
##  ##  ##### ##     ##        ##    ##  ##  #####  ## ##       ##   #####  ##### ##
              ##     ##     ####                             ####
"""

template_ja = """
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


def gaming(lines, w=90):
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
                if pos + w > columns:
                    pos = 0
    
            time.sleep(0.2) 

    
def get_option():
    arg_parser = ArgumentParser()
    arg_parser.add_argument(
        "-l",
        "--language",
	type=str,
        dest="lang",
	default="en",
	choices=["en", "english", "ja", "japanese"],
    )
    return arg_parser.parse_args()


def main():
    opt = get_option()

    template = template_en
    if opt.lang in ["ja", "japanese"]:
        template = template_ja

    lines = template.strip().split("\n")
    gaming(lines)


if __name__ == "__main__":
    main()
