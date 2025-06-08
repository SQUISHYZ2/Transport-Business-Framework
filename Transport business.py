import mysql.connector
from mysql.connector import Error

class TransportBusiness:
    def __init__(self, host_name, database_name, user_name, user_password):
        self.host_name = "localhost"
        self.database_name = "Transport"
        self.user_name = "root"
        self.user_password ="Incorrect"
        self.connection = None

    def connect_to_database(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host_name,   
                database=self.database_name,
                user=self.user_name,
                password=self.user_password
            )
            print("Connected to database successfully.")
        except Error as error:
            print(f"Failed to connect to database: {error}")

    def create_tables(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS vehicles (
                    vehicle_id INT AUTO_INCREMENT PRIMARY KEY,
                    vehicle_type VARCHAR(255) NOT NULL,
                    vehicle_number VARCHAR(255) NOT NULL,
                    capacity INT NOT NULL
                );
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS drivers (
                    driver_id INT AUTO_INCREMENT PRIMARY KEY,
                    driver_name VARCHAR(255) NOT NULL,
                    driver_phone VARCHAR(255) NOT NULL,
                    license_number VARCHAR(255) NOT NULL
                );
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS trips (
                    trip_id INT AUTO_INCREMENT PRIMARY KEY,
                    vehicle_id INT NOT NULL,
                    driver_id INT NOT NULL,
                    trip_date DATE NOT NULL,
                    trip_time TIME NOT NULL,
                    pickup_location VARCHAR(255) NOT NULL,
                    drop_location VARCHAR(255) NOT NULL,
                    total_sum VARCHAR(10) NOT NULL,
                );
            """)
            self.connection.commit()
            print("Tables created successfully.")
        except Error as error:
            print(f"Failed to create tables: {error}")

    def add_vehicle(self, vehicle_type, vehicle_number, capacity):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO vehicles (vehicle_type, vehicle_number, capacity)
                VALUES (%s, %s, %s);
            """, (vehicle_type, vehicle_number, capacity))
            self.connection.commit()
            print("Vehicle added successfully.")
        except Error as error:
            print(f"Failed to add vehicle: {error}")

    def add_driver(self, driver_name, driver_phone, license_number):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO drivers (driver_name, driver_phone, license_number)
                VALUES (%s, %s, %s);
            """, (driver_name, driver_phone, license_number))
            self.connection.commit()
            print("Driver added successfully.")
        except Error as error:
            print(f"Failed to add driver: {error}")

    def add_trip(self, vehicle_id, driver_id, trip_date, trip_time, pickup_location, drop_location, total_sum):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO trips (vehicle_id, driver_id, trip_date, trip_time, pickup_location, drop_location, total_sum)
                VALUES (%s, %s, %s, %s, %s, %s, %s);
            """, (vehicle_id, driver_id, trip_date, trip_time, pickup_location, drop_location, total_sum))
            self.connection.commit()
            print("Trip added successfully.")
        except Error as error:
            print(f"Failed to add trip: {error}")

    def display_vehicles(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM vehicles;")
            vehicles = cursor.fetchall()
            for vehicle in vehicles:
                print("Vehicle ID:", vehicle[0])
                print("Vehicle Type:", vehicle[1])
                print("Vehicle Number:", vehicle[2])
                print("Capacity:", vehicle[3])
                print("------------------------")
        except Error as error:
            print(f"Failed to display vehicles: {error}")

    def display_drivers(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM drivers;")
            drivers = cursor.fetchall()
            for driver in drivers:
                print("Driver ID:", driver[0])
                print("Driver Name:", driver[1])
                print("Driver Phone:", driver[2])
                print("License Number:", driver[3])
                print("------------------------")
        except Error as error:
            print(f"Failed to display drivers: {error}")

    def display_trips(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM trips;")
            trips = cursor.fetchall()
            for trip in trips:
                print("Trip ID:",trip[0])
                print("Vehicle ID:",trip[1])
                print("Driver ID:",trip[2])
                print("Trip Date:",trip[3])
                print("Trip Time:",trip[4])
                print("Pickup Location:", trip[5])
                print("Drop Location:", trip[6])
                print("Total Sum earned:", trip[7])
                print("------------------------")
        except Error as error:
            print(f"Failed to display trips: {error}")

def main():
    host_name = "localhost"
    database_name = "transport"
    user_name = "root"
    user_password = ""
    transport_business = TransportBusiness(host_name, database_name, user_name, user_password)
    transport_business.connect_to_database()
    transport_business.create_tables()
    while True:
        print("Welcome Admin!")
        print("\n1. Add Vehicle")
        print("2. Add Driver")
        print("3. Add Trip")
        print("4. Display Vehicles")
        print("5. Display Drivers")
        print("6. Display Trips")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            vehicle_type = input("Enter vehicle type: ")
            vehicle_number = input("Enter vehicle number: ")
            capacity = int(input("Enter capacity: "))
            transport_business.add_vehicle(vehicle_type, vehicle_number, capacity)
        elif choice == "2":
            driver_name = input("Enter driver name: ")
            driver_phone = input("Enter driver phone: ")
            license_number = input("Enter license number: ")
            transport_business.add_driver(driver_name, driver_phone, license_number)
        elif choice == "3":
            vehicle_id = input("Enter vehicle ID: ")
            driver_id = input("Enter driver ID: ")
            trip_date = input("Enter trip date (YYYY-MM-DD): ")
            trip_time = input("Enter trip time (HH:MM:SS): ")
            pickup_location = input("Enter pickup location: ")
            drop_location = input("Enter drop location: ")
            total_sum = ""
            for char in trip_time: 
                 if char != ":":
                      total_sum += char
            transport_business.add_trip(vehicle_id, driver_id, trip_date, trip_time, pickup_location, drop_location, total_sum)
        elif choice == "4":
            transport_business.display_vehicles()
        elif choice == "5":
            transport_business.display_drivers()
        elif choice == "6":
            transport_business.display_trips()
        elif choice == "7":
            print("Thank you for visiting!")
            print("Terminating Program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
main()


