import pandas as pd

class Hotel:
    """Represents a single hotel."""
    def __init__(self, hotel_name, location, best_rating, price_per_night, availability):
        self.hotel_name = hotel_name
        self.location = location
        self.best_rating = best_rating
        self.price_per_night = price_per_night
        self.availability = availability

    def __str__(self):
        return (f"Hotel: {self.hotel_name}, Location: {self.location}, "
                f"Rating: {self.best_rating}, Price: {self.price_per_night}, "
                f"Available: {self.availability}")

class HotelManagement:
    """Manages a collection of Hotel objects."""
    def __init__(self):
        self.hotels = []

    def load_data(self, file_path):
        """Load hotel data from a CSV file and initialize Hotel objects."""
        try:
            data = pd.read_csv(file_path)
            for _, row in data.iterrows():
                hotel = Hotel(
                    hotel_name=row.get('Hotel_Name'),
                    location=row.get('Location'),
                    best_rating=row.get('Best_Rating'),
                    price_per_night=row.get('Price_Per_Night'),
                    availability=row.get('Availability')
                )
                self.hotels.append(hotel)
            print(f"Loaded {len(self.hotels)} hotels successfully.")
        except Exception as e:
            print(f"Error loading data: {e}")

    def filter_by_rating(self, min_rating):
        """Filter hotels with a rating equal to or greater than the given rating."""
        return [hotel for hotel in self.hotels if hotel.best_rating >= min_rating]

    def available_hotels(self):
        """Get a list of all available hotels."""
        return [hotel for hotel in self.hotels if hotel.availability.lower() == 'yes']

    def cheapest_hotel(self):
        """Find the hotel with the lowest price per night."""
        return min(self.hotels, key=lambda hotel: hotel.price_per_night)

    def display_all_hotels(self, limit=5):
        """Display all hotels (or up to the limit)."""
        for hotel in self.hotels[:limit]:
            print(hotel)

# Example Usage
file_path = "/mnt/data/Hotel.csv"
hotel_manager = HotelManagement()

# Load hotels
hotel_manager.load_data(file_path)

# Display first few hotels
hotel_manager.display_all_hotels()

# Filter hotels by a minimum rating
high_rated_hotels = hotel_manager.filter_by_rating(4.5)
print("Highly Rated Hotels:")
for hotel in high_rated_hotels:
    print(hotel)

# List all available hotels
available_hotels = hotel_manager.available_hotels()
print("Available Hotels:")
for hotel in available_hotels:
    print(hotel)

# Get the cheapest hotel
print("Cheapest Hotel:", hotel_manager.cheapest_hotel())
