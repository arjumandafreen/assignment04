import random
import tkinter as tk
from tkinter import messagebox
import time

class Minesweeper:
    def __init__(self, size=5, bombs=3):
        self.size = size
        self.bombs = bombs
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.bomb_positions = set()
        self.revealed = set()
        self.flagged = set()
        self.start_time = None

        # Tkinter window
        self.root = tk.Tk()
        self.root.title("💣 Minesweeper Game")
        self.root.configure(bg="#f0f0f0")

        self.buttons = {}
        self.timer_label = tk.Label(self.root, text="Time: 0", font=('Helvetica', 14, 'bold'), bg="#f0f0f0")
        self.timer_label.grid(row=self.size, columnspan=self.size, pady=10)

        # Difficulty Dropdown
        self.difficulty_var = tk.StringVar(self.root)
        self.difficulty_var.set("Easy")
        difficulty_menu = tk.OptionMenu(self.root, self.difficulty_var, "Easy", "Medium", "Hard", command=self.change_difficulty)
        difficulty_menu.config(font=("Helvetica", 12), bg="#e0e0e0")
        difficulty_menu.grid(row=self.size + 1, columnspan=self.size, pady=5)

        # Game buttons
        for row in range(self.size):
            for col in range(self.size):
                button = tk.Button(self.root, text=" ", width=4, height=2, font=('Helvetica', 12, 'bold'),
                                   bg="#d0d0d0", relief="raised", 
                                   command=lambda r=row, c=col: self.reveal(r, c))
                button.grid(row=row, column=col, padx=1, pady=1)
                self.buttons[(row, col)] = button

        # Reset button
        self.reset_button = tk.Button(self.root, text="🔄 Reset Game", font=('Helvetica', 12, 'bold'),
                                      bg="#4CAF50", fg="white", command=self.reset_game)
        self.reset_button.grid(row=self.size + 2, columnspan=self.size, pady=10)

        self.play_sound('start')
        self._place_bombs()

    def play_sound(self, action):
        sounds = {
            'start': 'start_sound.mp3',
            'click': 'click_sound.mp3',
            'bomb': 'bomb_sound.mp3',
            'win': 'win_sound.mp3',
            'lose': 'lose_sound.mp3',
        }
        if action in sounds:
            print(f"Playing sound: {sounds[action]}")

    def _place_bombs(self):
        self.bomb_positions.clear()
        while len(self.bomb_positions) < self.bombs:
            r, c = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            self.bomb_positions.add((r, c))

    def _count_adjacent_bombs(self, r, c):
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),           (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]
        return sum((r+dr, c+dc) in self.bomb_positions for dr, dc in directions)

    def reveal(self, r, c):
        if not self.start_time:
            self.start_time = time.time()

        if (r, c) in self.flagged or (r, c) in self.revealed:
            return

        if (r, c) in self.bomb_positions:
            self.play_sound('bomb')
            self.buttons[(r, c)].config(bg="red", text="💣", disabledforeground='black')
            self.end_game("Game Over", "💣 You hit a bomb!")
            return

        self.revealed.add((r, c))
        bomb_count = self._count_adjacent_bombs(r, c)
        self.board[r][c] = str(bomb_count) if bomb_count > 0 else ' '

        button = self.buttons[(r, c)]
        colors = ['#f0f0f0', 'blue', 'green', 'red', 'purple', 'maroon', 'turquoise', 'black', 'gray']
        button.config(text=self.board[r][c], state="disabled", relief="sunken",
                      bg="#b3e0ff", disabledforeground=colors[bomb_count])

        if bomb_count == 0:
            for dr, dc in [(-1, -1), (-1, 0), (-1, 1),
                           (0, -1),           (0, 1),
                           (1, -1),  (1, 0),  (1, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < self.size and 0 <= nc < self.size:
                    self.reveal(nr, nc)

        if len(self.revealed) == (self.size ** 2 - self.bombs):
            self.play_sound('win')
            elapsed_time = int(time.time() - self.start_time)
            self.end_game("Congratulations!", f"🎉 You cleared the board in {elapsed_time} seconds!")

        self.update_timer()

    def update_timer(self):
        if self.start_time:
            elapsed_time = int(time.time() - self.start_time)
            self.timer_label.config(text=f"Time: {elapsed_time}")
        self.root.after(1000, self.update_timer)

    def end_game(self, title, message):
        messagebox.showinfo(title, message)
        self.root.quit()

    def reset_game(self):
        self.size, self.bombs = self._get_difficulty_params()
        self.board = [[' ' for _ in range(self.size)] for _ in range(self.size)]
        self.bomb_positions = set()
        self.revealed = set()
        self.flagged = set()
        self._place_bombs()
        self.start_time = None
        self.timer_label.config(text="Time: 0")

        for (r, c) in self.buttons:
            self.buttons[(r, c)].grid_forget()

        self.buttons = {}
        for row in range(self.size):
            for col in range(self.size):
                button = tk.Button(self.root, text=" ", width=4, height=2, font=('Helvetica', 12, 'bold'),
                                   bg="#d0d0d0", relief="raised",
                                   command=lambda r=row, c=col: self.reveal(r, c))
                button.grid(row=row, column=col, padx=1, pady=1)
                self.buttons[(row, col)] = button

        self.timer_label.grid(row=self.size, columnspan=self.size, pady=10)
        self.reset_button.grid(row=self.size + 2, columnspan=self.size, pady=10)
        self.play_sound('start')

    def change_difficulty(self, difficulty):
        if difficulty == "Easy":
            self.size, self.bombs = 5, 5
        elif difficulty == "Medium":
            self.size, self.bombs = 8, 12
        else:
            self.size, self.bombs = 10, 20
        self.reset_game()

    def _get_difficulty_params(self):
        diff = self.difficulty_var.get()
        return (5, 5) if diff == "Easy" else (8, 12) if diff == "Medium" else (10, 20)

    def play(self):
        self.update_timer()
        self.root.mainloop()

# Start the game
game = Minesweeper()
game.play()
