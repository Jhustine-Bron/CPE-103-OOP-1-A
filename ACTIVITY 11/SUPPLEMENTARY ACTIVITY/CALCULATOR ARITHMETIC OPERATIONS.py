import tkinter as tk
import math

def seven(event = 0):
    entry.insert(tk.END, "7")
def eight(event = 0):
    entry.insert(tk.END, "8")
def nine(event = 0):
    entry.insert(tk.END, "9")
def four(event = 0):
    entry.insert(tk.END, "4")
def five(event = 0):
    entry.insert(tk.END, "5")
def six(event = 0):
    entry.insert(tk.END, "6")
def one(event = 0):
    entry.insert(tk.END, "1")
def two(event = 0):
    entry.insert(tk.END, "2")
def three(event = 0):
    entry.insert(tk.END, "3")
def zero(event = 0):
    entry.insert(tk.END, "0")
def decimal(event = 0):
    entry.insert(tk.END, ".")
def addition(event = 0):
    entry.insert(tk.END, "+")
def subtraction(event = 0):
    entry.insert(tk.END, "-")
def multiply(event = 0):
    entry.insert(tk.END, "*")
def division(event = 0):
    entry.insert(tk.END, "/")
def parent1(event = 0):
    entry.insert(tk.END, "(")
def parent2(event = 0):
    entry.insert(tk.END, ")")
def delete(event = 0):
    current_text = entry.get()
    if len(current_text) > 0:
        entry.delete(len(current_text) -1,tk.END)
def clear(event = 0):
    entry.delete(0, tk.END)
def equal(event = 0):
    result = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, str(result))
def sin_function():
    result = math.sin(math.radians(float(entry.get())))
    entry.delete(0, tk.END)
    entry.insert(0, str(result))
def cos_function():
    result = math.cos(math.radians(float(entry.get())))
    entry.delete(0, tk.END)
    entry.insert(0, str(result))
def tan_function():
    result = math.tan(math.radians(float(entry.get())))
    entry.delete(0, tk.END)
    entry.insert(0, str(result))
def exponent(event = 0):
    entry.insert(tk.END, "**")

root = tk.Tk()
root.title("CALCULATOR USING GRID METHOD")
root.resizable(False, False)

entry = tk.Entry(root, font=("Consolas", 30), borderwidth=5,  justify="right", bg="white")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

button_add = tk.Button(root, text="+", font=("Consolas", 16), bg="#d9d9d9", command=addition)
button_add.grid(row=2, column=0, sticky="nsew")
sin_button = tk.Button(root, text="sin", font=("Consolas", 16), bg="#d9d9d9",width=5, height=2, command=sin_function)
sin_button.grid(row=1, column=0, sticky="nsew")
cos_button = tk.Button(root, text="cos", font=("Consolas", 16), bg="#d9d9d9",width=5, height=2, command=cos_function)
cos_button.grid(row=1, column=1, sticky="nsew")
tan_button = tk.Button(root, text="tan", font=("Consolas", 16), bg="#d9d9d9",width=5, height=2, command=tan_function)
tan_button.grid(row=1, column=2, sticky="nsew")
exp_button = tk.Button(root, text="x^", font=("Consolas", 16), bg="#d9d9d9",width=5, height=2, command=exponent)
exp_button.grid(row=1, column=3, sticky="nsew")

button_7 = tk.Button(root, text="7", font=("Consolas", 16), bg="#e6e6e6",width=5, height=2, command=seven)
button_7.grid(row=3, column=0, sticky="nsew")
button_8 = tk.Button(root, text="8", font=("Consolas", 16), bg="#e6e6e6",width=5, height=2, command=eight)
button_8.grid(row=3, column=1, sticky="nsew")
button_9 = tk.Button(root, text="9", font=("Consolas", 16), bg="#e6e6e6",width=5, height=2, command=nine)
button_9.grid(row=3, column=2, sticky="nsew")
parent = tk.Button(root, text="(", font=("Consolas", 16), bg="#e6e6e6",width=5, height=2, command=parent1)
parent.grid(row=3, column=3, sticky="nsew")

button_div = tk.Button(root, text="/", font=("Consolas", 16), bg="#d9d9d9",width=5, height=2, command=division)
button_div.grid(row=2, column=1, sticky="nsew")
button_4 = tk.Button(root, text="4", font=("Consolas", 16), bg="#e6e6e6",width=5, height=2, command=four)
button_4.grid(row=4, column=0, sticky="nsew")
button_5 = tk.Button(root, text="5", font=("Consolas", 16), bg="#e6e6e6",width=5, height=2, command=five)
button_5.grid(row=4, column=1, sticky="nsew")
button_6 = tk.Button(root, text="6", font=("Consolas", 16), bg="#e6e6e6",width=5, height=2, command=six)
button_6.grid(row=4, column=2, sticky="nsew")
parents = tk.Button(root, text=")", font=("Consolas", 16), bg="#e6e6e6",width=5, height=2, command=parent2)
parents.grid(row=4, column=3, sticky="nsew")

button_mul = tk.Button(root, text="*", font=("Consolas", 16), bg="#d9d9d9",width=5, height=2, command=multiply)
button_mul.grid(row=2, column=2, sticky="nsew")
button_1 = tk.Button(root, text="1", font=("Consolas", 16), bg="#e6e6e6",width=5, height=2, command=one)
button_1.grid(row=5, column=0, sticky="nsew")
button_2 = tk.Button(root, text="2", font=("Consolas", 16), bg="#e6e6e6",width=5, height=2, command=two)
button_2.grid(row=5, column=1, sticky="nsew")
button_3 = tk.Button(root, text="3", font=("Consolas", 16), bg="#e6e6e6",width=5, height=2, command=three)
button_3.grid(row=5, column=2, sticky="nsew")

dell = tk.Button(root, text="del", font=("Consolas", 16), bg="#e6e6e6",width=5, height=2, command=delete)
dell.grid(row=5, column=3, sticky="nsew")
button_sub = tk.Button(root, text="-", font=("Consolas", 16), bg="#d9d9d9",width=5, height=2, command=subtraction)
button_sub.grid(row=2, column=3, sticky="nsew")
button_0 = tk.Button(root, text="0", font=("Consolas", 16), bg="#e6e6e6",width=5, height=2, command=zero)
button_0.grid(row=6, column=0, sticky="nsew")
button_dot = tk.Button(root, text=".", font=("Consolas", 16), bg="#e6e6e6",width=5, height=2, command=decimal)
button_dot.grid(row=6, column=1, sticky="nsew")
clear_button = tk.Button(root, text="C", font=("Consolas", 16), bg="#ff9e7b",width=5, height=2, fg="black",  command=clear)
clear_button.grid(row=6, column=2, sticky="nsew")
equal_button = tk.Button(root, text="=", font=("Consolas", 16), bg="#b0e694",width=5, height=2, fg="black", command=equal)
equal_button.grid(row=6, column=3, sticky="nsew")

root.bind("1", one)
root.bind("2", two)
root.bind("3", three)
root.bind("4", four)
root.bind("5", five)
root.bind("6", six)
root.bind("7", seven)
root.bind("8", eight)
root.bind("9", nine)
root.bind("0", zero)
root.bind("+", addition)
root.bind("-", subtraction)
root.bind("*", multiply)
root.bind("/", division)
root.bind("<BackSpace>", delete)
root.bind("<Return>", equal)
root.bind("<Delete>", clear)
root.bind(")", parent1)
root.bind("(", parent2)
root.bind(".", decimal)
root.bind("^", exponent)

root.mainloop()
