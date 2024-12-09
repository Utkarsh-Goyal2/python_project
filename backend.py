"""
Update bookings is problem
Printing bookings in table order
Add booking time in transactions
Exception handling
"""
import csv
import os
from datetime import datetime, timedelta
from tabulate import tabulate

class TravelPackage:
    def __init__(self,package_id,destination,duration,price,availability_status):
        self.package_id = package_id
        self.destination = destination
        self.duration = duration
        self.price = price
        self.availability_status = availability_status
    '''def details(self):
        d = {"Package ID": self.package_id,"Destination": self.destination,"Duration": self.duration,"Price": self.price,"Availability": self.availability_status}
        return d'''
    
class Flight(TravelPackage):
    
    def __init__(self,package_id,destination,duration,price,availability_status,airline,departure_time,start):
        super().__init__(package_id,destination,duration,price,availability_status)
        self.package_id = package_id
        self.destination = destination
        self.duration = duration
        self.price = price
        self.availability_status = availability_status
        self.airline = airline
        self.departure_time = departure_time
        self.start = start
        time_obj = datetime.strptime(self.departure_time, "%H:%M:%S")
        flight_duration = timedelta(hours=self.duration['hours'], minutes=self.duration['minutes'])
        arrival_time = time_obj + flight_duration
        self.arrival_time = arrival_time.strftime("%H:%M:%S")
        
    def details(self):
        details = {"Package ID":self.package_id,"From":self.start,"To":self.destination,"Flight Name":self.airline,"Departure time":self.departure_time,"Arrival time":self.arrival_time,"Price":self.price,"Availibility Staus":self.availability_status}
        return details
    
class Hotel(TravelPackage):
    
    def __init__(self, package_id, destination, duration, price, availability_status, hotel_name, rating):
        super().__init__(package_id, destination, duration, price, availability_status)
        self.package_id = package_id
        self.destination = destination
        self.duration = duration
        self.price = price
        self.availability_status = availability_status
        self.hotel_name = hotel_name
        self.rating = rating

    def details(self):
        details = {"Package ID":self.package_id,"City":self.destination,"Hotel name":self.hotel_name,"Rating":self.rating,"Hotel Price":self.price,"Duration":self.duration,"Availibility Status":self.availability_status}
        return details
    
class CarRental(TravelPackage):
    def __init__(self, package_id, destination, duration, price, availability_status, car_model,start,car_transmission,car_fuel,car_seats):
        super().__init__(package_id, destination, duration, price, availability_status)
        self.package_id = package_id
        self.destination = destination
        self.duration = duration
        self.price = price
        self.availability_status = availability_status
        self.city = start
        self.car_model = car_model
        self.car_transmission = car_transmission
        self.car_fuel = car_fuel
        self.car_seats = car_seats

    def details(self):
        details = {"Package ID":self.package_id,"City":self.city,"Car name":self.car_name,"Car Transmisson":self.car_transmission,"Car Fuel":self.car_fuel,"Car Seats":self.car_Seats,"Price":self.car_price,"Duration":self.duration,"Availibility Status":self.availability_status}
        return details

