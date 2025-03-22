import tkinter as tk
from tkinter import ttk, messagebox

window = tk.Tk()
window.title("Birth Date Selector")
window.geometry("400x250")
window.configure(bg="#D1F1C7")


ttk.Label(window, text="Choose your Birth Date", font=("Times New Roman", 15), background="#D1F1C7").pack(pady=5)


selection_mode = tk.StringVar(value="combo")
day_var, month_var, year_var = tk.StringVar(), tk.StringVar(), tk.StringVar()
manual_entry = tk.StringVar()


frame_selection = tk.Frame(window, bg="#D1F1C7")
frame_selection.pack(pady=5)


ttk.Label(frame_selection, text="Select your Birth Day: ", background="#D1F1C7").grid(row=0, column=0, sticky="w")
ttk.Label(frame_selection, text="Select your Birth Month: ", background="#D1F1C7").grid(row=1, column=0, sticky="w")
ttk.Label(frame_selection, text="Select your Birth Year: ", background="#D1F1C7").grid(row=2, column=0, sticky="w")


day_combo = ttk.Combobox(frame_selection, width=5, textvariable=day_var, values=[str(i) for i in range(1, 32)])
month_combo = ttk.Combobox(frame_selection, width=10, textvariable=month_var, values=['January', 'February', 'March', 'April',
                                                                                     'May', 'June', 'July', 'August', 'September',
                                                                                     'October', 'November', 'December'])
year_combo = ttk.Combobox(frame_selection, width=6, textvariable=year_var, values=[str(i) for i in range(1980, 2025)])

day_combo.grid(row=0, column=1, padx=5, pady=2)
month_combo.grid(row=1, column=1, padx=5, pady=2)
year_combo.grid(row=2, column=1, padx=5, pady=2)


manual_entry_field = ttk.Entry(window, textvariable=manual_entry, width=30)


def toggle_input():
    if selection_mode.get() == "combo":

        manual_entry_field.pack_forget()
        frame_selection.pack()

        manual_entry.set("")
    else:

        frame_selection.pack_forget()
        manual_entry.set(f"{day_var.get()} {month_var.get()} {year_var.get()}")  # Pre-fill manual entry
        manual_entry_field.pack()

radio_frame = tk.Frame(window, bg="#D1F1C7")
tk.Radiobutton(radio_frame, text="Use ComboBox", variable=selection_mode, value="combo", bg="#D1F1C7", command=toggle_input).pack(side="left")
tk.Radiobutton(radio_frame, text="Enter Manually", variable=selection_mode, value="manual", bg="#D1F1C7", command=toggle_input).pack(side="left")
radio_frame.pack(pady=5)


def show_birthdate():
    birthdate = manual_entry.get() if selection_mode.get() == "manual" else f"{day_var.get()} {month_var.get()} {year_var.get()}"
    messagebox.showinfo("Your Birth Date", f"You selected: {birthdate}")


ttk.Button(window, text="Show Birth Date", command=show_birthdate).pack(pady=10)

window.mainloop()
