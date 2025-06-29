import tkinter as tk
from math import sin, cos, tan, sqrt, log, log10, factorial, radians

def calculate():
    try:
        expr = entry.get()
        result = str(eval_math(expr))
        result_label.config(text="Result: " + result)
    except Exception as e:
        result_label.config(text="Error: " + str(e))

def eval_math(expr):
    # Safe namespace
    safe_dict = {
        'sin': lambda x: sin(radians(x)),
        'cos': lambda x: cos(radians(x)),
        'tan': lambda x: tan(radians(x)),
        'sqrt': sqrt,
        'log': log,
        'log10': log10,
        'factorial': factorial,
        'abs': abs,
        'mod': lambda x, y: x % y,
        '__builtins__': {}
    }
    return eval(expr, {"__builtins__": None}, safe_dict)

# GUI setup
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x250")

entry = tk.Entry(root, width=40, font=('Arial', 14))
entry.pack(pady=15)

calc_button = tk.Button(root, text="Calculate", font=('Arial', 12), command=calculate)
calc_button.pack()

result_label = tk.Label(root, text="Result: ", font=('Arial', 14))
result_label.pack(pady=15)

hint_label = tk.Label(root, text="""
Use like: 
5+3, sqrt(25), sin(30), factorial(5), 
log(2.71), log10(100), mod(10,3)
""", font=('Arial', 10), fg="gray")
hint_label.pack()

root.mainloop()
