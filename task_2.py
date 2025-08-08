import tkinter as tk

# Function to update expression
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to evaluate expression
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except ZeroDivisionError:
        equation.set("Error: /0")
        expression = ""
    except:
        equation.set("Error")
        expression = ""

# Function to clear the screen
def clear():
    global expression
    expression = ""
    equation.set("")

# Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")
root.resizable(False, False)
root.config(bg="#2C3E50")

expression = ""
equation = tk.StringVar()

# Entry box
entry_frame = tk.Frame(root, bg="#2C3E50")
entry_frame.pack(pady=20)

expression_field = tk.Entry(entry_frame, textvariable=equation, font=('Arial', 24), 
                            width=15, borderwidth=2, relief="ridge", justify='right')
expression_field.grid(row=0, column=0)
equation.set("")

# Button style
btn_style = {
    "font": ('Arial', 18),
    "bd": 1,
    "relief": "ridge",
    "width": 5,
    "height": 2,
    "bg": "#34495E",
    "fg": "white",
    "activebackground": "#16A085",
    "activeforeground": "white"
}

# Buttons layout
btns_frame = tk.Frame(root, bg="#2C3E50")
btns_frame.pack()

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

for (text, row, col) in buttons:
    if text == "=":
        action = lambda: equalpress()
    else:
        action = lambda x=text: press(x)
    tk.Button(btns_frame, text=text, command=action, **btn_style).grid(row=row, column=col, padx=5, pady=5)

# Clear button
tk.Button(root, text="Clear", command=clear, font=('Arial', 18),
          width=20, height=1, bg="#E74C3C", fg="white",
          activebackground="#C0392B").pack(pady=10)

root.mainloop()
