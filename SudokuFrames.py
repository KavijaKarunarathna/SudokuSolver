from SampleSudokus import picked_board
import tkinter
import pyglet
pyglet.font.add_file('font 2.otf')


class BoardLabel:

    def __init__(self, frame, row, col):
        self.widget = tkinter.Label(frame, borderwidth=4, relief='groove', width=3, height=1, font="ABeeZee 25",
                                    fg="white", background="#138D75")
        self.widget.grid(row=row, column=col)
        self.labelText = tkinter.StringVar()
        self.widget.config(textvariable=self.labelText)

    def add_to_label(self, char, widgets, string_vars):
        self.labelText.set(char)
        widgets.append(self.widget)
        string_vars.append(self.labelText)


def create_board(window):
    widgets = []
    string_vars = []
    board = window
    for row in range(9):
        for col in range(9):
            label = BoardLabel(board, row, col)
            char = picked_board[row][col]
            label.add_to_label(char, widgets, string_vars)
    board.grid(row=0, column=0, rowspan=9, columnspan=9)
    n = 9
    widgets = [widgets[i * n:(i + 1) * n] for i in range((len(widgets) + n - 1) // n)]
    string_vars = [string_vars[i * n:(i + 1) * n] for i in range((len(string_vars) + n - 1) // n)]
    return widgets, string_vars



