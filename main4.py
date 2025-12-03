from tkinter import *
root = Tk()
root.title("New account")
root.geometry("300x400")

l1 = Label(text="FULL NAME", bg="#2319DD", fg="white")
l2 = Label(text="EMAIL ID", bg="#2319DD", fg="white")
l3 = Label(text="PASSWORD", bg="#2319DD", fg="white")

name_entry = Entry()
email_entry = Entry()
password_entry = Entry(show="*")

def display():
    name = name_entry.get()
    greet = "Hi", +name+"\n"
    message = "\n congratulations for your new account!"
    textbox.insert(END, greet)
    textbox.insert(END, message)
    
textbox = Text(bg="#637821", fg="black")
btn = Button(text="Create Account", command=display)

l1.pack()
name_entry.pack()
l2.pack()
email_entry.pack()
l3.pack()
password_entry.pack()
btn.pack()
textbox.pack()


root.mainloop()