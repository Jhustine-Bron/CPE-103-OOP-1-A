import tkinter as tk

def seven():
    entry.insert(tk.END, "7")
def eight():
    entry.insert(tk.END, "8")
def nine():
    entry.insert(tk.END, "9")
def four():
    entry.insert(tk.END, "4")
def five():
    entry.insert(tk.END, "5")
def six():
    entry.insert(tk.END, "6")
def one():
    entry.insert(tk.END, "1")
def two():
    entry.insert(tk.END, "2")
def three():
    entry.insert(tk.END, "3")
def zero():
    entry.insert(tk.END, "0")
def decimal():
    entry.insert(tk.END, ".")
def addition():
    entry.insert(tk.END, "+")
def subtraction():
    entry.insert(tk.END, "-")
def multiply():
    entry.insert(tk.END, "*")
def division():
    entry.insert(tk.END, "/")
def clear():
    entry.delete(0, tk.END)
def equal():
    result = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, str(result))

root = tk.Tk()
root.title("CALCULATOR USING GRID METHOD")

entry = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right", bg="white")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")
clear_button = tk.Button(root, text="CLEAR", font=("Arial", 16), bg="#ff9e7b", fg="black", height=2, command=clear).grid(row=1, column=0, columnspan=4, sticky="nsew")
button_7 = tk.Button(root, text="7", font=("Arial", 16), bg="#e6e6e6", width=5, height=2, command=seven).grid(row=2, column=0,  sticky="nsew")
button_8 = tk.Button(root, text="8", font=("Arial", 16), bg="#e6e6e6", width=5, height=2, command=eight).grid(row=2, column=1, sticky="nsew")
button_9 = tk.Button(root, text="9", font=("Arial", 16), bg="#e6e6e6", width=5, height=2, command=nine).grid(row=2, column=2,sticky="nsew")
button_div = tk.Button(root, text="/", font=("Arial", 16), bg="#d9d9d9", width=5, height=2, command=division).grid(row=2, column=3,sticky="nsew")
button_4 = tk.Button(root, text="4", font=("Arial", 16), bg="#e6e6e6", width=5, height=2, command=four).grid(row=3, column=0, sticky="nsew")
button_5 = tk.Button(root, text="5", font=("Arial", 16), bg="#e6e6e6", width=5, height=2, command=five).grid(row=3, column=1, sticky="nsew")
button_6 = tk.Button(root, text="6", font=("Arial", 16), bg="#e6e6e6", width=5, height=2, command=six).grid(row=3, column=2,  sticky="nsew")
button_mul = tk.Button(root, text="*", font=("Arial", 16), bg="#d9d9d9", width=5, height=2, command=multiply).grid(row=3, column=3,  sticky="nsew")
button_1 = tk.Button(root, text="1", font=("Arial", 16), bg="#e6e6e6", width=5, height=2, command=one).grid(row=4, column=0,  sticky="nsew")
button_2 = tk.Button(root, text="2", font=("Arial", 16), bg="#e6e6e6", width=5, height=2, command=two).grid(row=4, column=1, sticky="nsew")
button_3 = tk.Button(root, text="3", font=("Arial", 16), bg="#e6e6e6", width=5, height=2, command=three).grid(row=4, column=2,  sticky="nsew")
button_sub = tk.Button(root, text="-", font=("Arial", 16), bg="#d9d9d9", width=5, height=2, command=subtraction).grid(row=4, column=3,  sticky="nsew")
button_0 = tk.Button(root, text="0", font=("Arial", 16), bg="#e6e6e6", width=5, height=2, command=zero).grid(row=5, column=0, sticky="nsew")
button_dot = tk.Button(root, text=".", font=("Arial", 16), bg="#e6e6e6", width=5, height=2, command=decimal).grid(row=5, column=1,  sticky="nsew")
button_add = tk.Button(root, text="+", font=("Arial", 16), bg="#d9d9d9", width=5, height=2, command=addition).grid(row=5, column=2,  sticky="nsew")
equal_button = tk.Button(root, text="=", font=("Arial", 16), bg="#b0e694", fg="black", height=2, command=equal).grid(row=5, column=3, sticky="nsew")

root.mainloop()
