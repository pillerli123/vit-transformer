import tkinter as tk
import random

class SnakeGame(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Snake Game")
        self.geometry("400x400")
        self.canvas = tk.Canvas(self, bg="white", width=400, height=400)
        self.canvas.pack()
        self.snake = [(10, 10), (10, 20), (10, 30)]
        self.direction = 'Right'
        self.food = self.generate_food()
        self.food = self.generate_bolock()
        self.game_over = False

        self.bind("<Key>", self.change_direction)
        self.loop()

    def change_direction(self, event):
        if event.keysym == 'Up' and self.direction != 'Down':
            self.direction = 'Up'
        elif event.keysym == 'Down' and self.direction != 'Up':
            self.direction = 'Down'
        elif event.keysym == 'Left' and self.direction != 'Right':
            self.direction = 'Left'
        elif event.keysym == 'Right' and self.direction != 'Left':
            self.direction = 'Right'

    def loop(self):
        if not self.game_over:
            self.move()
            self.canvas.after(150, self.loop)

    def move(self):
        x, y = self.snake[-1]

        if self.direction == 'Up':
            y -= 10
        elif self.direction == 'Down':
            y += 10
        elif self.direction == 'Left':
            x -= 10
        elif self.direction == 'Right':
            x += 10

        if (x, y) in self.snake or x < 0 or x >= 400 or y < 0 or y >= 400:
            self.game_over = True
            return

        self.snake.append((x, y))

        if (x, y) == self.food:
            self.food = self.generate_food()
        else:
            self.snake.pop(0)

        self.canvas.delete("all")
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0] + 10, segment[1] + 10, fill="black")
        self.canvas.create_oval(self.food[0], self.food[1], self.food[0] + 10, self.food[1] + 10, fill="red")

    random.seed(42)
    def generate_food(self):

        x = random.randint(0, 39) * 10
        y = random.randint(0, 39) * 10
        while (x, y) in self.snake:
            x = random.randint(0, 39) * 10
            y = random.randint(0, 39) * 10
        return (x, y)


    # create the bock of the game
    def generate_bolock(self):
        x = random.randint(0, 39) * 10
        y = random.randint(0, 39) * 10
        while (x, y) in self.snake:
            x = random.randint(0, 39) * 10
            y = random.randint(0, 39) * 10
        return (x, y)


if __name__ == "__main__":
    game = SnakeGame()
    game.mainloop()