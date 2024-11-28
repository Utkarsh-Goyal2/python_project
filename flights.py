"""
Update bookings is problem
Printing bookings in table order
Add booking time in transactions
Exception handling
"""
import csv
import os
from datetime import datetime
class TravelPackage:
    def __init__(self,package_id,destination,duration,price,availability_status):
        self.package_id = package_id
        self.destination = destination
        self.duration = duration
        self.price = price
        self.availability_status = availability_status
    def details(self):
        d = {"Package ID": self.package_id,"Destination": self.destination,"Duration": self.duration,"Price": self.price,"Availability": self.availability_status}
        return d
    
class Flight(TravelPackage):
    
    def __init__(self,package_id,destination,duration,price,availability_status,airline,departure_time):
        super().__init__(package_id,destination,duration,price,availability_status)
        self.airline = airline
        self.departure_time = departure_time
    
    def details(self):
        details = super().details()
        details["Airline"] = self.airline
        details["Departure Time"] = self.departure_time
        return details
    
class Hotel(TravelPackage):
    
    def __init__(self, package_id, destination, duration, price, availability_status, hotel_name, rating):
        super().__init__(package_id, destination, duration, price, availability_status)
        self.hotel_name = hotel_name
        self.rating = rating

    def details(self):
        details = super().details()
        details["Hotel"] = self.hotel_name
        details["Rating"] = self.rating
        return details
    
class CarRental(TravelPackage):
    def __init__(self, package_id, destination, duration, price, availability_status, rental_company, car_model):
        super().__init__(package_id, destination, duration, price, availability_status)
        self.rental_company = rental_company
        self.car_model = car_model

    def details(self):
        details = super().details()
        details["Rental Company"]= self.rental_company 
        details["Car Model"]= self.car_model
        return details

class TravelManager:
    def __init__(self):
        self.package_list = []

    def determine_file_type(self,file):
        if "hotel" in file:
            return "bookings_hotel.csv"
        elif "flight" in file:
            return "bookings_flight.csv"
        else:
            return "bookings_car.csv"

    def add_package(self,package,file): #package is dictionary
        with open(file,mode = "a",newline='') as f:
            write = csv.writer(f)
            L = []
            for i in package:
                L.append(i)
            write.writerow(L)
            self.package_list.append(L)

    def update_package(self,package_id,updates,file):
        with open(file,mode = "r",) as f,open("dup,csv",mode = "w",newline = '') as f1:
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
        with open(file,mode = "r",) as f,open("dup,csv",mode = "w",newline = '') as f1:
            csvobject1 = csv.reader(f)
            csvobject2 = csv.writer(f1)
            for i in csvobject1:
                if i[0] != package_id:
                    csvobject2.writerow(i)
        os.remove(file)
        os.rename("dup.csv",file)
        print("Package deleted successfully")

    def save_packages_status(self,file,status,package_id):
        with open(file,mode = "r",) as f,open("dup,csv",mode = "w",newline = '') as f1:
            csvobject1 = csv.reader(f)
            csvobject2 = csv.writer(f1)
            for i in csvobject1:
                if i[0] != package_id:
                    csvobject2.writerow(i)
                else:
                    i[4] = status
                    csvobject2.writerow(i)
        os.remove(file)
        os.rename("dup.csv",file)

    def load_available_packages(self,file):
        with open(file,mode = 'r') as f:
            reader = csv.reader(f)
            for i in reader:
                if i[4] != "Not available": #Need to tabulate somehow
                    print(i)

    def load_all_packages(self,file):
        with open(file,mode = "r") as f:
            reader = csv.reader(f)
            for i in reader:
                print(i) #Need to tabulate somehow

    def make_bookings(self,file):
        file1 = self.determine_file_type(file)
        self.load_all_packages(file)
        while True:
            n = input("Enter package id of package you want to book")
            status = "False"
            with open(file,mode = "r") as f,open(file1,mode = "a",newline='') as f1:
                csvreader = csv.reader(f)
                csvwriter = csv.writer(f1)
                L = []
                for i in csvreader:
                    if i[0] == n:
                        status = "True"
                        T1 = "T" + i[0][1: :]
                        i[5] = "Booked"
                        L = [T1]  #idk what to do
                        L.extend(i)
                csvwriter.writerow(L)
            if status == "True":
                current_datetime = datetime.now()
                formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                L.append(formatted_datetime)
                self.log_transactions("transactions.csv",L)
                break
            else:
                print("Enter correct package id")


            
    def load_bookings(self,file,transaction_id):
        with open(file,mode = "r") as f:
            reader = csv.reader(f)
            next(reader)
            for i in reader:
                if i[1] == transaction_id:
                    print(i) #Need to tabulate somehow

    def delete_bookings(self,file,transaction_id):
        with open(file,mode = "r",) as f,open("dup,csv",mode = "w",newline = '') as f1:
            csvobject1 = csv.reader(f)
            csvobject2 = csv.writer(f1)
            for i in csvobject1:
                if i[0] != transaction_id:
                    csvobject2.writerow(i)
        os.remove(file)
        os.rename("dup.csv",file)
        print("Booking has been successfully removed")

    def log_transactions(self,file,L):
        with open(file,mode = "a",) as f:
            csvobject = csv.writer(f)
            csvobject.writerow(L)

    
def all_file_creation():
    file_creation("packages_flight.csv",["Package ID", "Destination", "Duration", "Price", "Availability", "Airline", "Departure Time"])
    file_creation("bookings_flight.csv",["Transaction ID","Package ID", "Destination", "Duration", "Price", "Availability", "Airline", "Departure Time"])
    file_creation("packages_hotel.csv",["Package ID", "Destination", "Duration", "Price", "Availability", "Hotel Name", "Rating"])
    file_creation("bookings_hotel.csv",["Transaction ID","Package ID", "Destination", "Duration", "Price", "Availability", "Hotel name", "Rating"])
    file_creation("packages_car.csv",["Package ID", "Destination", "Duration", "Price", "Availability", "Car Model", "Rental Company"])
    file_creation("bookings_car.csv",["Transaction ID","Package ID", "Destination", "Duration", "Price", "Availability", "Car Model", "Rental Company"])
    file_creation("transactions.csv",["Transaction ID","Package ID", "Destination", "Duration", "Price", "Availability", "Attribute 1", "Attribute 2","Booking Time"])

def file_creation(file1,L):
    with open(file1,mode = "w",newline = '') as f1:
        csvobject1 = csv.writer(f1)
        csvobject1.writerow(L)
           
while True:
    all_file_creation()
    package1 = Flight("F001","Thailand","12 hours","Available","Boeing","12:00:00")
    package2 = Hotel("H001","Bangkok","48 hours","10000","Available","Taj Hotels","5.0")
    package3 = CarRental("C001","Lonavla","48 hours","15000","Available","Toyota","Sedan")
    manager = TravelManager()
    manager.add_package(package1.details(),"packages_flight.csv")
    manager.add_package(package2.details(),"packages_hotel.csv")
    manager.add_package(package3.details(),"packages_car.csv")





