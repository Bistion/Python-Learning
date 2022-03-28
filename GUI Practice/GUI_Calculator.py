# Here is a basic calculator that is made by using the tkinter module

# This imports everything from the tkinter module
from cmath import exp
from tkinter import *
from turtle import width

# Globally declaration of the expression variable
expression = ""

# Function created to update expression in a text entry box
def press(num):
    global expression

    # Concatenation of a string
    expression = expression + str(num)

    # Updating expression using the set method
    equation.set(expression)

# Function created to evaluate the final expression
def equalpress():

    # Trying to equate for errors that might be seen
    try:

        global expression
        # eval function to evaluate the expression
        # and str function convert the result
        # into string
        total = str(eval(expression))

        equation.set(total)

        # initialize expression variable by an
        # empty string
        expression = ""

    # Error handling
    except:

        equation.set(" error ")
        expression = ""

# Function to clear the contents of text box
def clear():
    global expression
    expression = ""
    equation.set("")

# Driver code
if __name__ == "__main__":
    # create a GUI window
    gui = Tk()

    # Set background color
    gui.configure(background="black")

    # Set GUI title
    gui.title("Calculator Plus")

    # Set GUI window size
    gui.geometry("435x300")

    # StringVar() is the variable class we
    # create an instance of this class
    equation = StringVar()

    # Text entry box creation
    expression_field = Entry(gui, textvariable=equation)

    # Placing grid matrix
    expression_field.grid(columnspan=4, ipadx=150)

    # Creating various buttons and putting in place
    button1 = Button(gui, text=' 1 ', fg='black', bg='red',
                    command=lambda: press(1), height=3, width=14)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text=' 2 ', fg='black', bg='red',
                    command=lambda: press(2), height=3, width=14)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', fg='black', bg='red',
                    command=lambda: press(3), height=3, width=14)
    button3.grid(row=2, column=2)

    button4 = Button(gui, text=' 4 ', fg='black', bg='red',
                    command=lambda: press(4), height=3, width=14)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', fg='black', bg='red',
                    command=lambda: press(5), height=3, width=14)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', fg='black', bg='red',
                    command=lambda: press(6), height=3, width=14)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ', fg='black', bg='red',
                    command=lambda: press(7), height=3, width=14)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ', fg='black', bg='red',
                    command=lambda: press(8), height=3, width=14)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', fg='black', bg='red',
                    command=lambda: press(9), height=3, width=14)
    button9.grid(row=4, column=2)

    button0 = Button(gui, text=' 0 ', fg='black', bg='red',
                    command=lambda: press(0), height=3, width=14)
    button0.grid(row=5, column=0)

    plus = Button(gui, text=' + ', fg='black', bg='red',
                    command=lambda: press("+"), height=3, width=14)
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg='black', bg='red',
                    command=lambda: press("-"), height=3, width=14)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', fg='black', bg='red',
                    command=lambda: press("*"), height=3, width=14)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', fg='black', bg='red',
                    command=lambda: press("/"), height=3, width=14)
    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ', fg='black', bg='red',
                    command=equalpress, height=3, width=14)
    equal.grid(row=5, column=2)

    clear = Button(gui, text='Clear', fg='black', bg='red',
                    command=clear, height=3, width=14)
    clear.grid(row=5, column=1)

    Decimal = Button(gui, text=' . ', fg='black', bg='red',
                    command=lambda: press("."), height=3, width=14)
    Decimal.grid(row=6, column=0)

    # Start the GUI
    gui.mainloop()