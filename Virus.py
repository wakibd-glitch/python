from tkinter import *
from tkinter import messagebox

messagewindow = Tk()
messagewindow.geometry("200x200")
def messagefunction():
    messagebox.showwarning("Alert", "Stop! Virus Found.")

buttonWidget = Button(messagewindow, text="Scan for Virus", command = messagefunction)
buttonWidget.place(x=40, y=80)

messagewindow.mainloop()