import tkinter as tk

# Constants for canvas and cell configuration
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 25

class EraserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎨 Eraser Art Canvas")
        self.root.configure(bg="#f0f0f5")

        # Title label
        self.title = tk.Label(root, text="Interactive Eraser Grid", font=("Arial", 18, "bold"), bg="#f0f0f5", fg="#333")
        self.title.pack(pady=10)

        # Canvas setup
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white", bd=2, relief="groove", highlightthickness=0)
        self.canvas.pack(pady=10)

        # Reset button
        self.reset_btn = tk.Button(root, text="🔁 Reset Canvas", font=("Arial", 10, "bold"),
                                   bg="#ffcccc", fg="black", bd=1, relief="solid", command=self.reset_canvas)
        self.reset_btn.pack(pady=5)

        self.cells = {}
        self.create_grid()

        # Eraser initialization
        self.eraser = self.canvas.create_oval(0, 0, ERASER_SIZE, ERASER_SIZE, fill="#ff69b4", outline="black", width=2)

        # Bind events
        self.canvas.bind("<B1-Motion>", self.move_eraser)
        self.canvas.bind("<Motion>", self.hover_effect)

    def create_grid(self):
        """Draw a colorful grid"""
        colors = ["#add8e6", "#87cefa", "#b0e0e6", "#87ceeb"]
        for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
            for col in range(0, CANVAS_WIDTH, CELL_SIZE):
                color = colors[(row + col) // CELL_SIZE % len(colors)]
                cell = self.canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill=color, outline="gray")
                self.cells[(col, row)] = cell

    def move_eraser(self, event):
        """Move eraser and erase touched cells"""
        x, y = event.x, event.y
        self.canvas.coords(self.eraser, x - ERASER_SIZE/2, y - ERASER_SIZE/2, x + ERASER_SIZE/2, y + ERASER_SIZE/2)
        self.erase_cells(x, y)

    def hover_effect(self, event):
        """Subtle animation effect for eraser movement"""
        self.canvas.coords(self.eraser, event.x - ERASER_SIZE/2, event.y - ERASER_SIZE/2, event.x + ERASER_SIZE/2, event.y + ERASER_SIZE/2)

    def erase_cells(self, x, y):
        """Erase overlapping grid cells"""
        for (col, row), cell in self.cells.items():
            if (col < x + ERASER_SIZE/2 and col + CELL_SIZE > x - ERASER_SIZE/2 and
                row < y + ERASER_SIZE/2 and row + CELL_SIZE > y - ERASER_SIZE/2):
                self.canvas.itemconfig(cell, fill="white")

    def reset_canvas(self):
        """Reset the canvas to original state"""
        for cell in self.cells.values():
            self.canvas.itemconfig(cell, fill="#add8e6")  # Reset to default color


def main():
    root = tk.Tk()
    app = EraserApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
