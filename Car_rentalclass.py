import pandas as pd

class Car:
    """Represents a single car in the rental system."""
    def __init__(self, car_model, daily_rate, car_seats, car_fuel, car_transmission, city):
        self.car_model = car_model
        self.daily_rate = daily_rate
        self.car_seats = car_seats
        self.car_fuel = car_fuel
        self.car_transmission = car_transmission
        self.city = city

    def __str__(self):
        return (f"Model: {self.car_model}, Rate: {self.daily_rate}, "
                f"Seats: {self.car_seats}, Fuel: {self.car_fuel}, "
                f"Transmission: {self.car_transmission}, City: {self.city}")

class CarRentalSystem:
    """Manages a collection of Car objects for a rental system."""
    def __init__(self):
        self.cars = []

    def load_data(self, file_path):
        """Load car rental data from a CSV file and initialize Car objects."""
        try:
            data = pd.read_csv(file_path)
            for _, row in data.iterrows():
                car = Car(
                    car_model=row.get('Car_Model'),
                    daily_rate=row.get('Daily_Rate'),
                    car_seats=row.get('Car_Seats'),
                    car_fuel=row.get('Car_Fuel'),
                    car_transmission=row.get('Car_Transmission'),
                    city=row.get('City')
                )
                self.cars.append(car)
            print(f"Loaded {len(self.cars)} cars successfully.")
        except Exception as e:
            print(f"Error loading data: {e}")

    def filter_by_city(self, city_name):
        """Filter cars by city."""
        return [car for car in self.cars if car.city.lower() == city_name.lower()]

    def cheapest_car(self):
        """Find the car with the lowest daily rate."""
        return min(self.cars, key=lambda car: car.daily_rate)

    def filter_by_seats(self, min_seats):
        """Filter cars with at least a specified number of seats."""
        return [car for car in self.cars if car.car_seats >= min_seats]

    def display_all_cars(self, limit=5):
        """Display all cars (or up to the limit)."""
        for car in self.cars[:limit]:
            print(car)

# Example Usage
file_path = "/mnt/data/Car_rental.csv"
rental_system = CarRentalSystem()

# Load cars
rental_system.load_data(file_path)

# Display first few cars
rental_system.display_all_cars()

# Filter cars by city
city_cars = rental_system.filter_by_city("New York")
print("Cars in New York:")
for car in city_cars:
    print(car)

# Filter cars by minimum number of seats
cars_with_min_seats = rental_system.filter_by_seats(5)
print("Cars with at least 5 seats:")
for car in cars_with_min_seats:
    print(car)

# Get the cheapest car
print("Cheapest Car:", rental_system.cheapest_car())
