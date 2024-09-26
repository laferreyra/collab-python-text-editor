import curses
import sys
import os
import random
import string
from threading import Thread

from collab_python_text_editor import ui


def generate_random_filename():
    return (
        "".join(random.choices(string.ascii_lowercase + string.digits, k=10)) + ".txt"
    )


def load_file(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return file.read().splitlines()
    return []


def save_file(filename, content):
    with open(filename, "w") as file:
        file.write("\n".join(content))


def main():
    ui_thread = Thread(target=ui)
    ui_thread.run()


if __name__ == "__main__":
    # if len(sys.argv) > 1:
    #     filename = sys.argv[1]
    # else:
    #     filename = None
    # curses.wrapper(lambda stdscr: main(stdscr, filename))
    main()
