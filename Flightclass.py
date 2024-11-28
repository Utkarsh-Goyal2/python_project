class Flight:
    """Represents a single flight."""
    def __init__(self, airline, departure_time, arrival_time, price, origin, destination):
        self.airline = airline
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.price = price
        self.origin = origin
        self.destination = destination

    def __str__(self):
        return (f"Airline: {self.airline}, Departure: {self.departure_time}, "
                f"Arrival: {self.arrival_time}, Price: {self.price}, "
                f"From: {self.origin}, To: {self.destination}")

class FlightsData:
    """Manages a collection of Flight objects."""
    def __init__(self):
        self.flights = []

    def load_data(self, file_path):
        """Load flights from a CSV file and initialize Flight objects."""
        try:
            data = pd.read_csv(file_path)
            for _, row in data.iterrows():
                flight = Flight(
                    airline=row.get('Flight_Name'),
                    departure_time=row.get('Flight_Departure'),
                    arrival_time=row.get('Flight_Arrival'),
                    price=row.get('Flight_Price'),
                    origin=row.get('From'),
                    destination=row.get('To')
                )
                self.flights.append(flight)
            print(f"Loaded {len(self.flights)} flights successfully.")
        except Exception as e:
            print(f"Error loading data: {e}")

    def filter_by_airline(self, airline):
        """Filter flights by airline name."""
        return [flight for flight in self.flights if flight.airline == airline]

    def filter_by_origin(self, origin):
        """Filter flights by origin."""
        return [flight for flight in self.flights if flight.origin == origin]

    def display_all_flights(self, limit=5):
        """Display all flights (or up to the limit)."""
        for flight in self.flights[:limit]:
            print(flight)

    def get_cheapest_flight(self):
        """Get the flight with the lowest price."""
        return min(self.flights, key=lambda flight: flight.price)

    def save_data(self, output_path):
        """Save the current flights to a CSV file."""
        try:
            data = [{
                'Airline': flight.airline,
                'Departure': flight.departure_time,
                'Arrival': flight.arrival_time,
                'Price': flight.price,
                'From': flight.origin,
                'To': flight.destination
            } for flight in self.flights]
            pd.DataFrame(data).to_csv(output_path, index=False)
            print(f"Flights saved to {output_path}")
        except Exception as e:
            print(f"Error saving data: {e}")

# Example Usage
file_path = "/mnt/data/Flights.csv"
flights_manager = FlightsData()

# Load flights
flights_manager.load_data(file_path)

# Display first few flights
flights_manager.display_all_flights()

# Filter by airline
indigo_flights = flights_manager.filter_by_airline("IndiGo")
for flight in indigo_flights:
    print(flight)

# Get the cheapest flight
print("Cheapest Flight:", flights_manager.get_cheapest_flight())

# Save data to a new file
flights_manager.save_data("/mnt/data/Cleaned_Flights.csv")
