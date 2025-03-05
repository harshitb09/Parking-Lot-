# 🚗 Parking Lot System - Low-Level Design (LLD)

## 📌 Overview
This project is a **Low-Level Design (LLD)** implementation of a **smart parking lot system** using **object-oriented programming (OOP) principles** in Python. It efficiently manages **parking spot allocation, vehicle tracking, and payment processing** while ensuring scalability and extensibility.

## 🎯 Features
- ✅ Vehicles can **enter and exit** the parking lot.
- ✅ The system assigns an **available parking spot** dynamically.
- ✅ Supports **different vehicle types** (Bike, Car, Truck) with appropriate-sized spots.
- ✅ Keeps track of **occupied and free spots**.
- ✅ Handles **payments** based on parking time.
- ✅ Designed for **scalability and extensibility**.

## 🏗️ System Design
### 🔹 Core Entities
1. **ParkingLot** → Manages floors and spot allocation.
2. **ParkingFloor** → Contains multiple parking spots.
3. **ParkingSpot** → Represents individual parking slots.
4. **Vehicle** → Represents different types of vehicles.
5. **Ticket** → Issued when a vehicle is parked.
6. **PaymentProcessor** → Handles parking fees and payments.

## 🛠️ Installation & Usage
### 📥 Prerequisites
- Python 3.x
- Git (for version control)

### 🚀 Clone the Repository
```sh
$ git clone https://github.com/yourusername/parking-lot-LLD.git
$ cd parking-lot-LLD
```

### ▶️ Run the Simulation
```sh
$ python parking_lot.py
```

### 📌 Sample Output
```sh
✅ Vehicle CAR - ABC123 parked at Spot 1 [CAR] on Floor 1. Ticket: T-ABC123
💳 Payment of $10 processed for Ticket T-ABC123.
🚗 Vehicle CAR - ABC123 removed from Spot 1 [CAR].
```

## 📜 Code Structure
```
├── parking_lot.py         # Main Parking Lot System
├── README.md              # Project Documentation
```

## 🔮 Future Enhancements
- ✅ Add support for **multiple floors**.
- ✅ Implement **real-time availability tracking** using a database.
- ✅ Integrate **license plate recognition** (AI 🤖).
- ✅ Introduce **EV charging stations**.

## 🛠️ Contributing
Contributions are welcome! Please fork the repository and submit a pull request. For major changes, open an issue first to discuss the proposed changes.

## 📄 License
This project is **open-source** under the **MIT License**.

---
🚀 **Happy Coding!** 🎯

