from tkinter import *
import tkinter as tk
import pyttsx3

root = tk.Tk()
root.geometry("500x500")
root.title("Pindo IDE")

text1= Entry(root,width=50,fg="black",bg="white")
text1.pack(padx=10,pady=20)


def run():
    print(text1.get())

def create_GUI():
    root = tk.Tk()
    root.geometry("200x200")
    root.title("PindoGUI")

    root.mainloop()

def create_entry_in_GUI_source():
    root = tk.Tk()
    root.geometry("400x400")
    root.title("Entry Box Creator")
    label1 = Entry(root,width=50,fg="black",bg="white")
    label1.pack(padx=10,pady=20) 

    root.mainloop()

def speak_Entry():
    pyttsx3.speak(text1.get())

def Calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    sum = num1+num2
    print(sum)

def about():
    root = tk.Tk()
    root.title("About Pindo")
    label1 = Label(root,text="Pindo is a programming language created by AppDev Private Limited, well this is not a company name, if there is any such company this is coincidence.").pack()
    print(label1)

    root.mainloop()

def pindo_help():
    root = tk.Tk()
    root.title("Pindo Help")
    label2 = Label(root,text="Pindo is a simple readymade programming language which is still under development by AppDev").pack()
    print(label2)

    root.mainloop()

menu = Menu(root)
root.config(menu=menu)
submenu=Menu(menu,tearoff=False)
menu.add_cascade(label="Options",menu=submenu)
submenu.add_command(label="About",command=about)
submenu.add_command(label="Help",command=pindo_help)

def show_code_Clac():
    print("This code is using Python\nnum1 = float(input('Enter first number: '))\nnum2 = float(input('Enter seconde number: '))\nprint(sum)")

def feedback():
    root = Tk()
    root.title("Feedback")
    fb = Entry(root,width=50,fg="black",bg="white")
    fb.pack(padx=10,pady=20)
    def submit():
        print(fb.get()+".Thank You For Your Feedback")

    b1 = tk.Button(root,text="Submit",fg="black",bg="lightgrey",command=submit).pack()

    root.mainloop()

def show_code_speak():
    print("This is using python\npyttsx3.speak(text1.get())")

b1 = tk.Button(root,text="Run in console",fg="black",bg="lightgrey",command=run).pack()

b2 = tk.Button(root,text="Run in GUI",fg="black",bg="lightgrey",command=create_GUI).pack()

b3 = tk.Button(root,text="Create Entry box",fg="black",bg="lightgrey",command=create_entry_in_GUI_source).pack()

b4 = tk.Button(root,text="Speak Entry box",fg="black",bg="lightgrey",command=speak_Entry).pack()

b5 = tk.Button(root,text="Calculator",fg="black",bg="lightgrey",command=Calculator).pack()

b5 = tk.Button(root,text="Show Code For Calculator",fg="black",bg="lightgrey",command=show_code_Clac).pack()

b6 = tk.Button(root,text="Show Code For Speak",fg="black",bg="lightgrey",command=show_code_speak).pack()

b7 = tk.Button(root,text="FeedBack",fg="black",bg="lightgrey",command=feedback).pack()

b8 = tk.Button(root,text="Close",fg="black",bg="lightgrey",command=exit).pack()

root.mainloop()
