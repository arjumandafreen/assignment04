import socket
import threading
import pickle

# Server setup
HOST = '127.0.0.1'
PORT = 5555
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

players = []

# Define Player object
class Player:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

# Handle communication with individual clients
def handle_client(client, player_obj):
    global players
    while True:
        try:
            data = client.recv(2048)
            if not data:
                break
            players = pickle.loads(data)
            send_to_clients()
        except Exception as e:
            print(f"[⚠️] Connection error: {e}")
            break
    client.close()

# Send updated data to all clients
def send_to_clients():
    for player_data in players:
        for client in player_data['clients']:
            try:
                data = pickle.dumps(players)
                client.send(data)
            except Exception as e:
                print(f"[❌] Failed to send data to client: {e}")

# Start accepting clients
def start():
    print("🎮 Server is up and running on {}:{}...".format(HOST, PORT))
    while True:
        client, address = server.accept()
        print(f"[✅] New connection established: {address}")

        # Alternate player colors
        if len(players) % 2 == 0:
            new_player = Player(100, 100, (255, 0, 0))  # Red
        else:
            new_player = Player(200, 100, (0, 255, 0))  # Green

        players.append({'player': new_player, 'clients': [client]})

        thread = threading.Thread(target=handle_client, args=(client, new_player))
        thread.start()
        print(f"[🧵] Started thread for player {len(players)}")

# Run server
if __name__ == "__main__":
    start()
