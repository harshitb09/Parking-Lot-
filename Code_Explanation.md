### **Explanation of the Code - Parking Lot System (LLD)**

This **Parking Lot System** is designed using **Object-Oriented Programming (OOP)** principles in Python. It efficiently manages **parking spot allocation, vehicle tracking, and payment processing**, ensuring scalability and extensibility.

---

## **1. Importing Required Libraries**
```python
from enum import Enum
import time
```
- `Enum`: Used to define **VehicleType**, allowing us to categorize different vehicle sizes.
- `time`: Used in the **PaymentProcessor** to calculate parking duration.

---

## **2. Defining Vehicle Types Using Enum**
```python
class VehicleType(Enum):
    BIKE = 1
    CAR = 2
    TRUCK = 3
```
- This enumeration (`Enum`) defines three **vehicle categories**:
  - **BIKE** → Smallest vehicle type.
  - **CAR** → Medium-sized vehicle.
  - **TRUCK** → Largest vehicle type.
- The assigned **integer values** help in determining which vehicles can park in which spots.

---

## **3. Vehicle Class**
```python
class Vehicle:
    def __init__(self, license_plate: str, vehicle_type: VehicleType):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type

    def __str__(self):
        return f"{self.vehicle_type.name} - {self.license_plate}"
```
- **Represents a vehicle** entering the parking lot.
- Stores:
  - `license_plate`: Unique identifier for each vehicle.
  - `vehicle_type`: The type of vehicle (`BIKE`, `CAR`, `TRUCK`).
- The `__str__` method is used for easy debugging and printing.

---

## **4. Parking Spot Class**
```python
class ParkingSpot:
    def __init__(self, spot_id: int, size: VehicleType):
        self.spot_id = spot_id
        self.size = size
        self.occupied = False
        self.vehicle = None
```
- Represents a **single parking spot**.
- Stores:
  - `spot_id`: Unique number assigned to the spot.
  - `size`: The type of vehicles the spot can accommodate.
  - `occupied`: Tracks whether the spot is free or occupied.
  - `vehicle`: Stores the parked vehicle.

### **Park a Vehicle in a Spot**
```python
def park_vehicle(self, vehicle: Vehicle):
    if self.occupied or vehicle.vehicle_type.value > self.size.value:
        return False
    self.vehicle = vehicle
    self.occupied = True
    return True
```
- Ensures a **vehicle can park only if**:
  1. The spot is **not occupied**.
  2. The vehicle type is **smaller or equal** to the spot size.

### **Remove a Vehicle from a Spot**
```python
def remove_vehicle(self):
    self.vehicle = None
    self.occupied = False
```
- **Clears the parking spot** when a vehicle exits.

---

## **5. Parking Floor Class**
```python
class ParkingFloor:
    def __init__(self, floor_number: int, spots: list):
        self.floor_number = floor_number
        self.spots = spots
```
- Represents a **floor** in the parking lot.
- Stores:
  - `floor_number`: The floor’s identifier.
  - `spots`: A list of **ParkingSpot** objects.

### **Find an Available Parking Spot**
```python
def find_available_spot(self, vehicle: Vehicle):
    for spot in self.spots:
        if not spot.occupied and vehicle.vehicle_type.value <= spot.size.value:
            return spot
    return None
```
- Iterates over all parking spots on a floor.
- Returns the **first available spot** that fits the vehicle.

---

## **6. Parking Lot Class (Main Controller)**
```python
class ParkingLot:
    def __init__(self, floors: list):
        self.floors = floors
        self.active_tickets = {}
```
- Represents the **entire parking lot**, consisting of **multiple floors**.
- Stores:
  - `floors`: A list of **ParkingFloor** objects.
  - `active_tickets`: A dictionary to keep track of parked vehicles `{ticket_id: (vehicle, parking_spot)}`.

### **Park a Vehicle**
```python
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
```
- Searches all floors for an available spot.
- If a suitable spot is found:
  1. Parks the vehicle.
  2. Generates a **ticket ID**.
  3. Stores the vehicle and spot details in `active_tickets`.
- Returns **None** if no spot is available.

### **Remove a Vehicle**
```python
def remove_vehicle(self, ticket_id: str):
    if ticket_id not in self.active_tickets:
        print("❌ Invalid ticket!")
        return False
    vehicle, spot = self.active_tickets.pop(ticket_id)
    spot.remove_vehicle()
    print(f"🚗 Vehicle {vehicle} removed from {spot}.")
    return True
```
- Uses the **ticket ID** to find the parked vehicle.
- Removes the vehicle and **marks the spot as free**.

---

## **7. Payment Processor Class**
```python
class PaymentProcessor:
    def __init__(self, rate_per_hour=10):
        self.rate_per_hour = rate_per_hour
```
- Manages **payment processing** for parking.
- The default charge is `$10 per hour`.

### **Calculate Parking Fee**
```python
def calculate_fee(self, parked_time_seconds):
    hours = max(1, parked_time_seconds // 3600)
    return hours * self.rate_per_hour
```
- Ensures a **minimum of 1 hour** is charged.
- Computes fees based on **total time parked**.

### **Process Payment**
```python
def process_payment(self, ticket_id, entry_time):
    parked_time = time.time() - entry_time
    fee = self.calculate_fee(parked_time)
    print(f"💳 Payment of ${fee} processed for Ticket {ticket_id}.")
    return fee
```
- Calculates **total parking time** and processes payment.

---

## **8. Simulating the Parking Lot**
```python
spots1 = [ParkingSpot(i, VehicleType.CAR) for i in range(1, 6)]
spots2 = [ParkingSpot(i, VehicleType.BIKE) for i in range(6, 11)]
floor1 = ParkingFloor(1, spots1 + spots2)
```
- Creates **5 CAR parking spots** and **5 BIKE spots** on **Floor 1**.

```python
parking_lot = ParkingLot([floor1])
```
- Initializes the **ParkingLot** with **one floor**.

```python
vehicle1 = Vehicle("ABC123", VehicleType.CAR)
ticket1 = parking_lot.park_vehicle(vehicle1)
```
- A **car enters** and gets a **parking ticket**.

```python
entry_time = time.time()
time.sleep(2)
```
- Simulates **time spent in the parking lot**.

```python
payment_processor = PaymentProcessor()
payment_processor.process_payment(ticket1, entry_time)
```
- **Processes the payment** based on parked time.

```python
parking_lot.remove_vehicle(ticket1)
```
- **Removes the vehicle** from the parking lot.

---

## **🚀 Final Thoughts**
This **Parking Lot System LLD** is a **real-world simulation** of a smart parking system. It follows **clean Object-Oriented Design**, ensuring modularity, reusability, and extensibility.

### **Possible Enhancements**
- Add **multiple floors**.
- Implement **real-time spot tracking**.
- Integrate **license plate recognition (AI)**.
- Support **EV charging stations**.

This project is a great way to **practice LLD concepts in Python** while solving a real-world problem efficiently! 🚗🔧
