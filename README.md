# 🚗 IoT-Based Parking Management System

An intelligent, automated parking system that leverages **IoT sensors**, **Computer Vision**, and **OCR** to manage vehicle entry/exit, monitor real-time slot availability, and reduce traffic congestion. Designed to be scalable for smart cities, malls, and commercial hubs.

![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.8+-blue)
![IoT](https://img.shields.io/badge/IoT-Enabled-orange)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)

---

## 🧠 Features

- 🔍 **Vehicle Detection:** Ultrasonic sensors detect incoming/outgoing vehicles.
- 🛑 **Smart Gate Control:** Servo motor automates entry/exit based on real-time slot availability.
- 📷 **Slot Monitoring:** Camera and Computer Vision detect vacant parking spots.
- 🔐 **License Plate Recognition:** OCR extracts number plates for logging and validation.
- 📊 **Database Integration:** Logs all entry/exit data using MongoDB.
- 📺 **Real-Time Display:** Shows "FULL" or "AVAILABLE" dynamically on a screen.
- 🌐 **Scalable & Modular:** Easily deployable in real-world urban parking environments.

---

## 🛠️ Tech Stack

| Category              | Tools & Technologies                             |
|-----------------------|--------------------------------------------------|
| Programming           | Python, C++                                      |
| IoT Hardware          | Ultrasonic Sensor, Servo Motor                   |                              
| Computer Vision       | OpenCV, OCR (Tesseract)                          |
| Data Management       | MongoDB                                          |
| Version Control       | Git, GitHub                                      |

---

## 🚀 Getting Started

### 📦 Prerequisites
- Python 3.8+
- MongoDB installed locally or hosted
- Arduino (for IoT simulation)
- OpenCV and Tesseract installed

### 🛠️ Installation

```bash
cd smart-parking-system
pip install -r requirements.txt
```
