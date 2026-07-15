from tkinter import *

root = Tk()
root.title("Tk Window")
root.geometry("1600x900")

frame = Frame(master=root, height=200, width=360, bg="#d0efff")

labelfullname = Label(text = "Full Name", bg = "#3895D3", fg ="white", width = 12)
labelemail = Label(text = "Email", bg = "#3895D3", fg ="white", width = 12)
labelpassword = Label(text = "Password", bg = "#3895D3", fg ="white", width = 12)

name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame, show="⬛")






def display():
    name = name_entry.get()
    greet = "Hey " + name

    message = "\n Congratulations for your new account!"
   
    textbox.insert(END,greet)
    textbox.insert(END,message)

textbox = Text(height=3, width=100)
btn = Button(text= "Create Account", command=display,bg="red")


frame.place(x=20, y=0)
labelfullname.place(x=20, y=20)
name_entry.place(x=150, y=20)
labelemail.place(x=20, y=80)
email_entry.place(x=150, y=80)
labelpassword.place(x=20, y=140)
pass_entry.place(x=150, y=140)
btn.place(x=130, y=210)
textbox.place(y=250)

root.mainloop()