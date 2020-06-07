from SampleSudokus import picked_board
import tkinter
import pyglet
pyglet.font.add_file('font 2.otf')


class BoardLabel:

    def __init__(self, frame, row, col):
        self.widget = tkinter.Label(frame, borderwidth=4, relief='groove', width=3, height=1, font="ABeeZee 25",
                                    fg="white", background="#138D75")
        self.widget.grid(row=row, column=col)

    def add_to_label(self, char, widgets):
        self.widget.config(text=char)
        widgets.append(self.widget)


def create_board(window):
    widgets = []
    board = window
    for row in range(9):
        for col in range(9):
            label = BoardLabel(board, row, col)
            label.add_to_label(picked_board[row][col], widgets)
    board.grid(row=0, column=0, rowspan=9, columnspan=9)
    n = 9
    widgets = [widgets[i * n:(i + 1) * n] for i in range((len(widgets) + n - 1) // n)]
    # widgets.pop()
    # print(widgets)
    return widgets



