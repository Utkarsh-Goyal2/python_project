import pandas as pd

class Car:
    """Represents a single car in the rental system."""
    def __init__(self, car_model, rental_company, daily_rate, availability):
        self.car_model = car_model
        self.rental_company = rental_company
        self.daily_rate = daily_rate
        self.availability = availability

    def __str__(self):
        return (f"Model: {self.car_model}, Company: {self.rental_company}, "
                f"Rate: {self.daily_rate}, Available: {self.availability}")

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
                    rental_company=row.get('Rental_Company'),
                    daily_rate=row.get('Daily_Rate'),
                    availability=row.get('Availability')
                )
                self.cars.append(car)
            print(f"Loaded {len(self.cars)} cars successfully.")
        except Exception as e:
            print(f"Error loading data: {e}")

    def filter_by_company(self, company_name):
        """Filter cars by rental company."""
        return [car for car in self.cars if car.rental_company == company_name]

    def available_cars(self):
        """Get a list of all available cars."""
        return [car for car in self.cars if car.availability.lower() == 'yes']

    def cheapest_car(self):
        """Find the car with the lowest daily rate."""
        return min(self.cars, key=lambda car: car.daily_rate)

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

# Filter cars by a specific rental company
hertz_cars = rental_system.filter_by_company("Hertz")
for car in hertz_cars:
    print(car)

# List all available cars
available = rental_system.available_cars()
print("Available Cars:")
for car in available:
    print(car)

# Get the cheapest car
print("Cheapest Car:", rental_system.cheapest_car())
