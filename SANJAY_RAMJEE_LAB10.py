#importing the necessary modules
from tkinter import Tk, Text, Entry, END

#Note to grader: My input for the screenshot is a < b < e < 8 < CAPSLOCK < B < Z

#defining a function that handles the keybinds
def record(event):
    #setting each keybind to a variable each time a key is pressed, so I can easily retrive the value
    key = event.keysym
    #this block will check whether the key is a letter
    if key.isalpha():
        #if this is indeed a letter, it will check whether it's lowercase first
        if key.islower():
            tbox.insert(END, 'It is a lowercase letter.\n')
        #if it's not lowercase, it checks whether it's an uppercase
        elif key.isupper():
            tbox.insert(END, 'It is an uppercase letter.\n')
    #this block will now check if it's a digit
    elif key.isdigit():
        tbox.insert(END, 'It is a number.\n')
    #although I coulld just write it as an else statement, since it won't trigger the previous if and elifs, this is more specific
    elif len(event.keysym) > 1:
        tbox.insert(END, 'It is a non-alphanumeric key\n')
#creating the Tk application object
root = Tk()
#Entry Widget at the top 
entry = Entry(master = root)
entry.pack()
#Text box widget right blow, with specified dimensions
tbox = Text(master= root, width = 70, height = 20)
tbox.pack()

#Binding the text pressed in the Entry widget
entry.bind('<KeyPress>', record)

#main loop that creates the application
root.mainloop()

