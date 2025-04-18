import numpy as np
import pygame
import sys

# Constants
ROW_COUNT, COL_COUNT = 6, 7
SQUARE_SIZE = 100
RADIUS = SQUARE_SIZE // 2 - 5
WIDTH, HEIGHT = COL_COUNT * SQUARE_SIZE, (ROW_COUNT + 1) * SQUARE_SIZE
WHITE, BLUE, RED, YELLOW = (255, 255, 255), (0, 0, 255), (255, 0, 0), (255, 255, 0)

# Initialize Pygame
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect Four")
font = pygame.font.SysFont("monospace", 75)

# Create the game board
def create_board():
    return np.zeros((ROW_COUNT, COL_COUNT))

# Drop a piece into the board
def drop_piece(board, row, col, piece):
    board[row][col] = piece

# Check if a column is valid for a move
def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0

# Get the next open row in a column
def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

# Check for a winning move
def winning_move(board, piece):
    # Check horizontal, vertical, and diagonal win conditions
    for c in range(COL_COUNT - 3):
        for r in range(ROW_COUNT):
            if all(board[r][c + i] == piece for i in range(4)):
                return True

    for c in range(COL_COUNT):
        for r in range(ROW_COUNT - 3):
            if all(board[r + i][c] == piece for i in range(4)):
                return True

    for c in range(COL_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if all(board[r + i][c + i] == piece for i in range(4)):
                return True

    for c in range(COL_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if all(board[r - i][c + i] == piece for i in range(4)):
                return True

    return False

# Draw the board and the pieces
def draw_board(board):
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(win, BLUE, (c * SQUARE_SIZE, (r + 1) * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.circle(win, WHITE, (c * SQUARE_SIZE + SQUARE_SIZE // 2, (r + 1) * SQUARE_SIZE + SQUARE_SIZE // 2), RADIUS)

    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(win, RED, (c * SQUARE_SIZE + SQUARE_SIZE // 2, HEIGHT - r * SQUARE_SIZE - SQUARE_SIZE // 2), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(win, YELLOW, (c * SQUARE_SIZE + SQUARE_SIZE // 2, HEIGHT - r * SQUARE_SIZE - SQUARE_SIZE // 2), RADIUS)

    pygame.display.update()

# Main game loop
def game():
    board = create_board()
    game_over = False
    turn = 0
    draw_board(board)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(win, WHITE, (0, 0, WIDTH, SQUARE_SIZE))
                posx = event.pos[0]
                color = RED if turn == 0 else YELLOW
                pygame.draw.circle(win, color, (posx, SQUARE_SIZE // 2), RADIUS)
                pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(win, WHITE, (0, 0, WIDTH, SQUARE_SIZE))
                posx = event.pos[0]
                col = posx // SQUARE_SIZE

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    piece = 1 if turn == 0 else 2
                    drop_piece(board, row, col, piece)

                    if winning_move(board, piece):
                        winner_color = RED if piece == 1 else YELLOW
                        text = font.render(f"Player {piece} Wins!", True, winner_color)
                        win.blit(text, (40, 10))
                        pygame.display.update()
                        pygame.time.wait(3000)
                        game_over = True

                    draw_board(board)
                    turn ^= 1  # Switch turns

game()
