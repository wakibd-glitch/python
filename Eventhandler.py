from tkinter import *

window = Tk()
window.title("Event Handler")
window.geometry("100x100")

def handle_click(event):
    print("\n The button was clicked!")

def handle_keypress(event):
    print(event.char)

button = Button(text = "Click Me!")
button.pack()

button.bind("<Button-1>", handle_click)
window.bind("<Key>", handle_keypress)

window.mainloop()