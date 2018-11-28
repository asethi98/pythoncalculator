from tkinter import *
from tkinter import messagebox
import math
calc = Tk()

#Set canvas size and import background image
C = Canvas(calc, bg="blue", height=600, width=600)
filename = PhotoImage(file = "C:\\Users\\sethi\\Desktop\\Fall 2018\\Python 2302\\FinalProject\\backgroundgradient.png")
background_label = Label(calc, image=filename)
background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

calc.title("Calculator")
expression = "" 
result = ""
inputText = StringVar()

#Create text entry field for calculator
txtDisplay = Entry(calc, font = ('Slabo 27px', 20), textvariable = inputText, bd = 1, insertwidth = 30,
                   bg = "grey", fg = "white", justify = 'right').grid(columnspan = 8, sticky=N+S+E+W)

#Set default value in the calculator to 0
inputText.set(0)

#Create textbox to store the result of previous operations
textbox = Text(calc, height=20, width=45)
scroll = Scrollbar(calc, command=textbox.yview)
textbox.configure(yscrollcommand=scroll.set)
textbox.tag_configure('big', font=('Shink', 18, 'bold'))
textbox.tag_configure('color', foreground='grey', font=('Slabo 27px', 14, 'bold'))
textbox.insert(END,'Your Calculations:\n', 'big')

textbox.grid(row = 10, column = 10);
scroll.grid(row = 10, column = 20);



#Add operand to 'expression' string.
def buttonClick(operand):
    try:
        global expression 
        expression = expression + str(operand) #Convert operand to a string and add it to the 'expression' string
        inputText.set(expression) #Set the input text in the text entry field to the 'expression' string
    except:
        #Show error message in the message box.
        messagebox.showinfo("ERROR", "Invalid Input", icon="warning", parent=calc)

#Clear the expression entered in the text entry field
def buttonClear(): 
    global expression
    expression = ""
    inputText.set("")

#Perform calculation when = is pressed
def buttonEquals(): 
    global expression
    global result
    try:
        #Parse the expression to int and evaluate. Then, convert result to string and store in 'evaluated'.
        evaluated = str(eval(expression))
        output = "You entered: " + expression + " = " + evaluated + "\n"
        textbox.insert(END, output, 'color')
        inputText.set(evaluated)
        expression = evaluated
        result = evaluated
        
    except:
        messagebox.showinfo("ERROR", "Invalid Input", icon="warning", parent=calc)


#Erase last digit
def backspace():
    global inputText
    global expression
    
    expression = expression[:-1] # Remove last digit
    if expression: # If there is at least one digit, set input text for text entry field to updated 'expression' string without last digit
       inputText.set(expression)
    else: # If there are no more digits to remove, display 0 in the text entry field. 
       inputText.set(0)

#Perform cos function using math module
def cos():
    global expression
    global result
    cosine = str(math.cos(float(expression)))
    inputText.set(cosine)
    output = "You entered: cos(" + expression + ") = " + cosine + "\n"
    expression = cosine
    textbox.insert(END, output, 'color')
    result = cosine
    
#Perform sin function using math module
def sin():
    global expression
    global result
    sine = str(math.sin(float(expression)))
    inputText.set(sine)
    output = "You entered: sin(" + expression + ") = " + sine + "\n"
    expression = sine
    textbox.insert(END, output, 'color')
    result = sine #store value in result for 'A' button
    
#Perform sqrt function using math module
def sqrt():
    global expression
    global result
    sqrtV = str(math.sqrt(float(expression)))
    inputText.set(sqrtV)
    output = "You entered: sqrt(" + expression + ") = " + sqrtV + "\n"
    expression = sqrtV
    textbox.insert(END, output, 'color')
    result = sqrtV

#Perform squared function using math module
def squared():
    global expression
    global result
    square = str(math.pow(float(expression), 2))
    inputText.set(square)
    output = "You entered: (" + expression + ")² = " + square + "\n"
    expression = square
    textbox.insert(END, output, 'color')
    result = square

#ROW 1 BUTTONS

button7 = Button(calc, padx = "19px", pady = "12px", bd = 0, bg = "#A2ECDD", fg = "black", font = ('Slabo 27px', 16, ''),
                 text = "7", command = lambda:buttonClick(7))
button7.grid(row = 1, column = 0, sticky=N+S+E+W)

button8 = Button(calc, bd = 0, bg = "#A2ECDD", fg = "black", font = ('Slabo 27px', 16, ''),
                 text = "8", command = lambda:buttonClick(8))
button8.grid(row = 1, column = 1, sticky=N+S+E+W)

button9 = Button(calc, padx = "19px", pady = "12px", bd = 0, bg = "#A2ECDD", fg = "black", font = ('Slabo 27px', 16, ''),
                 text = "9", command = lambda:buttonClick(9))
button9.grid(row = 1, column = 2, sticky=N+S+E+W)

mulButton = Button(calc, padx = "19px", pady = "12px", bd = 0, bg = "#A2ECDD", fg = "black", font = ('Slabo 27px', 16, ''),
                 text = "*", command = lambda:buttonClick("*"))
mulButton.grid(row = 1, column = 3, sticky=N+S+E+W)

openParenthesisButton = Button(calc, bd = 0, bg = "grey", fg = "white", font = ('Slabo 27px', 16, ''),
                 text = "(", command = lambda:buttonClick("("))
openParenthesisButton.grid(row = 1, column = 4, sticky=N+S+E+W)


