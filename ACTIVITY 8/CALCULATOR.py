from tkinter import *

class MyWindow:
    def __init__(self, win):
        self.lbl1 = Label(win, text='CALCULATOR', font = "Helvetica", bg="#D7F8CE")
        self.lbl1.place(x=275, y=15)
        self.t1 = Entry(bd=5)
        self.t1.place(x=200, y=50, width=260)

        self.lbl1=Label(win, text='First number:', bg="#D7F8CE")
        self.lbl1.place(x=100, y=50)
        self.t1 = Entry(bd=5)
        self.t1.place(x=200, y=50, width = 260)

        self.lbl2=Label(win, text='Second number:', bg="#D7F8CE")
        self.t2 = Entry(bd=5)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100, width = 260)

        self.lbl3=Label(win, text='Result:', bg="#D7F8CE")
        self.t3 = Entry(bd=5)
        self.lbl3.place(x=100, y=150)
        self.t3.place(x=200, y=150, width = 260)

        self.btn1 = Button(win, text='Addition', command= self.add, fg = 'Black', bg = "#AAEB99", font = "Helvetica" )
        self.btn1.place(x=100, y=200)

        self.btn2 = Button(win, text='Subtract', fg = 'black', bg = "#AAEB99", font = "Helvetica")
        self.btn2.bind('<Button-1>', self.sub)
        self.btn2.place(x=200, y=200)

        self.btn3 = Button(win, text='Multiply', fg='black', bg="#AAEB99", font="Helvetica")
        self.btn3.bind('<Button-1>', self.multiply)
        self.btn3.place(x=300, y=200)

        self.btn4 = Button(win, text='Divide', fg='black', bg="#AAEB99", font="Helvetica")
        self.btn4.bind('<Button-1>', self.Divide)
        self.btn4.place(x=400, y=200)

        self.btn4 = Button(win, text='Clear', fg='black', bg="#AAEB99", font="Helvetica")
        self.btn4.bind('<Button-1>', self.Clear)
        self.btn4.place(x=250, y=250)

    def add(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 + num2
        self.t3.insert(END, str(result))

    def sub(self, event):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 - num2
        self.t3.insert(END, str(result))

    def multiply(self, event):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 * num2
        self.t3.insert(END, str(result))

    def Divide(self, event):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 / num2
        self.t3.insert(END, str(result))

    def Clear(self, event):
        self.t1.delete(0, 'end')
        self.t2.delete(0, 'end')
        self.t3.delete(0, 'end')

window = Tk()
mywin = MyWindow(window)
window.title('Hello Python')
window.geometry("500x300+10+10")
window.configure(bg="#D7F8CE")
window.mainloop()


