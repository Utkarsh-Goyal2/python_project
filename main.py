def Register():
    users = []
    k = True
    class registering:
        def __init__(self):
            name = input("Please enter a username: ")
            for i in users:
                if name in i:
                    print("Username already exists, try a different one")
                    return 
            passcode = input("Please enter a password:")
            self.username = name
            self.password = passcode
            users.append([name,passcode])
            global k
            k = False
            
    while k:
        user = registering()
Register()
      

