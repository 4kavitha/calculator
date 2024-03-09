import tkinter as tk
import math

calculator = ""

def add_to_calculator(symbol):
    global calculator
    calculator += str(symbol)
    text_res.delete("1.0", "end")
    text_res.insert("1.0", calculator)

def evaluate_calculator():
    global calculator
    try:
        calculator = str(eval(calculator.replace("^", "**")))
        text_res.delete("1.0", "end")
        text_res.insert("1.0", calculator)
    except ZeroDivisionError:
        clear_field()
        text_res.insert("1.0", "Error: Division by zero")
    except Exception as e:
        clear_field()
        text_res.insert("1.0", "Error: " + str(e))

def clear_field():
    global calculator
    calculator = ""
    text_res.delete("1.0", "end")

def calculate_square_root():
    global calculator
    try:
        calculator = str(math.sqrt(eval(calculator)))
        text_res.delete("1.0", "end")
        text_res.insert("1.0", calculator)
    except Exception as e:
        clear_field()
        text_res.insert("1.0", "Error: " + str(e))

box = tk.Tk()
box.geometry("400x375")

text_res = tk.Text(box, height=3, width=18, font=("Arial", 28))
text_res.grid(columnspan=6)

buttons = [
    ("1", 2, 1, 1, lambda: add_to_calculator(1)),
    ("2", 2, 2, 1, lambda: add_to_calculator(2)),
    ("3", 2, 3, 1, lambda: add_to_calculator(3)),
    ("4", 3, 1, 1, lambda: add_to_calculator(4)),
    ("5", 3, 2, 1, lambda: add_to_calculator(5)),
    ("6", 3, 3, 1, lambda: add_to_calculator(6)),
    ("7", 4, 1, 1, lambda: add_to_calculator(7)),
    ("8", 4, 2, 1, lambda: add_to_calculator(8)),
    ("9", 4, 3, 1, lambda: add_to_calculator(9)),
    ("0", 5, 2, 1, lambda: add_to_calculator(0)),
    ("+", 2, 4, 1, lambda: add_to_calculator("+")),
    ("*", 4, 4, 1, lambda: add_to_calculator("*")),
    ("-", 3, 4, 1, lambda: add_to_calculator("-")),
    (".", 5, 3, 1, lambda: add_to_calculator(".")),
    ("^", 5, 1, 1, lambda: add_to_calculator("^")),
    ("/", 5, 4, 1, lambda: add_to_calculator("/")),
    ("C", 6, 1, 2, clear_field),
    ("=", 6, 3, 2, evaluate_calculator)
    
]

for button in buttons:
    text, row, col, col_span, command = button
    btn = tk.Button(box, text=text, command=lambda cmd=command: cmd(), width=5, font=("Arial", 18))
    btn.grid(row=row, column=col, columnspan=col_span)

box.mainloop()
