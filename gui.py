import customtkinter as ctk
from PIL import Image,ImageTk
from backend import TravelManager
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
def main():
    def logout():
        main_window.destroy() 
        from loginregisteration import welcome_ui 
        welcome_ui() 
    def check_input(first, second):
        if not first or not second:
            popup = ctk.CTkToplevel()
            popup.geometry("300x150")
            popup.attributes("-topmost", True)
            popup.grab_set()
            label = ctk.CTkLabel(popup, text="Entry cant be empty", font=("Arial", 14))
            label.pack(pady=20)
            close_button = ctk.CTkButton(popup, text="Close", command=popup.destroy)
            close_button.pack(pady=10)
            return False
        return True
            
    def searching_flight(start,dest):
        if check_input(start,dest):
            results=TravelManager.search_flight_packages(start,dest)
            resultframe(flights,results)
    def searching_car(start, dest):
        if check_input(start,dest):
            TravelManager.search_car_packages(start,dest)
    def searching_hotel(rating, dest):
        if check_input(dest, "lmo"):
            if not rating:
                rating = 0
            TravelManager.search_hotel_packages(rating,dest)
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

    class resultframe(ctk.CTkScrollableFrame):
        frames = []
        def __init__(self,parent,results):
            self.parent = parent
            self.results = results
            super().__init__(parent)
            self.grid(row = 4, column = 0, sticky = "nsew",pady = 10)
            if self not in resultframe.frames:
                resultframe.frames.append(self)
            for i, thing in enumerate(results):
                formatted_results = f"From: {thing[1]}\nTo: {thing[2]}\nAirline: {thing[3]}\nDeparture Time: {thing[4]}\nArrival Time: {thing[5]}\nPrice: ₹{thing[6]}\nAvailability: {thing[7]}\nSeats Left = {thing[8]} "
                label = ctk.CTkLabel(self, text=f"{formatted_results}", anchor="w", font=("Arial", 20),text_color="white",justify = "left")
                label.grid(row=2*i, column=0, padx=10, pady=5, sticky="w")
                separator = ctk.CTkLabel(self, text="", fg_color="gray", height=1, width=500)
                separator.grid(row=2*i+1, column=0, sticky="ew", padx=10, pady=(0, 10))
            parent.grid_rowconfigure(4, weight=1)
            parent.grid_columnconfigure(0, weight=1)

    #leftframe (will containt stuff like history and cart and stuff)
    leftframe = ctk.CTkFrame(main_window, width=900, fg_color="#FFF4D2")
    leftframe.grid(row=0, column=0, rowspan=2, sticky="ns",padx = 5) 
    home_btn = ctk.CTkButton(leftframe,text = "HOME", command = lambda: welcomepage.showframe())
    home_btn.pack()
    flights_btn = ctk.CTkButton(leftframe, text="Flights", command=lambda: flights.showframe())
    flights_btn.pack()

    car_rentals_btn = ctk.CTkButton(leftframe, text="Car Rentals", command=lambda: car_rentals.showframe())
    car_rentals_btn.pack() 

    hotel_booking_btn = ctk.CTkButton(leftframe, text="Hotel Booking", command=lambda: hotel_booking.showframe())
    hotel_booking_btn.pack()

    #logout button and logo 
    topframe = ctk.CTkFrame(main_window, fg_color="#CCFFCC", height=150)
    logout_btn = ctk.CTkButton(topframe,width=100,text="LOGOUT",font=("Arial", 14),fg_color = "#FF5C5C",command= lambda: logout())
    logout_btn.pack(side = "right")
    logo_label = ctk.CTkLabel(topframe,text = "WanderEase", font = ("Times new roman", 20,"bold"),text_color = "#333333")
    logo_label.pack(side = "left",padx = 20,pady = 10)
    topframe.grid(row=0, column=1, sticky="ew")
    #welcome page
    welcomepage = centerframe()
    def welcome_page(frame):
        image_path = "welcome.png"
        image = ctk.CTkImage(light_image=Image.open(image_path), dark_image=Image.open(image_path), size=(800, 400))
        welcome_label = ctk.CTkLabel(frame, text="",image = image, font=("Arial", 30))
        frame.grid_rowconfigure(0, weight=0)  
        frame.grid_rowconfigure(1, weight=0)  
        frame.grid_rowconfigure(2, weight=0)  
        frame.grid_rowconfigure(3, weight=0)  
        frame.grid_columnconfigure(0, weight=1)  
        frame.grid_columnconfigure(1, weight=1)  

        welcome_label.grid(row=0, column=0, columnspan=2, pady=15, sticky="nsew")

        
        message = ctk.CTkLabel(frame, text="What will be your next journey?", font=("Arial", 30), text_color="#333333")
        message.grid(row=1, column=0, columnspan=2, pady=5, sticky="nsew")

        
        flights_btn = ctk.CTkButton(frame, text="Flights", command=lambda: flights.showframe(),font = ("arial", 30), width=150, height=80,fg_color = "#3CB6A8")
        flights_btn.grid(row=2, column=0, padx=20, pady=5, sticky="nsew")

        car_rentals_btn = ctk.CTkButton(frame, text="Car Rentals", command=lambda: car_rentals.showframe(),font = ("arial", 30), width=150, height=80, fg_color = "#FF7F50")
        car_rentals_btn.grid(row=2, column=1, padx=20, pady=5, sticky="nsew")


        hotel_booking_btn = ctk.CTkButton(frame, text="Hotel Booking", command=lambda: hotel_booking.showframe(),font = ("arial", 30), width=150, height=80, fg_color = "#4CAF50")
        hotel_booking_btn.grid(row=3, column=1, padx=20, pady=10, sticky="nsew")

        return frame


    welcomepage= welcome_page(welcomepage)
    flights = centerframe()
    def flight_page(frame):
        frame.grid_rowconfigure(0, weight=0)  # Space above the widgets
        frame.grid_rowconfigure(1, weight=0)  # For the first entry
        frame.grid_rowconfigure(2, weight=0)  # For the second entry  # For the button
        frame.grid_rowconfigure(4, weight=1)  # Space below the widgets
        frame.grid_columnconfigure(0, weight=1)  
        
        destination = ctk.CTkEntry(frame, placeholder_text="Enter your destination", font=("Arial", 20), width=300)
        destination.grid(row=0, column=0, padx=10, pady=10, sticky="")  # Place at row 0, column 0

        starting_point = ctk.CTkEntry(frame, placeholder_text="Enter your starting point", font=("Arial", 20), width=300)
        starting_point.grid(row=1, column=0, padx=10, pady=10, sticky="")  # Place at row 1, column 0

        search = ctk.CTkButton(frame,width = 300, text="SEARCH", font=("Arial", 20), command=lambda: searching_flight(starting_point.get(), destination.get()))
        search.grid(row=2, column=0, padx=10, pady=20, sticky="")  # Place at row 2, column 0

        return frame
    flights = flight_page(flights)
    hotel_booking = centerframe()
    def hotel_booking_page(frame):
        destination = ctk.CTkEntry(frame, placeholder_text="Enter the city", font = ("Arial",20),width = 300)
        destination.pack()
        rating = ctk.CTkEntry(frame,placeholder_text="Enter minimum price", font = ("Arial", 20), width = 300)
        rating.pack()
        search = ctk.CTkButton(frame, text = "SEARCH", font= ("Arial", 20), command = lambda: searching_hotel(rating.get(),destination.get()))
        search.pack()
        return frame
    hotel_booking=hotel_booking_page(hotel_booking)
    car_rentals = centerframe()
    def car_rental_page(frame):
        destination = ctk.CTkEntry(frame, placeholder_text="Enter the city", font= ("Arial", 20), width = 300)
        destination.pack()
        no_of_seats= ctk.CTkEntry(frame, placeholder_text="Enter no. of seats", font = ("Arial", 20), width = 300)
        no_of_seats.pack()
        search = ctk.CTkButton(frame, text = "SEARCH", font= ("Arial", 20), command = lambda: searching_car(no_of_seats.get(),destination.get()))
        search.pack()
        return frame    
    car_rentals = car_rental_page(car_rentals)
    welcomepage.showframe()
    main_window.mainloop()
main()
