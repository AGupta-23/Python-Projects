from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

def handle_login():
    email = email_input.get()
    password = password_input.get()
    print(email, password)

    if email == 'abhidha2105@gmail.com' and password == '1234':
        messagebox.showinfo('YaY', 'Login Successful')
    else:
        messagebox.showerror('Error', "Login Failed")


root = Tk()

root.title('Login Form')
root.iconbitmap('Flipkart-Logo.webp')

# root.minsize(400,400)
# root.maxsize(600,600)

root.geometry('350x500')

root.configure(background = "#0096dc")

#use of pil now

img = Image.open('Flipkart-Emblem.webp')
resized_img = img.resize((150,70))
img = ImageTk.PhotoImage(resized_img)

img_label = Label(root, image = img, bg = '#0096dc')

# geometry manager - decides where every elemnt will sit - 2 types pack and grid
img_label.pack(pady = (10,10))

text_label = Label(root, text = 'Flipkart', fg = 'white', bg = '#0096dc')
text_label.pack()
text_label.config(font = ('verdana', 24))

email_label = Label(root, text = 'Enter Email' , fg = 'white', bg = '#0096dc')
email_label.pack(pady = (20,5))
email_label.config(font = ('verdana', 12))

email_input = Entry(root, width = 50)
email_input.pack(ipady = 6, pady = (1,15))

password_label = Label(root, text = 'Enter Password' , fg = 'white', bg = '#0096dc')
password_label.pack(pady = (20,5))
password_label.config(font = ('verdana', 12))

password_input = Entry(root, width = 50)
password_input.pack(ipady = 6, pady = (1,15))

login_btn = Button(root, text = "login Here", fg = 'black', bg = 'white', width = 20, height = 2 , command = handle_login)
login_btn.pack(pady = (10,20))
login_btn.config(font = ('verdana', 10))
root.mainloop()