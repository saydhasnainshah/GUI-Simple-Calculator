#PROBLEM WITH KEYBIND

from tkinter import *



class HoverButton(Button):
    def __init__(self, master, **kw):
        Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground

def evaluate():
    global equation 
    equation = equation.replace("^", "**")
    answer = eval(equation)
    return answer

def change(value):
    global equation
    if value in inputVals: 
        equation = equation + value
    elif value == "C":
        equation = ""
    elif value == "back":
        equation = equation[:-1]
    elif value == "=":
        equation = evaluate()

    display.configure(text = equation)


equation = ""

inputVals = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "^2", "^(0.5)", "+", "-", "*", "/" ]

root = Tk()
#root.geometry("340x545")

display = Label(root, text = "", bg = "gainsboro")
display.configure(height = 7, width = 47)
display.grid(columnspan = 4, rowspan = 2 )

clear = HoverButton(root, text = "C", command = lambda: change("C"), bg = "white", relief = "flat")
clear.config(height = 5, width = 10)
clear.grid(column = 3, row = 2, padx = 2, pady = 2)

backspace = HoverButton(root, text = "back", command = lambda: change("back"), bg = "white", relief = "flat")
backspace.configure(height = 5, width = 10)
backspace.grid(column = 2, row = 2, padx = 2, pady = 2)

square = HoverButton(root, text = "^2", command = lambda: change("^2"), bg = "white", relief = "flat")
square.configure(height = 5, width = 10)
square.grid(column = 1, row = 2)

squareroot = HoverButton(root, text = "sqrt", command = lambda: change("^(0.5)"), bg = "white", relief = "flat")
squareroot.configure(height = 5, width = 10)
squareroot.grid(column = 0, row = 2, padx = 2, pady = 2)

A = HoverButton(root, text = "+", command = lambda: change("+"), bg = "white", relief = "flat")
A.configure(height = 5, width = 10)
A.grid(column = 3, row = 3, padx = 2, pady = 2)

S = HoverButton(root, text = "-", command = lambda: change("-"), bg = "white", relief = "flat")
S.configure(height = 5, width = 10)
S.grid(column = 3, row = 4, padx = 2, pady = 2)

M = HoverButton(root, text = "*", command = lambda: change("*"), bg = "white", relief = "flat")
M.configure(height = 5, width = 10)
M.grid(column = 3, row = 5, padx = 2, pady = 2)

D = HoverButton(root, text = "/", command = lambda: change("/"), bg = "white", relief = "flat")
D.configure(height = 5, width = 10)
D.grid(column = 3, row = 6, padx = 2, pady = 2)

E = HoverButton(root, text = "=", command = lambda: change("="), bg = "sky blue", relief = "flat", activebackground = "skyblue2")
E.configure(height = 5, width = 10)
E.grid(column = 2, row = 6, padx = 2, pady = 2)

seven = HoverButton(root, text = "7", command = lambda: change("7"), bg = "white", relief = "flat")
seven.configure(height = 5, width = 10)
seven.grid(column = 0, row = 3, padx = 2, pady = 2)

eight = HoverButton(root, text = "8", command = lambda: change("8"), bg = "white", relief = "flat")
eight.configure(height = 5, width = 10)
eight.grid(column = 1, row = 3, padx = 2, pady = 2)

nine = HoverButton(root, text = "9", command = lambda: change("9"), bg = "white", relief = "flat")
nine.configure(height = 5, width = 10)
nine.grid(column = 2, row = 3, padx = 2, pady = 2)

four = HoverButton(root, text = "4", command = lambda: change("4"), bg = "white", relief = "flat")
four.configure(height = 5, width = 10)
four.grid(column = 0, row = 4, padx = 2, pady = 2)

five = HoverButton(root, text = "5", command = lambda: change("5"), bg = "white", relief = "flat")
five.configure(height = 5, width = 10)
five.grid(column = 1, row = 4, padx = 2, pady = 2)

six = HoverButton(root, text = "6", command = lambda: change("6"), bg = "white", relief = "flat")
six.configure(height = 5, width = 10)
six.grid(column = 2, row = 4, padx = 2, pady = 2)

one = HoverButton(root, text = "1", command = lambda: change("1"), bg = "white", relief = "flat")
one.configure(height = 5, width = 10)
one.grid(column = 0, row = 5, padx = 2, pady = 2)

two = HoverButton(root, text = "2", command = lambda: change("2"), bg = "white", relief = "flat")
two.configure(height = 5, width = 10)
two.grid(column = 1, row = 5, padx = 2, pady = 2)

three = HoverButton(root, text = "3", command = lambda: change("3"), bg = "white", relief = "flat")
three.configure(height = 5, width = 10)
three.grid(column = 2, row = 5, padx = 2, pady = 2)

dot = HoverButton(root, text = ".", command = lambda: change("."), bg = "white", relief = "flat")
dot.configure(height = 5, width = 10)
dot.grid(column = 0, row = 6, padx = 2, pady = 2)

zero = HoverButton(root, text = "0", command = lambda: change("0"), bg = "white", relief = "flat")
zero.configure(height = 5, width = 10)
zero.grid(column = 1, row = 6, padx = 2, pady = 2)

root.mainloop()

