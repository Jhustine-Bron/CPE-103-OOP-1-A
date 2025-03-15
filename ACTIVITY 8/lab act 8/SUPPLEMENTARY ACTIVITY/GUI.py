import tkinter as tk
import math

def sin():
    try:
        value = float(entry1.get())
        result_value = round(math.sin(math.radians(value)), 4)
        result.set(result_value)
        history_list.insert(tk.END, f"sin({value}) = {result_value}")
    except ValueError:
        result.set("Error! Invalid input.")

def cos():
    try:
        value = float(entry1.get())
        result_value = round(math.cos(math.radians(value)), 4)
        result.set(result_value)
        history_list.insert(tk.END, f"cos({value}) = {result_value}")
    except ValueError:
        result.set("Error! Invalid input.")

def tan():
    try:
        value = float(entry1.get())
        result_value = round(math.tan(math.radians(value)), 4)
        result.set(result_value)
        history_list.insert(tk.END, f"tan({value}) = {result_value}")
    except ValueError:
        result.set("Error! Invalid input.")

def add():
    result_value = round(float(entry1.get()) + float(entry2.get()), 4)
    result.set(result_value)
    history_list.insert(tk.END, f"{entry1.get()} + {entry2.get()} = {result_value}")

def subtract():
    result_value = round(float(entry1.get()) - float(entry2.get()), 4)
    result.set(result_value)
    history_list.insert(tk.END, f"{entry1.get()} - {entry2.get()} = {result_value}")

def multiply():
    result_value = round(float(entry1.get()) * float(entry2.get()), 4)
    result.set(result_value)
    history_list.insert(tk.END, f"{entry1.get()} * {entry2.get()} = {result_value}")

def divide():
    try:
        result_value = round(float(entry1.get()) / float(entry2.get()), 4)
        result.set(result_value)
        history_list.insert(tk.END, f"{entry1.get()} / {entry2.get()} = {result_value}")
    except ZeroDivisionError:
        result.set("Error! Division by zero.")
        history_list.insert(tk.END, "Error! Division by zero.")

def power():
    try:
        base = float(entry1.get())
        exponent = float(entry2.get())
        result_value = round(base**exponent, 4)
        result.set(result_value)
        history_list.insert(tk.END, f"{base}^{exponent} = {result_value}")
    except ValueError:
        result.set("Error! Invalid input.")

def clear():
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    result.set("")

def clear_history():
    history_list.delete(0, tk.END)

def squareroot():
    try:
        value = float(entry1.get())
        result_value = round(value**0.5, 4)
        result.set(result_value)
        history_list.insert(tk.END, f"√{value} = {result_value}")
    except ValueError:
        result.set("Error! Invalid input.")


def validate_input(value_if_allowed):

    if value_if_allowed == "" or value_if_allowed.replace(".", "", 1).isdigit():
        return True
    return False


root = tk.Tk()
root.title("CALCU")
root.geometry("500x360")
root.configure(bg = "#EFFFEA")

result = tk.StringVar()

validate_cmd = root.register(validate_input)


tk.Label(root, text="Enter first number:", font="helvetica", bg = "#EFFFEA").grid(row=0, column=0)
entry1 = tk.Entry(root, validate="key", validatecommand=(validate_cmd, "%P"))
entry1.grid(row=0, column=1)

tk.Label(root, text="Enter second number:", font="helvetica", bg = "#EFFFEA").grid(row=1, column=0)
entry2 = tk.Entry(root, validate="key", validatecommand=(validate_cmd, "%P"))
entry2.grid(row=1, column=1)


tk.Button(root, text="Add", command=add, bg = "#E0FBDA").grid(row=2, column=0, ipadx=20.5)
tk.Button(root, text="Subtract", command=subtract, bg = "#E0FBDA").grid(row=2, column=1, ipadx=9)
tk.Button(root, text="Multiply", command=multiply, bg = "#E0FBDA").grid(row=3, column=0, ipadx=9.5)
tk.Button(root, text="Divide", command=divide, bg = "#E0FBDA").grid(row=3, column=1, ipadx=14)
tk.Button(root, text="Square Root", command=squareroot, bg = "#E0FBDA").grid(row=4, column=0, ipadx=0)
tk.Button(root, text="Power", command=power, bg = "#E0FBDA").grid(row=4, column=1, ipadx=15)
tk.Button(root, text="Sin", command=sin, bg = "#E0FBDA").grid(row=5, column=0, ipadx=22)
tk.Button(root, text="Cos", command=cos, bg = "#E0FBDA").grid(row=5, column=1, ipadx=20.5)
tk.Button(root, text="Tan", command=tan, bg = "#E0FBDA").grid(row=6, column=0, ipadx=20)


tk.Button(root, text="Clear", command=clear, bg = "#FBE0DA").grid(row=6, column=1, ipadx=19)
tk.Button(root, text="Clear History", command=clear_history, bg = "#FBE0DA").grid(row=7, column=0, columnspan=2, pady=5)


tk.Label(root, text="RESULT:", font="helvetica", bg = "#EFFFEA").grid(row=8, column=0, pady=10)
tk.Label(root, textvariable=result, bg="White", font="helvetica").grid(row=8, column=1, ipadx=40)


tk.Label(root, text="History:", font="helvetica", bg = "#EFFFEA").grid(row=0, column=2)
history_list = tk.Listbox(root, height=15, width=30)
history_list.grid(row=1, column=2, rowspan=7, padx=10, pady=5)

tk.Label(root, text="Note: Square roots, powers, or trigonometric functions only apply to the first number",
         bg="#EFFFEA").grid(row=11, column=0, columnspan=3, pady=10, sticky="s")

root.mainloop()
