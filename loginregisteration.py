import csv
import customtkinter as ctk
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

def Login(name,password,window):
    if not name or not password:
        show_popup("Message", "Username and password cannot be empty.")
        return
    with open(CSV_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Name"] == name:
                if row["Password"] == password:
                    if window.winfo_exists():
                        window.destroy()
                    popup = ctk.CTkToplevel() 
                    popup.title("Message")  
                    popup.geometry("300x150")  
                        
                    label = ctk.CTkLabel(popup, text="login succesfull", font=("Arial", 14))
                    label.pack(pady=20)
                        
                    # close_button = ctk.CTkButton(popup, text="Close", command=popup.destroy)
                    # close_button.pack(pady=10)
                    # print("Login Successfull")
                    return
                else:
                    show_popup("password error", "Wrong password")
        
                return
        else:
            show_popup("Registeration error", "User not registered, please signup first")
            return
        