class TravelManager:

    def search_flight_packages(start, destination):
        """Search flights by start and destination."""
        file="packages_flight.csv"
        results = []
        with open(file, mode="r") as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                if row[1].lower() == start.lower() and row[2].lower() == destination.lower():
                    results.append(row)
            print(results)
        if results:
            return results
            print("Matching Flight Packages:")
            print(tabulate(results, headers=header, tablefmt="grid"))
        else:
            print("No matching flight packages found.")

    def search_hotel_packages(city, min_rating=0, file="packages_hotel.csv"):
        """Search hotels by city and minimum rating."""
        results = []
        with open(file, mode="r") as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                if row[1].lower() == city.lower() and float(row[3]) >= float(min_rating):
                    results.append(row)
        if results:
            print("Matching Hotel Packages:")
            print(tabulate(results, headers=header, tablefmt="grid"))
        else:
            print("No matching hotel packages found.")

    def search_car_packages(destination, min_seats, file="packages_car.csv"):
        """Search car rentals by destination and minimum number of seats."""
        results = []
        with open(file, mode="r") as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                if row[1].lower() == destination.lower() and int(row[5]) >= int(min_seats):
                    results.append(row)
        if results:
            print("Matching Car Rental Packages:")
            print(tabulate(results, headers=header, tablefmt="grid"))
        else:
            print("No matching car rental packages found.")

    def __init__(self):
        self.package_list = []

    def determine_file_type(self,file):
        if "hotel" in file:
            if file != "bookings_hotel.csv":
                return "bookings_hotel.csv"
            else:
                return "packages_hotel.csv"
        elif "flight" in file:
            if file != "bookings_flight.csv":
                return "bookings_flight.csv"
            else:
                return "packages_flight.csv"
        else:
            if file != "bookings_car.csv":
                return "bookings_car.csv"
            else:
                return "packages_car.csv"

    def add_package(self,package,file): #package is dictionary
        with open(file,mode = "a",newline='') as f:
            write = csv.writer(f)
            L = []
            for i in package:
                L.append(package[i])
            write.writerow(L)
            self.package_list.append(L)
        

    def update_package(self,package_id,updates,file): #what is updates #sus
        with open(file,mode = "r",) as f,open("dup.csv",mode = "w",newline = '') as f1:
            csvobject1 = csv.reader(f)
            csvobject2 = csv.writer(f1)
            self.package_list = []
            for i in csvobject1:
                if i[0] != package_id:
                    csvobject2.writerow(i)
                    self.package_list.append(i)
                else:
                    L =[]
                    for i in updates:
                        L.append(i)
                    csvobject2.writerow(L)
                    self.package_list.append(L)
        os.remove(file)
        os.rename("dup.csv",file)

    def delete_package(self,package_id,file):
        with open(file,mode = "r",) as f,open("dup.csv",mode = "w",newline = '') as f1:
            csvobject1 = csv.reader(f)
            csvobject2 = csv.writer(f1)
            for i in csvobject1:
                if i[0] != package_id:
                    csvobject2.writerow(i)
        os.remove(file)
        os.rename("dup.csv",file)
        print("Package deleted successfully")

    def save_packages_status(self,file,status,package_id):
        with open(file,mode = "r",) as f,open("dup.csv",mode = "w",newline = '') as f1:
            csvobject1 = csv.reader(f)
            csvobject2 = csv.writer(f1)
            for i in csvobject1:
                if i[0] != package_id:
                    csvobject2.writerow(i)
                else:
                    n = len(i)
                    i[n-1] = status #check
                    csvobject2.writerow(i)
        os.remove(file)
        os.rename("dup.csv",file)

    def load_available_packages(self,file): #check
        with open(file,mode = 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            rows = []
            for i in reader:
                n = len(i)
                if i[n-1] != "Not available": #confirm availibilty staus
                    rows.append(i)
            print(tabulate(rows, headers=header, tablefmt="grid"))

    def load_all_packages(self,file):
        with open(file,mode = "r") as f:
            reader = csv.reader(f)
            header = next(reader)
            rows = list(reader)
            print(tabulate(rows, headers=header, tablefmt="grid"))

    def show_specific_package(self,file,n):
        with open(file,mode = "r") as f:
            reader = csv.reader(f)
            header = next(reader)
            rows = []
            for i in reader:
                if i[0] == n:
                    rows.append(i)
            print(tabulate(rows, headers=header, tablefmt="grid"))


    def make_bookings(self,file):
        file1 = self.determine_file_type(file)
        self.load_all_packages(file)
        status = "True"
        while status:
            n = input("Enter package id of package you want to book")
            with open(file,mode = "r") as f,open(file1,mode = "a",newline='') as f1:
                csvreader = csv.reader(f) #packages file
                csvwriter = csv.writer(f1) #bookings file
                L = []
                for i in csvreader:
                    if i[0] == n:
                        status = "False"
                        L1 = i[:]
                        T1 = "T" + L1[0][1: :]
                        L = [T1]  #sus
                        n = len(L1)
                        L1[n-1] = "Booked"
                        L.extend(L1)
                csvwriter.writerow(L)
            if status == "False":
                current_datetime = datetime.now()
                formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                if "car" in file:
                    L2 = [L[0],L[1],L[2],L[8],L[7],L[3],formatted_datetime]
                if "hotel" in file:
                    L2 = [L[0],L[1],L[2],L[6],L[5],L[3],formatted_datetime]
                if "flight" in file:
                    format = "%H:%M:%S"
                    time_obj1 = datetime.strptime(L[6], format)
                    time_obj2 = datetime.strptime(L[5], format)
                    duration = time_obj1 - time_obj2
                    L2 = [L[0],L[1],L[3],duration,L[7],L[4],formatted_datetime]
                    self.log_transactions("transactions.csv",L2)
                    self.save_packages_status(file,"Not available",n)
            else:
                print("Enter correct package id")

    def load_bookings(self,file,transaction_id):
        with open(file,mode = "r") as f:
            reader = csv.reader(f)
            header = next(reader)
            rows = []
            for i in reader:
                if i[0] == transaction_id:
                    rows.append(i)
            print(tabulate(rows, headers=header, tablefmt="grid"))

    def delete_bookings(self,file,transaction_id):
        with open(file,mode = "r",) as f,open("dup.csv",mode = "w",newline = '') as f1:
            csvobject1 = csv.reader(f)
            csvobject2 = csv.writer(f1)
            for i in csvobject1:
                if i[0] != transaction_id:
                    csvobject2.writerow(i)
                else:
                    n = i[1]
        os.remove(file)
        os.rename("dup.csv",file)
        self.save_packages_status(self.determine_file_type(file),"Not available",n) #sus
        print("Booking has been successfully removed")

    def log_transactions(self,file,L): #no availibilty and cancel
        with open(file,mode = "a",) as f:
            csvobject = csv.writer(f)
            csvobject.writerow(L)
#seperate window(u need to write two line of code for input)
def show_hotels_and_cars(destination, hotel_file="Hotel.csv", car_file="Car_rental.csv"):
    """
    Displays available hotels and car rentals for a given destination.
    """
    import csv
    from tabulate import tabulate

    try:
        # Load Hotels
        with open(hotel_file, mode="r") as h_file:
            h_reader = csv.reader(h_file)
            h_header = next(h_reader)  # Skip header
            hotels = [row for row in h_reader if row[1].lower() == destination.lower()]

        # Load Car Rentals
        with open(car_file, mode="r") as c_file:
            c_reader = csv.reader(c_file)
            c_header = next(c_reader)  # Skip header
            cars = [row for row in c_reader if row[1].lower() == destination.lower()]

        # Print Hotels
        if hotels:
            print("\nHotels available in", destination)
            print(tabulate(hotels, headers=h_header, tablefmt="grid"))
        else:
            print(f"\nNo hotels available in {destination}.")

        # Print Car Rentals
        if cars:
            print("\nCar rentals available in", destination)
            print(tabulate(cars, headers=c_header, tablefmt="grid"))
        else:
            print(f"\nNo car rentals available in {destination}.")

    except FileNotFoundError as e:
        print(f"Error: {e}. Make sure the file exists.")
    except Exception as e:
        print(f"An error occurred: {e}")



