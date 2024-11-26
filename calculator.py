import tkinter as tk
from tkinter import messagebox
# Function to update expression in the text entry box
def click(button_text):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + button_text)
# Function to evaluate the final expression
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")
        entry.delete(0, tk.END)
    except Exception:
        messagebox.showerror("Error", "Invalid input")
        entry.delete(0, tk.END)
# Function to clear the input field
def clear():
    entry.delete(0, tk.END)
# Setting up the main window
window = tk.Tk()
window.title("Colorful Calculator")
window.geometry("400x500")
window.configure(bg="#222831")  # Dark background for the window
# Entry widget for input/output display
entry = tk.Entry(window, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4, bg="#393E46", fg="white")
entry.grid(row=0, column=0, columnspan=4, pady=20)
# Button style customization
button_config = {
    'font': ('Arial', 16),
    'width': 5,
    'height': 2,
    'bd': 1,
    'relief': 'raised'
}
# Button colors
button_colors = {
    'numbers': '#00ADB5',
    'operations': '#FF5722',
    'equals': '#00C851',
    'clear': '#FF4444'
}
# Creating buttons with colors
buttons = [
    ('7', 1, 0, button_colors['numbers']), ('8', 1, 1, button_colors['numbers']), ('9', 1, 2, button_colors['numbers']), ('/', 1, 3, button_colors['operations']),
    ('4', 2, 0, button_colors['numbers']), ('5', 2, 1, button_colors['numbers']), ('6', 2, 2, button_colors['numbers']), ('*', 2, 3, button_colors['operations']),
    ('1', 3, 0, button_colors['numbers']), ('2', 3, 1, button_colors['numbers']), ('3', 3, 2, button_colors['numbers']), ('-', 3, 3, button_colors['operations']),
    ('0', 4, 0, button_colors['numbers']), ('C', 4, 1, button_colors['clear']), ('=', 4, 2, button_colors['equals']), ('+', 4, 3, button_colors['operations']),
]
# Adding buttons to the grid with colors and commands
for (text, row, col, color) in buttons:
    if text == '=':
        tk.Button(window, text=text, bg=color, fg="white", command=calculate, **button_config).grid(row=row, column=col, sticky="nsew")
    elif text == 'C':
        tk.Button(window, text=text, bg=color, fg="white", command=clear, **button_config).grid(row=row, column=col, sticky="nsew")
    else:
        tk.Button(window, text=text, bg=color, fg="white", command=lambda txt=text: click(txt), **button_config).grid(row=row, column=col, sticky="nsew")
# Adjust row and column weights to make the layout responsive
for i in range(5):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)
# Main loop
window.mainloop()
