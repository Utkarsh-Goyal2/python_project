import customtkinter as ctk
from PIL import Image,ImageTk
from loginregisteration import Login,Register
ctk.set_appearance_mode("dark")
# Set the color theme (default, blue, green, dark-blue)
ctk.set_default_color_theme("blue")

# Create the main application window 
app = ctk.CTk()
app.title("---")
app.geometry("700x600")

#welcome message
image_path="yo.png"
image = ctk.CTkImage(light_image=Image.open(image_path), dark_image=Image.open(image_path),size = (600,200))
label = ctk.CTkLabel(app, text="Welcome to WanderEase!", font=("Berlin Sans FB", 50),bg_color="transparent",image = image,text_color = "white")
label.pack(pady=70)

#input username 
username_frame = ctk.CTkFrame(app)
username_frame.pack(pady=20, anchor="center") 
username_icon = ctk.CTkImage(light_image=Image.open("username.png"), size=(30, 30))
uicon_label = ctk.CTkLabel(username_frame, image=username_icon, text="")
uicon_label.pack(side="left")
username = ctk.CTkEntry(username_frame,width = 300, placeholder_text="Enter your username",font=("Arial", 20))
username.pack(side="left")
#input password
password_frame = ctk.CTkFrame(app)
password_frame.pack(pady = 10, anchor = "center")
password_icon  = ctk.CTkImage(light_image=Image.open("password.png"), size=(30, 30))
picon_label = ctk.CTkLabel(password_frame,image = password_icon, text = "")
picon_label.pack(side = "left")
password = ctk.CTkEntry(password_frame,width = 300, placeholder_text="Enter your password", font = ("Arial", 20),show = "*")
password.pack(pady = 10)
#login / register button
button_frame = ctk.CTkFrame(app)
button_frame.pack(pady = 20, anchor = "center")
login = ctk.CTkButton(button_frame,width = 100,text = "LOGIN", font = ("Arial", 20), command=lambda: Login(username.get(), password.get(),app))
login.pack(side = "left", padx = 20)
registeration_btn = ctk.CTkButton(button_frame,width = 100,text = "SIGNUP",font = ("Arial", 20), command = lambda : Register())
registeration_btn.pack(side = "right", padx = 20)
#running
app.mainloop()