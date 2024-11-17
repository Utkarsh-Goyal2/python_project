import csv
import os
CSV_FILE = r"C:\Users\mail2\OneDrive\Desktop\users.csv"
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
def Login():
    tries = 1
    name = input("Enter your username")
    with open(CSV_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Name"] == name:
                while tries <= 3:
                    passcode = input("Enter your password:")
                    if row["Password"] == passcode:
                        print("Login Successfull")
                        break
                    else:
                        print(f"Wrong password. You have {3-tries} tries left")
                        tries += 1
            else:
                print("User is not registered")
                return 
        

with open(CSV_FILE, mode='r') as file:
    reader = csv.DictReader(file)
    print("Headers:", reader.fieldnames)
for i in range(5):
    Register()
Login()
#just trying push-pull