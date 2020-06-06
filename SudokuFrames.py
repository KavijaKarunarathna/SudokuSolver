from SampleSudokus import picked_board
import tkinter
import pyglet
pyglet.font.add_file('font 2.otf')


class BoardLabel:

    def __init__(self, frame, row, col):
        self.widget = tkinter.Label(frame, borderwidth=4, relief='groove', width=3, height=1, font="ABeeZee 25",
                                    fg="white", background="#138D75")
        self.widget.grid(row=row, column=col)

    def add_to_label(self, char):
        self.widget.config(text=char)


def create_board(window):
    widgets = []
    board = tkinter.Frame(window)
    for row in range(9):
        for col in range(9):
            label = BoardLabel(board, row, col)
            label.add_to_label(picked_board[row][col])
            widgets.append(label)
    board.grid(row=0, column=0, rowspan=9, columnspan=9)
    return widgets



