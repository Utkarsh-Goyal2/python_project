import customtkinter as ctk
from PIL import Image,ImageTk
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
def main():
    def logout():
        main_window.destroy() 
        from loginregisteration import welcome_ui 
        welcome_ui() 
    main_window = ctk.CTk()
    screen_width = main_window.winfo_screenwidth()
    screen_height = main_window.winfo_screenheight()
    main_window.geometry(f"{screen_width}x{screen_height}+0+0")
    main_window.title("Main Application")
    main_window.grid_rowconfigure(1, weight=1)
    main_window.grid_columnconfigure(1, weight=1)
    class centerframe(ctk.CTkFrame):
        parent = main_window
        frames = []
        def __init__(self):
            super().__init__(centerframe.parent, fg_color="#F3F8F1")
            self.grid(row=1, column=1, sticky="nsew",pady= 5)
            if self not in centerframe.frames:
                centerframe.frames.append(self)
        def showframe(self):
            for f in centerframe.frames:
                f.grid_forget()
            self.grid(row=1, column=1, sticky="nsew",pady= 5)  

    #leftframe (will containt stuff like history and cart and shit idk)
    leftframe = ctk.CTkFrame(main_window, width=300, fg_color="#FFF4D2")
    leftframe.grid(row=0, column=0, rowspan=2, sticky="ns",padx = 5) 
    home_btn = ctk.CTkButton(leftframe,text = "home", command = lambda: welcomepage.showframe())
    home_btn.pack()
    ooga_booga_btn = ctk.CTkButton(leftframe,text = "ooga_booga", command = lambda: ooga_booga.showframe())
    ooga_booga_btn.pack()
        #logout button and logo 
    topframe = ctk.CTkFrame(main_window, fg_color="#FFC2D1", height=150)
    logout_btn = ctk.CTkButton(topframe,width=100,text="LOGOUT",font=("Arial", 14),fg_color = "#FF5C5C",command= lambda: logout())
    logout_btn.pack(side = "right")
    logo_label = ctk.CTkLabel(topframe,text = "WanderEase", font = ("Times new roman", 20,"bold"),text_color = "#333333")
    logo_label.pack(side = "left",padx = 20,pady = 10)
    topframe.grid(row=0, column=1, sticky="ew")

    welcomepage = centerframe()
    message = ctk.CTkLabel(welcomepage, text = "What do you want to explore today?", font = ("Arial",30),text_color="#333333")
    message.pack()
    ooga_booga = centerframe()
    checking = ctk.CTkLabel(ooga_booga,text ="oogabooga",font = ("Arial", 30),text_color="#333333")
    checking.pack()
    welcomepage.showframe()
    main_window.mainloop()
main()