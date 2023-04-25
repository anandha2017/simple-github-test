import curses
import random
import time

# def matrix(window):
#     code_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_-+=[]{}|;:,.<>?/\\'
#     num_columns = window.getmaxyx()[1]
#     columns = [0] * num_columns

#     while True:
#         try:
#             for i in range(num_columns):
#                 if columns[i] == 0 and random.random() < 0.05:
#                     columns[i] = random.randint(1, 10)
#                 elif columns[i] > 0:
#                     char = random.choice(code_chars)
#                     attr = curses.A_BOLD if random.random() < 0.2 else curses.A_NORMAL
#                     window.addch(columns[i] - 1, i, char, attr)
#                     window.addch(columns[i], i, char, attr | curses.color_pair(1))

#                     columns[i] += 1
#                     if columns[i] >= window.getmaxyx()[0]:
#                         columns[i] = 0

#             window.refresh()
#             time.sleep(0.1)
#             window.erase()

#             key = window.getch()

#             # Exit the loop if the 'q' key is pressed
#             if key == ord('q'):
#                 break

#         except KeyboardInterrupt:
#             break
        

def matrix(window):
    code_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_-+=[]{}|;:,.<>?/\\'
    num_columns = window.getmaxyx()[1]
    columns = [0] * num_columns

    while True:
        try:
            for i in range(num_columns):
                if columns[i] == 0 and random.random() < 0.05:
                    columns[i] = random.randint(1, 10)
                elif columns[i] > 0:
                    char = random.choice(code_chars)
                    attr = curses.A_BOLD if random.random() < 0.2 else curses.A_NORMAL

                    # Check if the position is within the window boundaries
                    if columns[i] - 1 < window.getmaxyx()[0] - 1:
                        window.addch(columns[i] - 1, i, char, attr)

                    # Check if the position is within the window boundaries
                    if columns[i] < window.getmaxyx()[0] - 1:
                        window.addch(columns[i], i, char, attr | curses.color_pair(1))

                    columns[i] += 1
                    if columns[i] >= window.getmaxyx()[0]:
                        columns[i] = 0

            window.refresh()
            time.sleep(0.1)
            window.erase()
            
            key = window.getch()

            # Exit the loop if the 'q' key is pressed
            if key == ord('q'):
                break

        except KeyboardInterrupt:
            break

def main(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    stdscr.nodelay(1)
    curses.curs_set(0)
    matrix(stdscr)

if __name__ == '__main__':
    curses.wrapper(main)
