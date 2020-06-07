import SudokuFrames
import tkinter
from SampleSudokus import picked_board
from time import sleep

temp_board = picked_board[::]
master = tkinter.Tk()
master.title("SudokuSolver")
master.geometry("603x500+500+170")
Frame = tkinter.Frame(master, background="#138D75")
widgets = SudokuFrames.create_board(Frame)
solve_btn = tkinter.PhotoImage(file="btn.png")
Button = tkinter.Button(Frame, image=solve_btn, command=lambda: solve(temp_board, numbers))
Button.grid(row=9, column=0, columnspan=9, sticky='ew')
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def valid(board, cha, rw, column):
    if cha in board[rw]:
        return False
    for i in range(9):
        if cha in board[i][column]:
            return False
    return True


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == ' ':
                return i, j
    return False


def solve(board, number):
    find = find_empty(board)
    if not find:
        return True

    else:
        row, col = find

    for cha in number:
        if valid(board, cha, row, col):
            widgets[row][col].config(text=cha)
            widgets[row][col].config(background="#D1F2EB")
            widgets[row][col].config(fg="#1B4F72")
            board[row][col] = cha

            if solve(board, number):
                return True

            widgets[row][col].config(background="#D1F2EB")
            widgets[row][col].config(fg="#1B4F72")
            widgets[row][col].config(text=" ")
            board[row][col] = " "

    return False

master.mainloop()
