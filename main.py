import SudokuFrames
import tkinter

if __name__ == '__main__':
    master = tkinter.Tk()
    master.title("SudokuSolver")
    master.geometry("603x440+500+170")
    widgets = SudokuFrames.create_board(master)
    for row in widgets:
        print(row)
    master.mainloop()
