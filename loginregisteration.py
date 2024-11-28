import csv
import os
import customtkinter as ctk
CSV_FILE = "users.csv"
def initialize_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Password"])

def Register():
    k = True
    class registering:
        def __init__(self):
            nonlocal k
            name = input("Please enter a username: ")
            with open(CSV_FILE, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["Name"] == name:
                        print("Username already exists, try a different one")
                        return
            passcode = input("Please enter a password:")
            with open(CSV_FILE, mode = 'a', newline = "") as file:
                writer = csv.writer(file)
                writer.writerow([name,passcode])
            k = False
            
    while k:
        registering()
    return 
def Login(name,password):
    with open(CSV_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Name"] == name:
                if row["Password"] == password:
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
                    popup = ctk.CTkToplevel()  
                    popup.title("Message")  
                    popup.geometry("300x150") 
                        
                    label = ctk.CTkLabel(popup, text=f"Wrong password", font=("Arial", 14))
                    label.pack(pady=20)
                        
                    # Add a button to close the popup window
                    close_button = ctk.CTkButton(popup, text="Close", command=popup.destroy)
                    close_button.pack(pady=10)
        
                return
        else:
            popup = ctk.CTkToplevel()  
            popup.title("Message") 
            popup.geometry("300x150")  
                        
            label = ctk.CTkLabel(popup, text=f"User not registered", font=("Arial", 14))
            label.pack(pady=20)
        
            close_button = ctk.CTkButton(popup, text="Close", command=popup.destroy)
            close_button.pack(pady=10)
            print("User is not registered, please signup")
            return
        

# for i in range(3):
#     Register()

# #tryingpushpull
