# Import all classes and functions from the tkinter module for GUI creation
from tkinter import *
import math  # Import the math library to use mathematical functions

# Create the main window for the calculator application
win = Tk()
win.title("Calculator")  # Set the title of the window
win.geometry("280x437")  # Set the dimensions of the window
win.resizable(0,0)  # Prevent window resizing

equation = "0"  # Global variable to store the current equation input

# Function to clear the calculator input
def clear_button():
    global equation
    equation = ""  # Reset the equation to an empty string
    input_int.set("0")  # Update the display to show 0

# Function to handle button clicks and update the equation
def click_button(key):
    global equation
    if equation == "0":  # If the equation is 0, replace it with the new input
        equation = ""
    equation = equation + key  # Append the clicked button value to the equation
    input_int.set(equation)  # Update the display with the new equation

# Function to evaluate the current equation and display the result
def equal_to():
    global equation
    result = str(eval(equation))  # Evaluate the equation using eval()
    input_int.set(result)  # Update the display with the result

# Function to calculate and display the square root of the input
def square_root():
    global equation
    result = str(math.sqrt(int(equation)))  # Calculate the square root
    input_int.set(result)  # Update the display with the result

# Function to remove the last character from the equation (backspace)
def backspace():
    global equation
    if equation == "0":  # If equation is already 0, keep it as is
        input_int.set("0")
    else:
        equation = equation[:-1]  # Remove the last character
        input_int.set(equation)  # Update the display

# Function to toggle between positive and negative values
def plus_minus():
    global equation
    equation = str(-1 * int(equation))  # Multiply the equation by -1 to toggle sign
    input_int.set(equation)  # Update the display
        
# IntVar() is a tkinter variable that holds an integer value, used to track the input field
input_int = IntVar()

# Create a frame to hold the display (entry box)
entry_frame = Frame(win, width=278, height=130,highlightbackground="black", highlightthickness=1)
entry_frame.pack(side=TOP)  # Place the frame at the top of the window

# Create the entry box where the numbers and results are displayed
entry = Entry(entry_frame, font=("Times New Roman", 40, "bold"), textvariable=input_int, justify=RIGHT)
entry.pack(ipadx=20,ipady=50) # Place the entry box inside the frame

# Create another frame to hold the buttons
buttons_frame = Frame(win, width=280, height=400)
buttons_frame.pack() # Place the buttons frame below the entry box

# Row 0: Clear, CE (clear entry), and Backspace buttons
clear_entry = Button(buttons_frame, width= 8, height=2, font=("Times New Roman", 10, "bold"), text = "CE", command=lambda : clear_button()).grid(row = 0, column = 0, padx=2, pady=2)
clear = Button(buttons_frame, width= 18, height=2, font=("Times New Roman", 10, "bold"), text = "C", command=lambda: clear_button()).grid(row = 0, column = 1, columnspan=2, padx=2, pady=2)
back_space = Button(buttons_frame, width= 8, height=2, font=("Times New Roman", 10, "bold"), text = "⌫", command=lambda: backspace()).grid(row = 0, column = 3, padx=2, pady=2)

# Row 1: Power, Square, Square root, and Division buttons
x_p_y = Button(buttons_frame, width= 8, height=2, font=("Times New Roman", 10, "bold"), text = "x^y", command=lambda : click_button('**')).grid(row = 1, column = 0, padx=2, pady=2)
x_p_2 = Button(buttons_frame, width= 8, height=2, font=("Times New Roman", 10, "bold"), text = "x²", command=lambda : click_button('**2')).grid(row = 1, column = 1, padx=2, pady=2)
root = Button(buttons_frame, width= 8, height=2, font=("Times New Roman", 10, "bold"), text = "√x", command=lambda : square_root()).grid(row = 1, column = 2, padx=2, pady=2)
divide = Button(buttons_frame, width= 8, height=2, font=("Times New Roman", 10, "bold"), text = "÷", command=lambda : click_button('/')).grid(row = 1, column = 3, padx=2, pady=2)

# Row 2: Number buttons (7, 8, 9) and Multiply button
seven = Button(buttons_frame, width= 8, height=2, font=("Times New Roman", 10, "bold"), text = "7", command=lambda : click_button('7')).grid(row = 2, column = 0, padx=2, pady=2)
eight = Button(buttons_frame, width= 8, height=2, font=("Times New Roman", 10, "bold"), text = "8", command=lambda : click_button('8')).grid(row = 2, column = 1, padx=2, pady=2)
nine = Button(buttons_frame, width= 8, height=2, font=("Times New Roman", 10, "bold"), text = "9", command=lambda : click_button('9')).grid(row = 2, column = 2, padx=2, pady=2)
multiply = Button(buttons_frame, width= 8, height=2, font=("Times New Roman", 10, "bold"), text = "x", command=lambda : click_button('*')).grid(row = 2, column = 3, padx=2, pady=2)

# Row 3: Number buttons (4, 5, 6) and Minus button
four = Button(buttons_frame,  width= 8, height=2, font=("Times New Roman", 10, "bold"), text = "4", command=lambda : click_button('4')).grid(row = 3, column = 0, padx=2, pady=2)
five = Button(buttons_frame, width= 8, height=2, font=("Times New Roman", 10, "bold"), text = "5", command=lambda : click_button('5')).grid(row = 3, column = 1, padx=2, pady=2)
six = Button(buttons_frame, width= 8, height=2, font=("Times New Roman", 10, "bold"), text = "6", command=lambda : click_button('6')).grid(row = 3, column = 2, padx=2, pady=2)
minus = Button(buttons_frame, width= 8, height=2, font=("Times New Roman", 10, "bold"), text = "-", command=lambda : click_button('-')).grid(row = 3, column = 3, padx=2, pady=2)

# Row 4: Number buttons (1, 2, 3) and Plus button
one = Button(buttons_frame, width= 8, height=2, font=("Times New Roman", 10, "bold"), text = "1", command=lambda : click_button('1')).grid(row = 4, column = 0, padx=2, pady=2)
two = Button(buttons_frame, width= 8, height=2, font=("Times New Roman", 10, "bold"), text = "2", command=lambda : click_button('2')).grid(row = 4, column = 1, padx=2, pady=2)
three = Button(buttons_frame, width= 8, height=2, font=("Times New Roman", 10, "bold"), text = "3", command=lambda : click_button('3')).grid(row = 4, column = 2, padx=2, pady=2)
plus = Button(buttons_frame, width= 8, height=2, font=("Times New Roman", 10, "bold"), text = "+", command=lambda : click_button('+')).grid(row = 4, column = 3, padx=2, pady=2)

# Row 5: Plus/Minus, Zero, Decimal point, and Equal buttons
plus_mins = Button(buttons_frame, width= 8, height=2, font=("Times New Roman", 10, "bold"), text = "+/-", command=lambda : plus_minus()).grid(row = 5, column = 0, padx=2, pady=2)
zero = Button(buttons_frame, width= 8, height=2, font=("Times New Roman", 10, "bold"), text = "0", command=lambda : click_button('0')).grid(row = 5, column = 1, padx=2, pady=2)
dot = Button(buttons_frame, width= 8, height=2, font=("Times New Roman", 10, "bold"), text = ".", command=lambda : click_button('.')).grid(row = 5, column = 2, padx=2, pady=2)
eual = Button(buttons_frame, width= 8, height=2, font=("Times New Roman", 10, "bold"), text = "=", command=lambda : equal_to()).grid(row = 5, column = 3, padx=2, pady=2)


win.mainloop()