import customtkinter as ctk
from PIL import Image, ImageTk
from backend import TravelManager

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# Global booking list
bookings = []


def book_item(thing):
    """Book an item and store it in the global bookings list."""
    bookings.append(thing)
    popup = ctk.CTkToplevel()
    popup.geometry("300x150")
    popup.attributes("-topmost", True)
    popup.grab_set()
    label = ctk.CTkLabel(popup, text="Booking Successful!", font=("Arial", 14))
    label.pack(pady=20)
    close_button = ctk.CTkButton(popup, text="Close", command=popup.destroy)
    close_button.pack(pady=10)


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
            label = ctk.CTkLabel(popup, text="Entry can't be empty", font=("Arial", 14))
            label.pack(pady=20)
            close_button = ctk.CTkButton(popup, text="Close", command=popup.destroy)
            close_button.pack(pady=10)
            return False
        return True

    def searching_flight(start, dest):
        if check_input(start, dest):
            results = TravelManager.search_flight_packages(start, dest)
            resultframe(flights, results)

    def searching_car(start, dest):
        if check_input(start, dest):
            TravelManager.search_car_packages(start, dest)

    def searching_hotel(rating, dest):
        if check_input(dest, "lmo"):
            if not rating:
                rating = 0
            TravelManager.search_hotel_packages(rating, dest)

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
            self.grid(row=1, column=1, sticky="nsew", pady=5)
            if self not in centerframe.frames:
                centerframe.frames.append(self)

        def showframe(self):
            for f in centerframe.frames:
                f.grid_forget()
            self.grid(row=1, column=1, sticky="nsew", pady=5)

    class resultframe(ctk.CTkScrollableFrame):
        frames = []

        def __init__(self, parent, results):
            self.parent = parent
            self.results = results
            super().__init__(parent)
            self.grid(row=4, column=0, sticky="nsew", pady=10)
            if self not in resultframe.frames:
                resultframe.frames.append(self)
            for i, thing in enumerate(results):
                formatted_results = (
                    f"From: {thing[1]}\nTo: {thing[2]}\nAirline: {thing[3]}\n"
                    f"Departure Time: {thing[4]}\nArrival Time: {thing[5]}\n"
                    f"Price: ₹{thing[6]}\nAvailability: {thing[7]}\nSeats Left = {thing[8]}"
                )
                label = ctk.CTkLabel(self, text=f"{formatted_results}", anchor="w", font=("Arial", 20), text_color="white", justify="left")
                label.grid(row=2 * i, column=0, padx=10, pady=5, sticky="w")

                book_button = ctk.CTkButton(self, text="Book", command=lambda t=thing: book_item(t))
                book_button.grid(row=2 * i, column=1, padx=10, pady=5, sticky="e")

                separator = ctk.CTkLabel(self, text="", fg_color="gray", height=1, width=500)
                separator.grid(row=2 * i + 1, column=0, sticky="ew", padx=10, pady=(0, 10))
            parent.grid_rowconfigure(4, weight=1)
            parent.grid_columnconfigure(0, weight=1)

    def booking_history_page(frame):
        """Creates the booking history page."""
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        label = ctk.CTkLabel(frame, text="Booking History", font=("Arial", 30))
        label.pack(pady=20)

        if not bookings:
            empty_label = ctk.CTkLabel(frame, text="No bookings yet!", font=("Arial", 20))
            empty_label.pack(pady=10)
        else:
            for booking in bookings:
                formatted_booking = (
                    f"From: {booking[1]}\nTo: {booking[2]}\nAirline: {booking[3]}\n"
                    f"Departure Time: {booking[4]}\nArrival Time: {booking[5]}\n"
                    f"Price: ₹{booking[6]}"
                )
                label = ctk.CTkLabel(frame, text=f"{formatted_booking}", font=("Arial", 20), text_color="white", justify="left")
                label.pack(pady=10)

        return frame

    # Sidebar (leftframe)
    leftframe = ctk.CTkFrame(main_window, width=900, fg_color="#FFF4D2")
    leftframe.grid(row=0, column=0, rowspan=2, sticky="ns", padx=5)

    home_btn = ctk.CTkButton(leftframe, text="HOME", command=lambda: welcomepage.showframe())
    home_btn.pack()
    flights_btn = ctk.CTkButton(leftframe, text="Flights", command=lambda: flights.showframe())
    flights_btn.pack()
    car_rentals_btn = ctk.CTkButton(leftframe, text="Car Rentals", command=lambda: car_rentals.showframe())
    car_rentals_btn.pack()
    hotel_booking_btn = ctk.CTkButton(leftframe, text="Hotel Booking", command=lambda: hotel_booking.showframe())
    hotel_booking_btn.pack()
    booking_history_btn = ctk.CTkButton(leftframe, text="Booking History", command=lambda: booking_history.showframe())
    booking_history_btn.pack()

    # Centerframe pages
    welcomepage = centerframe()
    flights = centerframe()
    hotel_booking = centerframe()
    car_rentals = centerframe()
    booking_history = centerframe()

    # Pages (flight_page, hotel_booking_page, etc.)
    def flight_page(frame):
        ...
    flights = flight_page(flights)

    def hotel_booking_page(frame):
        ...
    hotel_booking = hotel_booking_page(hotel_booking)

    def car_rental_page(frame):
        ...
    car_rentals = car_rental_page(car_rentals)

    booking_history = booking_history_page(booking_history)

    welcomepage.showframe()
    main_window.mainloop()


main()

