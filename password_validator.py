from tkinter import *
import bcrypt
root = Tk()
root.geometry("300x300")

password_entry = Entry(root)
password_entry.pack()

def validates(password):
    hash =b'$2b$12$F7D3hxafeQlLllF8UjSOZeVJA4Zi5rd7wbp9Q1R9sqTX7C0vzJmCC'
    password = bytes(password,encoding='utf-8')
    if bcrypt.checkpw(password,hash):   
        print('Login successful')
    else:
        print('Invalid password')

button = Button(text="validate",command=lambda: validates(password_entry.get()))   #lambda function ensures that whatever the value is being entered in the function gets acce[ted and executed after the user enters in the input and not after the program is run]
button.pack()

root.mainloop()