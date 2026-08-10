from tkinter import *  # type: ignore
from PIL import ImageTk, Image
from tkinter import messagebox
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# ---------------- LOGIN FUNCTION ----------------

def handle_login():
    email = email_input.get()
    password = password_input.get()

    print(email, password)

    if email == 'abhidha2105@gmail.com' and password == '1234':
        messagebox.showinfo('YaY', 'Login Successful')
    else:
        messagebox.showerror('Error', 'Login Failed')


# ---------------- PASSWORD TOGGLE ----------------

password_visible = False


def toggle_password():
    global password_visible

    if password_visible == False:
        password_input.config(show='')
        password_visible = True
    else:
        password_input.config(show='*')
        password_visible = False


# ---------------- MAIN WINDOW ----------------

root = Tk()

root.title('Login Form')
#root.iconbitmap('Flipkart-Logo.ico')
root.iconbitmap(BASE_DIR / 'Flipkart-Logo.ico')

root.geometry('350x500')

root.configure(background="#0096dc")


# ---------------- FLIPKART IMAGE ----------------

#img = Image.open('Flipkart-Emblem.webp')
img = Image.open(BASE_DIR / 'Flipkart-Emblem.webp')
resized_img = img.resize((150, 70))
img = ImageTk.PhotoImage(resized_img)

img_label = Label(
    root,
    image=img,
    bg='#0096dc'
)

img_label.pack(pady=(10, 10))


# ---------------- FLIPKART TEXT ----------------

text_label = Label(
    root,
    text='Flipkart',
    fg='white',
    bg='#0096dc'
)

text_label.pack()

text_label.config(font=('verdana', 24))


# ---------------- EMAIL ----------------

email_label = Label(
    root,
    text='Enter Email',
    fg='white',
    bg='#0096dc'
)

email_label.pack(pady=(20, 5))

email_label.config(font=('verdana', 12))


email_input = Entry(
    root,
    width=50
)

email_input.pack(
    ipady=6,
    pady=(1, 15)
)


# ---------------- PASSWORD ----------------

password_label = Label(
    root,
    text='Enter Password',
    fg='white',
    bg='#0096dc'
)

password_label.pack(pady=(20, 5))

password_label.config(font=('verdana', 12))


# Frame to keep password box and eye button together
password_frame = Frame(
    root,
    bg='#0096dc'
)

password_frame.pack()


# Password is hidden by default
password_input = Entry(
    password_frame,
    width=43,
    show='*'
)

password_input.pack(
    side='left',
    ipady=6,
    pady=(1, 15)
)


# Eye button
eye_btn = Button(
    password_frame,
    text='👁',
    command=toggle_password
)

eye_btn.pack(
    side='left',
    padx=2
)


# ---------------- LOGIN BUTTON ----------------

login_btn = Button(
    root,
    text='login Here',
    fg='black',
    bg='white',
    width=20,
    height=2,
    command=handle_login
)

login_btn.pack(
    pady=(10, 20)
)

login_btn.config(
    font=('verdana', 10)
)


# ---------------- RUN APPLICATION ----------------

root.mainloop()