import csv
import customtkinter as ctk
from PIL import Image,ImageTk 
CSV_FILE = "users.csv"
def show_popup(title, message):
    popup = ctk.CTkToplevel()
    popup.title(title)
    popup.geometry("300x150")
    popup.attributes("-topmost", True)
    popup.grab_set()
    label = ctk.CTkLabel(popup, text=message, font=("Arial", 14))
    label.pack(pady=20)
    close_button = ctk.CTkButton(popup, text="Close", command=popup.destroy)
    close_button.pack(pady=10)
    return popup

def checkpassword(password):
    if len(password) < 3 or len(password) > 15:
        show_popup("caution", "Please make the password length between 3 and 15 characters")
        return False
    return True

def checking_new_user(name,password,popup):
    if not name or not password:
        show_popup("Message", "Username and password cannot be empty.")
        return 
    with open(CSV_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Name"] == name:
                show_popup("Username error", "Username already exists")
                return
        else:
            if checkpassword(password):
                with open(CSV_FILE, mode = 'a', newline = "") as file:
                    writer = csv.writer(file)
                    writer.writerow([name,password])
                show_popup("Success", "Registration successful!")
                if popup.winfo_exists():
                        popup.destroy()

    return
def Register():
    registeration = ctk.CTkToplevel()  
    registeration.title("register")  
    registeration.geometry("500x400")
    registeration.attributes("-topmost", True)
    name = ctk.CTkEntry(registeration, placeholder_text="Enter a username", font=("Arial", 20),width = 300)
    name.pack(pady=20)
    passcode = ctk.CTkEntry(registeration, placeholder_text="Enter a password", font=("Arial", 20),show = "*",width = 300)
    passcode.pack(pady = 20)
    close_button = ctk.CTkButton(registeration, text="Start your journey..(almost)", command=lambda: checking_new_user(name.get(),passcode.get(),registeration))
    close_button.pack(pady=10)

def Login(name,password,app):
    from gui import main
    if not name or not password:
        show_popup("Message", "Username and password cannot be empty.")
        return
    with open(CSV_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Name"] == name:
                if row["Password"] == password:
                    app.destroy()
                    main()
                    return
                else:
                    show_popup("password error", "Wrong password")
        
                return
        else:
            show_popup("Registeration error", "User not registered, please signup first")
            return

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
def welcome_ui():
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
    registeration_btn = ctk.CTkButton(button_frame,width = 100,text = "SIGNUP",font = ("Arial", 20), command = lambda : Register())
    registeration_btn.pack(side = "right", padx = 20)
    login = ctk.CTkButton(button_frame,width = 100,text = "LOGIN", font = ("Arial", 20), command=lambda: Login(username.get(), password.get(),app))
    login.pack(side = "left", padx = 20)
    #running
    app.mainloop()
if __name__ == "__main__":
    welcome_ui()

