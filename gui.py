import tkinter as tk
from tkinter import Tk, Label, PhotoImage
from PIL import Image, ImageTk

welcome = tk.Tk()
#welcome message 
welcome_message = tk.Label(welcome, text = "Welcome!", font=("Arial", 30, "bold" ))
welcome_message.place(x = 650, y = 100)
#login button 
login_button = tk.Button(welcome, text = "Login", font = ("Times new Roman", 20 ))
#registeration button 
register_button = tk.Button(welcome, text = "Register", font = ("Times new Roman", 20 ))
#placing buttons
login_button.place(x = 650, y = 200)
register_button.place(x = 650, y = 300)
#image
image = Image.open(r"C:\Users\mail2\OneDrive\Desktop\trial.png")  

resized_image = image.resize((300, 200), Image.Resampling.LANCZOS)  
tk_image = ImageTk.PhotoImage(resized_image)

# placing image
label = Label(welcome, image=tk_image)
label.place(x = 650, y = 400)

welcome.mainloop()

