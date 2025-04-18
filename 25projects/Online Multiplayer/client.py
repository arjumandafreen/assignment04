import socket
import pygame
import pickle
import threading

# Socket setup
host = '127.0.0.1'
port = 5555
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

# Initialize Pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🌈 Simple Online Multiplayer Game")

# Fonts
font = pygame.font.SysFont("comicsans", 20)

# Colors
BACKGROUND_COLOR = (30, 30, 60)
PLAYER_COLORS = [(255, 0, 0), (0, 200, 255), (0, 255, 0), (255, 255, 0)]
BORDER_COLOR = (255, 255, 255)

# Player class
class Player:
    def __init__(self, x, y, color, name="You"):
        self.x = x
        self.y = y
        self.color = color
        self.velocity = 5
        self.name = name

    def draw(self, surface):
        pygame.draw.rect(surface, BORDER_COLOR, (self.x - 2, self.y - 2, 54, 54), border_radius=8)
        pygame.draw.rect(surface, self.color, (self.x, self.y, 50, 50), border_radius=6)
        name_text = font.render(self.name, True, (255, 255, 255))
        surface.blit(name_text, (self.x, self.y - 20))

# Create player
player = Player(100, 100, PLAYER_COLORS[0])

# Send player data
def send_data():
    try:
        players_data = pickle.dumps([player])
        client.send(players_data)
    except:
        pass

# Receive data from server
def receive_data():
    global player
    while True:
        try:
            data = client.recv(2048)
            players = pickle.loads(data)
            if len(players) > 0:
                draw_window(players)
        except:
            pass

# Main loop
def update():
    running = True
    clock = pygame.time.Clock()

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x -= player.velocity
        if keys[pygame.K_RIGHT]:
            player.x += player.velocity
        if keys[pygame.K_UP]:
            player.y -= player.velocity
        if keys[pygame.K_DOWN]:
            player.y += player.velocity

        send_data()

    pygame.quit()

# Draw players on screen
def draw_window(players):
    win.fill(BACKGROUND_COLOR)
    for i, pdata in enumerate(players):
        p = pdata['player']
        color = PLAYER_COLORS[i % len(PLAYER_COLORS)]
        temp_player = Player(p.x, p.y, color, f"Player {i + 1}")
        temp_player.draw(win)
    pygame.display.update()

# Start receive thread
receive_thread = threading.Thread(target=receive_data)
receive_thread.start()

# Start main loop
update()
