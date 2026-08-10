# Tkinter Login Form

A small GUI login form built with **Python, Tkinter, and Pillow**.

## 🎯 Project Goal

Build a basic login GUI while learning:
- Tkinter GUI basics
- Widgets and layout
- User input
- Button callbacks
- Password show/hide logic
- Image handling with Pillow
- File paths using `pathlib`

---

## 🛠️ Libraries Used

| Library | Purpose |
|---|---|
| `tkinter` | Build the GUI |
| `Pillow (PIL)` | Load, resize and display images |
| `pathlib` | Handle file paths |
| `messagebox` | Show success/error popups |

---

## 🧩 Main Tkinter Widgets

| Widget | Purpose |
|---|---|
| `Tk()` | Creates the main application window |
| `Label()` | Displays text or images |
| `Entry()` | Takes user input |
| `Button()` | Creates clickable buttons |
| `Frame()` | Groups related widgets together |

---

## 📐 Important Tkinter Concepts

| Concept | What it does |
|---|---|
| `.pack()` | Places widgets in the window |
| `pady` / `padx` | Adds space outside a widget |
| `ipady` / `ipadx` | Adds space inside a widget |
| `side='left'` | Places widgets beside each other |
| `.config()` | Changes a widget's properties |
| `.get()` | Gets the value entered in an `Entry` |
| `command=` | Calls a function when a button is clicked |
| `mainloop()` | Keeps the GUI running and waits for events |

---

## 🔐 Password Show / Hide

### Main idea

Password is hidden by default:

`show='*'` → displays `****`

To show it:

`show=''` → displays the actual password

The project uses a Boolean state:

| `password_visible` | Meaning |
|---|---|
| `False` | Password hidden |
| `True` | Password visible |

### Toggle logic

**Click 👁:**

`False → show='' → True`

**Click 👁 again:**

`True → show='*' → False`

### Important function

| Function | Purpose |
|---|---|
| `toggle_password()` | Switches password between hidden and visible |

---

## 🔑 Login Logic

| Function | Purpose |
|---|---|
| `handle_login()` | Gets email/password, checks credentials and displays result |

Important methods:

| Code / Method | Purpose |
|---|---|
| `email_input.get()` | Gets entered email |
| `password_input.get()` | Gets entered password |
| `messagebox.showinfo()` | Shows successful login |
| `messagebox.showerror()` | Shows failed login |

### Login flow

`User Input → .get() → Check credentials → Success/Error message`

---

## 🖼️ Pillow / Image Handling

| Function | Purpose |
|---|---|
| `Image.open()` | Opens an image |
| `.resize()` | Changes image dimensions |
| `ImageTk.PhotoImage()` | Converts the image so Tkinter can display it |

### Basic flow

`Image → Image.open() → resize() → PhotoImage() → Label`

---

## 📁 File Paths

```text
BASE_DIR = Path(__file__).resolve().parent
```

### What each part means

| Part | Meaning |
|---|---|
| `__file__` | Current Python file |
| `Path()` | Creates a path object |
| `.resolve()` | Gets the absolute path |
| `.parent` | Gets the folder containing the Python file |
| `BASE_DIR` | Stores that folder path |

Used like:

`BASE_DIR / 'Flipkart-Emblem.webp'`

### Why?

Allows image/icon files to be found based on the Python file's location instead of depending on the terminal's current directory.

---

## 🧠 Python Concepts Practiced

- Functions
- Variables
- Boolean state
- `if / else`
- `and` operator
- Global variables
- Imports/modules
- Method calls
- User input
- Event-driven programming
- File paths

---

## ⭐ Key Learnings

1. **Widgets** are the building blocks of a Tkinter GUI.
2. **`pack()`** controls widget placement.
3. **`command=`** connects buttons to functions.
4. **`.get()`** retrieves user input.
5. **`.config()`** changes widget properties.
6. **`show='*'`** hides password characters.
7. **Boolean state** can control show/hide behavior.
8. **`Frame`** helps group widgets such as the password box + eye button.
9. **Pillow** makes image loading/resizing easier.
10. **`pathlib`** makes file paths reliable when running the project from different directories.
11. **`mainloop()`** keeps the GUI active and handles user events.

---

## 📌 Project Type

**Python GUI / Tkinter Mini Project**

Main focus: **Learning GUI development and event-driven programming in Python.**
