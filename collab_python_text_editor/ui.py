from curses import wrapper
import curses
from typing import Tuple


class UIState:
    text: list[str]
    cursor_pos: Tuple[int, int]

    def __init__(self, text: list[str], cursor_pos: Tuple[int, int]):
        self.text = text
        self.cursor_pos = cursor_pos


def run_ui(stdscr):
    state = UIState(cursor_pos=(0, 0), text=[""])

    while True:
        height, width = stdscr.getmaxyx()
        stdscr.clear()

        for i, line in enumerate(state.text):
            if i < height:
                stdscr.addstr(i, 0, line[: width - 1])

        stdscr.move(
            state.cursor_pos[1], state.cursor_pos[0]
        )  # Curses usex y,x coordinates

        stdscr.refresh()
        key = stdscr.getch()
        state = _process_key(key, state)


def _process_key(key, state):
    current_text_lines = state.text
    cursor_x = state.cursor_pos[0]
    cursor_y = state.cursor_pos[1]

    if key == ord("\n"):
        current_line = (
            current_text_lines[cursor_y] if cursor_y < len(current_text_lines) else ""
        )
        left_part = current_line[:cursor_x]
        right_part = current_line[cursor_x:]
        current_text_lines[cursor_y : cursor_y + 1] = [left_part, right_part]
        cursor_y += 1
        cursor_x = 0
    elif key == ord("q"):
        raise Exception("exit")
    elif 32 <= key <= 126:
        if cursor_y == len(current_text_lines):
            current_text_lines.append("")

        current_line = current_text_lines[cursor_y]
        new_line = current_line[:cursor_x] + chr(key) + current_line[cursor_x:]
        current_text_lines[cursor_y] = new_line
        cursor_x += 1

    return UIState(text=current_text_lines, cursor_pos=(cursor_x, cursor_y))


wrapper(run_ui)
