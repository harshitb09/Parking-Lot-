from enum import Enum
import time

# Define Vehicle Types
class VehicleType(Enum):
    BIKE = 1
    CAR = 2
    TRUCK = 3

# Vehicle Class
class Vehicle:
    def __init__(self, license_plate: str, vehicle_type: VehicleType):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type

    def __str__(self):
        return f"{self.vehicle_type.name} - {self.license_plate}"

# Parking Spot Class
class ParkingSpot:
    def __init__(self, spot_id: int, size: VehicleType):
        self.spot_id = spot_id
        self.size = size
        self.occupied = False
        self.vehicle = None

    def park_vehicle(self, vehicle: Vehicle):
        if self.occupied or vehicle.vehicle_type.value > self.size.value:
            return False
        self.vehicle = vehicle
        self.occupied = True
        return True

    def remove_vehicle(self):
        self.vehicle = None
        self.occupied = False

    def __str__(self):
        return f"Spot {self.spot_id} [{self.size.name}] - {'Occupied' if self.occupied else 'Free'}"

# Parking Floor Class
class ParkingFloor:
    def __init__(self, floor_number: int, spots: list):
        self.floor_number = floor_number
        self.spots = spots

    def find_available_spot(self, vehicle: Vehicle):
        for spot in self.spots:
            if not spot.occupied and vehicle.vehicle_type.value <= spot.size.value:
                return spot
        return None

    def __str__(self):
        return f"Floor {self.floor_number}: " + ", ".join(str(spot) for spot in self.spots)

# Parking Lot Class
class ParkingLot:
    def __init__(self, floors: list):
        self.floors = floors
        self.active_tickets = {}

    def park_vehicle(self, vehicle: Vehicle):
        for floor in self.floors:
            spot = floor.find_available_spot(vehicle)
            if spot:
                spot.park_vehicle(vehicle)
                ticket_id = f"T-{vehicle.license_plate}"
                self.active_tickets[ticket_id] = (vehicle, spot)
                print(f"✅ Vehicle {vehicle} parked at {spot} on Floor {floor.floor_number}. Ticket: {ticket_id}")
                return ticket_id
        print("❌ No available spots!")
        return None

    def remove_vehicle(self, ticket_id: str):
        if ticket_id not in self.active_tickets:
            print("❌ Invalid ticket!")
            return False
        vehicle, spot = self.active_tickets.pop(ticket_id)
        spot.remove_vehicle()
        print(f"🚗 Vehicle {vehicle} removed from {spot}.")
        return True

# Payment Processor Class
class PaymentProcessor:
    def __init__(self, rate_per_hour=10):
        self.rate_per_hour = rate_per_hour

    def calculate_fee(self, parked_time_seconds):
        hours = max(1, parked_time_seconds // 3600)
        return hours * self.rate_per_hour

    def process_payment(self, ticket_id, entry_time):
        parked_time = time.time() - entry_time
        fee = self.calculate_fee(parked_time)
        print(f"💳 Payment of ${fee} processed for Ticket {ticket_id}.")
        return fee

# Simulating the Parking Lot
spots1 = [ParkingSpot(i, VehicleType.CAR) for i in range(1, 6)]
spots2 = [ParkingSpot(i, VehicleType.BIKE) for i in range(6, 11)]
floor1 = ParkingFloor(1, spots1 + spots2)

parking_lot = ParkingLot([floor1])

vehicle1 = Vehicle("ABC123", VehicleType.CAR)
ticket1 = parking_lot.park_vehicle(vehicle1)

entry_time = time.time()
time.sleep(2)

payment_processor = PaymentProcessor()
payment_processor.process_payment(ticket1, entry_time)
parking_lot.remove_vehicle(ticket1)