#ROW 2 BUTTONS

button4 = Button(calc, bd = 0, fg = "black", bg = "#A2ECDD", font = ('Slabo 27px', 16, ''),
                 text = "4", command = lambda:buttonClick(4))
button4.grid(row = 2, column = 0, sticky=N+S+E+W)

button5 = Button(calc, bd = 0, bg = "#A2ECDD", fg = "black", font = ('Slabo 27px', 16, ''),
                 text = "5", command = lambda:buttonClick(5))
button5.grid(row = 2, column = 1, sticky=N+S+E+W)

button6 = Button(calc, bd = 0, bg = "#A2ECDD", fg = "black", font = ('Slabo 27px', 16, ''),
                 text = "6", command = lambda:buttonClick(6))
button6.grid(row = 2, column = 2, sticky=N+S+E+W)

subButton = Button(calc, bd = 0, bg = "#A2ECDD", fg = "black", font = ('Slabo 27px', 16, 'bold'),
                 text = "-", command = lambda:buttonClick("-"))
subButton.grid(row = 2, column = 3, sticky=N+S+E+W)

closeParenthesisButton = Button(calc, bd = 0, bg = "grey", fg = "white", font = ('Slabo 27px', 16, ''),
                 text = ")", command = lambda:buttonClick(")"))
closeParenthesisButton.grid(row = 2, column = 4, sticky=N+S+E+W)


#ROW 3 BUTTONS

button1 = Button(calc, bd = 0, bg = "#A2ECDD", fg = "black", font = ('Slabo 27px', 16, ''),
                 text = "1", command = lambda:buttonClick(1))
button1.grid(row = 3, column = 0, sticky=W+E+N+S)

button2 = Button(calc, bd = 0, bg = "#A2ECDD", fg = "black", font = ('Slabo 27px', 16, ''),
                 text = "2", command = lambda:buttonClick(2))
button2.grid(row = 3, column = 1, sticky=W+E+N+S)

button3 = Button(calc, bd = 0, bg = "#A2ECDD", fg = "black", font = ('Slabo 27px', 16, ''),
                 text = "3", command = lambda:buttonClick(3))
button3.grid(row = 3, column = 2, sticky=W+E+N+S)

addButton = Button(calc, bd = 0, bg = "#A2ECDD", fg = "black", font = ('Slabo 27px', 16, ''),
                 text = "+", command = lambda:buttonClick("+"))
addButton.grid(row = 3, column = 3, sticky=W+E+N+S)

cosButton = Button(calc, bd = 0, bg = "grey", fg = "white", font = ('Shink', 16, ''),
                 text = "cos", command = cos)
cosButton.grid(row = 3, column = 4, sticky=N+S+E+W)


#ROW 4 BUTTONS

button0 = Button(calc, padx = "19px", pady = "12px", bd = 0, bg = "#A2ECDD", fg = "black", font = ('Slabo 27px', 16, ''),
                 text = "0", command = lambda:buttonClick(0))
button0.grid(row = 4, column = 0)

clearButton = Button(calc, padx = "19px", pady = "12px", bd = 0, bg = "#A2ECDD", fg = "black", font = ('Slabo 27px', 16, ''),
                 text = "C", command = buttonClear)
clearButton.grid(row = 4, column = 1)

backButton = Button(calc, bd = 0, bg = "#A2ECDD", fg = "black", font = ('Slabo 27px', 16, ''),
                 text = "⌫", command = backspace)
backButton.grid(row = 4, column = 2, sticky=W+E+N+S)

divButton = Button(calc, bd = 0, bg = "#A2ECDD", fg = "black", font = ('Slabo 27px', 16, ''),
                 text = chr(247), command = lambda:buttonClick("/"))
divButton.grid(row = 4, column = 3, sticky=W+E+N+S)

sinButton = Button(calc, bd = 0, bg = "grey", fg = "white", font = ('Shink', 16, ''),
                 text = "sin", command = sin)
sinButton.grid(row = 4, column = 4, sticky=N+S+E+W)


#ROW 5 BUTTONS

decimalButton = Button(calc, bd = 0, bg = "#A2ECDD", fg = "black", font = ('Slabo 27px', 16, ''),
                 text = ".", command = lambda:buttonClick("."))
decimalButton.grid(row = 5, column = 0, sticky=W+E+N+S)

resultButton = Button(calc, bd = 0, bg = "#A2ECDD", fg = "black", font = ('Slabo 27px', 16, ''),
                 text = "A", command = lambda:buttonClick(result))
resultButton.grid(row = 5, column = 1, sticky=N+S+E+W)

sqrtButton = Button(calc, bd = 0, bg = "#A2ECDD", fg = "black", font = ('Shink', 16, ''),
                 text = "√", command = sqrt)
sqrtButton.grid(row = 5, column = 2, sticky=N+S+E+W)

squaredButton = Button(calc, bd = 0, bg = "#A2ECDD", fg = "black", font = ('Slabo 27px', 16, ''),
                 text = "x²", command = squared)
squaredButton.grid(row = 5, column = 3, sticky=N+S+E+W)

equalsButton = Button(calc, bd = 0, bg = "grey", fg = "white", font = ('Slabo 27px', 16, 'bold'),
                 text = "=", command = buttonEquals)
equalsButton.grid(row = 5, column = 4, sticky=N+S+E+W)

C.pack()

calc.mainloop()
