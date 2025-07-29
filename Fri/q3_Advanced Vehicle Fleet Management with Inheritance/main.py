from datetime import datetime, timedelta

# ===== Base Class =====
class Vehicle:
    def __init__(self, vehicle_id, make, model, year, daily_rate):
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.year = year
        self.daily_rate = daily_rate
        self.is_available = True
        self.mileage = 0
        self.fuel_type = "Petrol"  # default

    def rent(self):
        if not self.is_available:
            return "Vehicle not available"
        self.is_available = False
        return "Rented successfully"

    def return_vehicle(self):
        self.is_available = True
        return "Returned successfully"

    def calculate_rental_cost(self, days):
        return self.daily_rate * days

    def get_vehicle_info(self):
        return f"{self.make} {self.model} ({self.year}) - ID: {self.vehicle_id}"

    def get_fuel_efficiency(self):
        return "Not implemented"


# ===== Car Class =====
class Car(Vehicle):
    def __init__(self, vehicle_id, make, model, year, daily_rate, seating_capacity, transmission_type, has_gps):
        super().__init__(vehicle_id, make, model, year, daily_rate)
        self.seating_capacity = seating_capacity
        self.transmission_type = transmission_type
        self.has_gps = has_gps

    def calculate_rental_cost(self, days):
        return self.daily_rate * days  # no multiplier

    def get_vehicle_info(self):
        return f"{super().get_vehicle_info()} | Type: Car | Seats: {self.seating_capacity}"

    def get_fuel_efficiency(self):
        if self.transmission_type == "Automatic":
            return {"city_mpg": 20, "highway_mpg": 25}
        else:
            return {"city_mpg": 25, "highway_mpg": 30}


# ===== Motorcycle Class =====
class Motorcycle(Vehicle):
    def __init__(self, vehicle_id, make, model, year, daily_rate, engine_cc, bike_type):
        super().__init__(vehicle_id, make, model, year, daily_rate)
        self.engine_cc = engine_cc
        self.bike_type = bike_type

    def calculate_rental_cost(self, days):
        if days < 7:
            return self.daily_rate * days * 0.8  # 20% discount
        return self.daily_rate * days

    def get_vehicle_info(self):
        return f"{super().get_vehicle_info()} | Type: Motorcycle | CC: {self.engine_cc}"

    def get_fuel_efficiency(self):
        return 45  # average mpg for motorcycle


# ===== Truck Class =====
class Truck(Vehicle):
    def __init__(self, vehicle_id, make, model, year, daily_rate, cargo_capacity, license_required, max_weight):
        super().__init__(vehicle_id, make, model, year, daily_rate)
        self.cargo_capacity = cargo_capacity
        self.license_required = license_required
        self.max_weight = max_weight

    def calculate_rental_cost(self, days):
        return self.daily_rate * days * 1.5  # 50% surcharge for commercial

    def get_vehicle_info(self):
        return f"{super().get_vehicle_info()} | Type: Truck | Cargo: {self.cargo_capacity}kg"

    def get_fuel_efficiency(self):
        return {
            "empty_mpg": 12,
            "loaded_mpg": 8
        }
