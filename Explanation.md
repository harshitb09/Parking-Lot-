# 🚗 Parking Lot System - Low-Level Design (LLD) Explained in Detail

This **Parking Lot System** is a **Low-Level Design (LLD)** implementation built using **Object-Oriented Programming (OOP)** in Python. It efficiently **manages parking spot allocation, vehicle tracking, and payment processing** while maintaining scalability and flexibility for future improvements.

---

## 📌 Overview
The parking lot system simulates a **real-world smart parking lot**, where vehicles can **enter, park, pay, and exit**. The system is designed to handle **multiple types of vehicles**, ensuring that each vehicle is assigned a **properly sized parking spot**. Additionally, a **payment system** calculates parking fees based on the time a vehicle remains parked.

This project follows **Object-Oriented Design (OOD)** principles, making it **modular, scalable, and easy to extend**. The primary focus is on **clean code structure, reusability, and efficiency**.

---

## 🎯 Features Explained in Detail
### ✅ Vehicle Entry & Exit
- When a **vehicle arrives**, the system checks for an **available parking spot** based on the vehicle type (Bike, Car, or Truck).
- If a suitable spot is found, a **ticket is issued**, and the vehicle is parked.
- When the vehicle **exits**, the system calculates the **parking duration** and processes the **payment**.

### ✅ Dynamic Parking Spot Allocation
- Different vehicles require different **parking spot sizes**.
- The system intelligently assigns a **suitable parking spot** based on the **vehicle type**.
- If no parking spot is available, the system notifies the user.

### ✅ Vehicle Type Handling
- The system supports three types of vehicles:
  1. **Bike** – Smallest vehicle type.
  2. **Car** – Medium-sized vehicle.
  3. **Truck** – Requires the largest parking space.

### ✅ Occupied and Free Spot Tracking
- The system maintains a **real-time record** of which parking spots are **occupied** and which are **free**.
- This allows for **efficient spot management** and quick identification of available spots.

### ✅ Payment Processing for Parking Time
- The system **calculates the total parking fee** based on the time the vehicle was parked.
- A **minimum charge** applies for the first hour, with additional charges for extra hours.

### ✅ Scalability and Extensibility
- Designed to **support multiple floors** in the future.
- Can be extended to include **automated license plate recognition** using **computer vision**.
- Allows for easy **integration of EV charging stations**.

---

## 🏗️ System Design & Core Components
The **Parking Lot System** consists of multiple components that work together to manage parking efficiently. Each component follows the **Single Responsibility Principle (SRP)** in **OOD**.

### 🔹 1. `ParkingLot` (Main Controller)
- **Manages multiple parking floors**.
- Assigns parking spots when a vehicle enters.
- Issues **tickets** to track parked vehicles.
- Processes **payments** when a vehicle exits.

### 🔹 2. `ParkingFloor` (Organized Parking)
- Represents a **single floor** in the parking lot.
- Contains multiple **parking spots**.
- Tracks the availability of **parking spots**.

### 🔹 3. `ParkingSpot` (Individual Parking Slots)
- Represents **a single parking space**.
- Stores information on whether the spot is **occupied or free**.
- Assigns a **vehicle** to the spot when parked.

### 🔹 4. `Vehicle` (Represents Different Vehicles)
- Contains information like:
  - **License plate**
  - **Vehicle type** (Bike, Car, or Truck)

### 🔹 5. `Ticket` (Proof of Parking)
- A **unique identifier** issued when a vehicle parks.
- Used to track **payment and parking duration**.

### 🔹 6. `PaymentProcessor` (Handles Parking Charges)
- Calculates parking fees based on **time spent** in the parking lot.
- Processes **payments** when a vehicle exits.

---

## 🛠️ Installation & Usage
### 📥 Prerequisites
Before running the system, make sure you have:
- **Python 3.x** installed.
- **Git** for version control.

### 🚀 Clone the Repository
To get started, clone the repository:
```sh
$ git clone https://github.com/yourusername/parking-lot-LLD.git
$ cd parking-lot-LLD
```

### ▶️ Run the Simulation
Run the Python script to start the simulation:
```sh
$ python parking_lot.py
```

### 📌 Sample Output
When a vehicle enters and exits, the system generates the following output:
```sh
✅ Vehicle CAR - ABC123 parked at Spot 1 [CAR] on Floor 1. Ticket: T-ABC123
💳 Payment of $10 processed for Ticket T-ABC123.
🚗 Vehicle CAR - ABC123 removed from Spot 1 [CAR].
```
This shows that:
1. The car was parked successfully.
2. A ticket was issued.
3. The **payment was processed** before exit.

---

## 📜 Code Structure
The project is **organized** to maintain clarity and modularity:

```
├── parking_lot.py         # Main Parking Lot System
├── README.md              # Project Documentation
```
- `parking_lot.py` → Contains the **entire system implementation**.
- `README.md` → Project **documentation and usage instructions**.

---

## 🔮 Future Enhancements
The current system **lays the foundation** for future improvements. Some planned enhancements include:
- ✅ **Support for multiple floors**.
- ✅ **Real-time availability tracking** using a **database**.
- ✅ **AI-based license plate recognition** for automated parking.
- ✅ **EV charging stations** integration.

These enhancements will make the system **more powerful and future-ready**.

---

## 🛠️ Contributing
This project is **open-source**, and contributions are encouraged! To contribute:
1. **Fork the repository** on GitHub.
2. Create a **new branch** for changes.
3. Make your changes and **commit them**.
4. Submit a **pull request** for review.

For major changes, **open an issue** to discuss your proposed improvements before implementing them.

---

## 📄 License
This project is **licensed under the MIT License**, meaning anyone can freely use, modify, and distribute it.

---

### 🚀 Final Thoughts
This **Parking Lot System LLD** is a **well-structured and scalable solution** for parking management. It follows best practices in **Object-Oriented Design**, ensuring **modularity, reusability, and maintainability**.

By implementing **clean OOP principles**, this system can be **easily extended** to support **advanced features** like AI-based license plate recognition, real-time spot tracking, and smart parking analytics.

This project serves as an excellent **LLD practice** for software engineers, showcasing **real-world problem-solving** using **Python**.

🚀 Happy Coding! 🎯

