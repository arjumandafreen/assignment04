# 🎮 Simple Online Multiplayer Game (Python + Pygame)

This project is a **basic 2-player online multiplayer game** built with **Python**, **Pygame**, and **Sockets**. It allows two players to move colored blocks on a shared game window in real time.

## 🧩 Project Structure

- `server.py` — Handles connections from clients, receives player movement data, and sends updates to all connected players.
- `client.py` — Connects to the server, allows a user to move their player using arrow keys, and displays other players on the screen.

## 🚀 How It Works

1. The **server** runs on a host machine and listens for client connections.
2. Each **client** connects to the server and gets assigned a player (with unique color and position).
3. Players use the **arrow keys** to move their block around.
4. Each client's position is sent to the server, which then broadcasts it to all players to ensure synchronization.

---

## 🖥️ Requirements

- Python 3.x
- Pygame

### 📦 Install Requirements

```bash
pip install pygame
🛠️ How to Run
1. Start the Server
bash
Copy
Edit
python server.py
You should see:

pgsql
Copy
Edit
🎮 Server is up and running on 127.0.0.1:5555...
2. Start Clients (in separate terminals or different machines on the same network)
bash
Copy
Edit
python client.py
Each client opens a game window where they control a block using the arrow keys.

🎨 Features
Smooth player movement with arrow keys

Real-time multiplayer over local network

Color-coded players

Clean and colorful UI

Logging for server actions and connections

🔧 Customization
You can enhance this project by:

Adding obstacles or scoring logic

Supporting more than 2 players

Adding sound effects

Using actual sprites for characters

👨‍💻 Author
Developed by [Arjumand Afreen Tabinda]


📜 License
This project is open-source and free to use for learning and development purposes.