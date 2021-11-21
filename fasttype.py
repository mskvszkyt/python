import random
import curses
from curses import wrapper


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0,"Hello! \nDo you want to play? \nPress any button.", curses.color_pair(1))
    stdscr.refresh()
    stdscr.getkey()

def word_per_min(stdscr):
    texts = ["Suspendisse nulla dolor efficitur quis urna sit amet ullamcorper pretium.", "Pellentesque tempus justo sed porttitor auctor. Etiam tristique velit non.","Interdum et malesuada fames ac ante ipsum primis in faucibus.","Praesent auctor massa id nisl vestibulum", "Ut finibus purus sit amet diam ullamcorper sed iaculis nisl molestie.","Quisque egestas tristique augue quis porta.","Maecenas consectetup lacus nec posuere placerat tellus ligula iaculis augu nec vestibulum eros nibh eget nunc."]
    target_text = random.choice(texts)
    current_text = []

    while True:
        stdscr.clear()
        stdscr.addstr(target_text)
        key = stdscr.getkey()
        
        for character in current_text:
            stdscr.addstr(0,0,character, curses.color_pair(1))

        stdscr.refresh()

        if ord(key) == 27:
            break
        if key in ("KEY_BACKSPACE", '\b', '\x7f'):
            if len(current_text) > 0:
                current_text.pop()

        else:
            current_text.append(key)

        current_text.append(key)    
        


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)


    start_screen(stdscr)
    word_per_min(stdscr)

wrapper(main)







