# Local Host Survival — Offline Disaster Communication Portal

<p align="center">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen" />
  <img src="https://img.shields.io/badge/Python-3.x-blue" />
  <img src="https://img.shields.io/badge/Flask-SocketIO-black" />
  <img src="https://img.shields.io/badge/Offline-100%25-orange" />
  <img src="https://img.shields.io/badge/License-MIT-lightgrey" />
</p>

> A lightweight, **fully offline**, real-time communication platform designed to establish a local information network during natural disasters or internet blackouts — enabling peer-to-peer chat and high-priority emergency alerts over a local Wi-Fi hotspot, **no internet required**.

---

## 📖 Overview

When disaster strikes and internet infrastructure fails, communication becomes the biggest bottleneck for rescue coordination. **Local Host Survival** solves this by turning any single device with Wi-Fi hotspot capability into a self-contained communication hub — allowing nearby devices to instantly connect, chat, and broadcast emergency alerts, all without a single byte of external internet traffic.

---

## 👥 Team & Contributions

This project was built by a 4-member team, with clearly divided ownership so everyone could work in parallel without conflicts.

| Member | Role | Responsibilities |
|---|---|---|
| **[Sanchal Kumar](https://github.com/Sanchal-01)** |  Backend Lead | Flask server & routing, Flask-SocketIO integration, real-time event handling (`send_message`, `broadcast_alert`) |
| **[Shreyash](https://github.com/Shreyash71-byte)** |  Database & Logic Engineer | SQLite schema design, message persistence logic, chat history sync for newly connected devices |
| **[Shorya Dev](https://github.com/shoryadev312-dev)** |  Frontend Developer | Mobile-first UI design, chat interface, login screen, emergency alert banner, tab-based navigation |
| **[Shyam Narayan Pandey](https://github.com/shyamsnp1804)** |  Integration, Testing & Demo Lead | Offline asset management, frontend-backend JS integration, hotspot networking setup, live multi-device testing & demo |

> Backend and Database roles worked closely to wire SQLite into Flask, while Frontend and Integration roles built and tested the client experience end-to-end.

---

## 🌟 Key Features

| Feature | Description |
|---|---|
| 🔌 **100% Offline Capability** | No external CDNs — all assets served locally so the app works even with zero internet access. |
| ⚡ **Real-Time Communication** | Instant, full-duplex messaging across all connected devices via WebSockets. |
| 🆘 **Emergency Broadcasts** | Dedicated priority channel to flash critical alerts to every connected device instantly. |
| 💾 **Persistent Local Database** | Embedded SQLite engine auto-syncs full chat & alert history to newly connected devices. |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python, Flask, Flask-SocketIO |
| **Database** | SQLite3 (Embedded) |
| **Frontend** | Vanilla HTML5, CSS3, JavaScript (Socket.IO client) |

---

## 📁 Project Structure

```text
local-host-survival/
│
├── app.py                 # Core Flask & Socket.IO server engine
├── init_db.py              # SQLite database schema & query module
├── database.db             # Auto-generated SQLite local database
│
├── templates/
│   └── index.html          # Frontend live communication dashboard
│
└── static/
    └── socket.io.js         # Offline Socket.IO client library
```

---

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Sanchal-01/local-host-survival.git
cd local-host-survival
```

### 2. Install Dependencies
Make sure Python is installed, then run:
```bash
pip install flask flask-socketio
```

### 3. Initialize the Database
Builds the required communication tables:
```bash
python init_db.py
```

### 4. Start the Application
```bash
python app.py
```

---

## 💻 How to Test & Deploy Locally

1. Once the server starts, it binds to `0.0.0.0:5000`, allowing access across the local network.
2. Open your browser and go to: `http://127.0.0.1:5000`
3. **Local Network Testing:** Connect other devices (phones, laptops) to the same Wi-Fi router or mobile hotspot. Find your host machine's local IP (e.g., `192.168.X.X`) from the terminal output, then open `http://192.168.X.X:5000` on those devices to simulate a real-world disaster response squad.

---

## 🧭 Use Case

Designed for scenarios like:
- 🌪️ Natural disasters (earthquakes, floods, cyclones) where internet/cell towers are down
- 🏕️ Remote rescue camps needing local coordination
- 🏫 Community shelters requiring an internal alert system

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/Sanchal-01/local-host-survival/issues).

---

## 📜 License

This project is licensed under the **MIT License**.

---

<p align="center">Made with ❤️ by a 4-member team, for a more resilient, connected world — even when the internet isn't.</p>
