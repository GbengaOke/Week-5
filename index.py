#--Python Assignment Assignment 1:
# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, os, storage, battery_life):
        self.brand = brand
        self.model = model
        self.os = os
        self.storage = storage
        self.battery_life = battery_life

    def display_info(self):
        return f"{self.brand} {self.model} runs on {self.os} with {self.storage}GB storage and {self.battery_life} hours of battery life."

    def make_call(self, number):
        return f"Calling {number} using {self.brand} {self.model}..."

    def send_message(self, number, message):
        return f"Sending message to {number}: {message}"

# Subclass: Android, inheriting from Smartphone
class Android(Smartphone):
    def __init__(self, brand, model, os, storage, battery_life, play_store_apps):
        super().__init__(brand, model, os, storage, battery_life)
        self.play_store_apps = play_store_apps

    def download_app(self, app_name):
        return f"Downloading {app_name} from Play Store on {self.brand} {self.model}."

# Subclass: iPhone, inheriting from Smartphone
class iPhone(Smartphone):
    def __init__(self, brand, model, os, storage, battery_life, app_store_apps):
        super().__init__(brand, model, os, storage, battery_life)
        self.app_store_apps = app_store_apps

    def download_app(self, app_name):
        return f"Downloading {app_name} from App Store on {self.brand} {self.model}."

# Creating instances of each class
smartphone1 = Smartphone("Generic", "Model X", "OS 1.0", 64, 10)
android_phone = Android("Samsung", "Galaxy S21", "Android 11", 128, 20, ["WhatsApp", "Instagram"])
iphone = iPhone("Apple", "iPhone 13", "iOS 15", 256, 18, ["iMessage", "FaceTime"])

# Displaying information and using methods
print(smartphone1.display_info())
print(smartphone1.make_call("123-456-7890"))
print(smartphone1.send_message("123-456-7890", "Hello!"))

print(android_phone.display_info())
print(android_phone.make_call("123-456-7890"))
print(android_phone.send_message("123-456-7890", "Hi there!"))
print(android_phone.download_app("TikTok"))

print(iphone.display_info())
print(iphone.make_call("098-765-4321"))
print(iphone.send_message("098-765-4321", "Good day!"))
print(iphone.download_app("Spotify"))


#-- Python Assignment Assignment 2:
# Base class: Vehicle
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.brand} {self.model}"

    def move(self):
        pass

# Subclass: Car
class Car(Vehicle):
    def __init__(self, brand, model, year, fuel_type):
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type

    def move(self):
        print("Driving")

    def display_info(self):
        return f"{super().display_info()} (Fuel: {self.fuel_type})"

# Subclass: Plane
class Plane(Vehicle):
    def __init__(self, brand, model, year, max_altitude):
        super().__init__(brand, model, year)
        self.max_altitude = max_altitude

    def move(self):
        print("Flying")

    def display_info(self):
        return f"{super().display_info()} (Max Altitude: {self.max_altitude} feet)"

# Subclass: Boat
class Boat(Vehicle):
    def __init__(self, brand, model, year, boat_type):
        super().__init__(brand, model, year)
        self.boat_type = boat_type

    def move(self):
        print("Sailing")

    def display_info(self):
        return f"{super().display_info()} (Type: {self.boat_type})"

# Function to demonstrate polymorphism
def demonstrate_movement(vehicles):
    for vehicle in vehicles:
        print(vehicle.display_info())
        vehicle.move()

# Creating instances of each class
car = Car("Toyota", "Camry", 2022, "Gasoline")
plane = Plane("Boeing", "747", 2020, 35000)
boat = Boat("Yamaha", "242X", 2021, "Motorboat")

# List of vehicles
vehicles = [car, plane, boat]

# Demonstrate movement for each vehicle
demonstrate_movement(vehicles)
