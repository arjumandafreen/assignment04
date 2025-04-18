# 🎲 Magical Dice Roller 🎲

Welcome to the **Magical Dice Roller**, a simple and fun Python-based terminal app that simulates the rolling of two dice and adds a colorful twist to your luck!

## 🌟 Purpose of the App

The goal of this app is to provide a fun and engaging way to simulate the rolling of two six-sided dice. Using colorful terminal output, it adds personality and excitement to each roll, with reactions based on the total.

Whether you're just testing your luck or looking for a quick break, this app is perfect for a little fun in the terminal.

## 💻 How It Works

- When run, the app simulates the rolling of two dice using Python's `random` module.
- It displays each die's result with colorful, animated feedback using the `colorama` library.
- Based on the total of the dice, it gives different reactions:
  - 🎉 **Double sixes (12)**: Jackpot!
  - 😲 **Snake Eyes (2)**: Tough luck!
  - 🍀 **Lucky numbers (7 or 11)**: Feeling lucky!
  - 🔁 **Any other total**: Try your luck again!

## 🛠️ Requirements

- Python 3.x
- [`colorama`](https://pypi.org/project/colorama/) for colorful terminal output

### Install dependencies

```bash
pip install colorama
▶️ How to Run

python main.py