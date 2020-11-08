try:
    import tkinter
except ImportError:
    import Tkinter as tkinter
import functions

keys = [
    [('C', 1), ('CE', 1)],
    [('1', 1), ('2', 1), ('3', 1), ('+', 1)],
    [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
    [('7', 1), ('8', 1), ('9', 1), ('*', 1)],
    [('0', 1), ('=', 1), ('/', 1)]
]

mainWindow = tkinter.Tk()
mainWindow.title("Calculator")
mainWindow.geometry("640x480-8-200")
mainWindow["padx"] = 8

result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, sticky='nsew')

keyPadFrame = tkinter.Frame(mainWindow)
keyPadFrame.grid(row=1, column=0, sticky='nsew')

row = 0
for keyRow in keys:
    col = 0
    for key in keyRow:
        tkinter.Button(keyPadFrame, text=key[0]).grid(row=row, column=col, columnspan=key[1], sticky=tkinter.E + tkinter.W)
        col += key[1]
    row += 1

mainWindow.update()
mainWindow.minsize(keyPadFrame.winfo_width() + 8, result.winfo_height() + keyPadFrame.winfo_height())
mainWindow.maxsize(keyPadFrame.winfo_width() + 58, result.winfo_height() + keyPadFrame.winfo_height())
mainWindow.mainloop()
