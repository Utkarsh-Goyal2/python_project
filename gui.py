import customtkinter as ctk
from PIL import Image,ImageTk
from loginregisteration import Login,Register
ctk.set_appearance_mode("dark")
# Set the color theme (default, blue, green, dark-blue)
ctk.set_default_color_theme("blue")

# Create the main application window 
app = ctk.CTk()
app.title("---")
app.geometry("800x700")

#welcome message
image_path=r"C:\Users\mail2\OneDrive\Desktop\yo.png"
image = ctk.CTkImage(light_image=Image.open(image_path), dark_image=Image.open(image_path),size = (600,200))
label = ctk.CTkLabel(app, text="Welcome to WanderEase!", font=("Berlin Sans FB", 50),bg_color="transparent",image = image,text_color = "white")
label.pack(pady=70)

#input username and password
username = ctk.CTkEntry(app,width = 300, placeholder_text="Enter your username",font=("Arial", 20))
username.pack(pady=10)
password = ctk.CTkEntry(app,width = 300, placeholder_text="Enter your password", font = ("Arial", 20))
password.pack(pady = 10)
#login / register button
login = ctk.CTkButton(app,width = 100,text = "LOGIN", font = ("Arial", 20), command=lambda: Login(username.get(), password.get()))
login.pack(pady = 20)
# Run the application
app.mainloop()