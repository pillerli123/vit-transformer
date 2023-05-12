import tkinter as tk
import random
import re

random.seed(42)


import numpy as np
import pyautogui
import threading
import cv2

class SnakeGame(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Snake Game")
        self.geometry("400x400")
        ## interface size
        self.canvas = tk.Canvas(self, bg="white", width=400, height=400)

        self.canvas.pack()
        # intite the snake length
        self.snake = [(10, 10), (10, 20), (10, 30)]
        self.check=[(170, 150), (140, 80), (60, 340), (50, 370), (270, 20), (10, 50), (130, 140), (320, 380), (10, 350), (120, 340), (260, 140), (280, 370), (170, 0), (100, 270), (210, 170), (90, 130), (210, 60), (50, 240), (60, 220), (220, 380), (160, 20), (290, 340), (70, 240), (50, 350), (180, 390), (230, 360), (120, 40), (20, 140), (180, 50), (140, 60), (240, 170), (290, 230), (100, 230), (220, 130), (170, 40), (380, 100), (340, 150), (100, 290), (240, 170), (350, 140), (200, 30), (140, 20), (200, 250), (170, 40), (130, 360), (200, 130), (310, 250), (290, 90), (160, 80), (150, 350)]

        # intite the snack direction
        self.direction = 'Right'
        # intite the generate the food
    
        self.food = self.generate_food()
        # intite the genereate the blocks
        self.blocks = self.generate_blocks()
        # intite the game not over
        self.game_over = False


        # 创建一个四字符代码的视频编码格式
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        # 创建 VideoWriter 对象
        self.out = cv2.VideoWriter('output.avi', self.fourcc, 3.0, (400, 400))



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
            self.update()
            self.move()
            self.capture_frame()
            self.canvas.after(150, self.loop)
        else:
            self.out.release()

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

        if (x, y) in self.snake or x < 0 or x >= 400 or y < 0 or y >= 400 or (x, y) in self.blocks:
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


        # 绘制障碍物
        for block in self.blocks:
            # print(block)
            self.canvas.create_rectangle(block[0], block[1], block[0] + 10, block[1] + 10, fill="blue")
        self.canvas.create_oval(self.food[0], self.food[1], self.food[0] + 10, self.food[1] + 10, fill="red")

    def generate_food(self):
        '''
        random the food position
        :return:
        '''
        x = random.randint(0, 39) * 10  # beacuse this size is 400 ,so , (0-39)*10
        y = random.randint(0, 39) * 10
        # if the random is in the sanke ,re-setting the (x,y)
        while (x, y) in self.snake or (x,y) in self.check:
            x = random.randint(0, 39) * 10
            y = random.randint(0, 39) * 10


        return (x, y)




    def generate_blocks(self):
        blocks=[]

        # a=(140, 80)
        # b=(140, 88)
        # c=(140, 96)
        # d=(140, 104)
        # blocks.append(a)
        # blocks.append(b)
        # blocks.append(c)0
        # blocks.append(d)
        # blocks = []
        # genate the randmo number
        for _ in range(50):   # set 10, 30,
            x = random.randint(0, 39) * 10
            y = random.randint(0, 39) * 10
            # while (x,y ) not in the sanke and not  generate in the food.
            while (x, y) in self.snake or (x, y) in self.food:
                x = random.randint(0, 39) * 10
                y = random.randint(0, 39) * 10
            blocks.append((x, y))

        return blocks

    def capture_frame(self):
        # 捕获屏幕
        geometry=self.winfo_geometry()
        width, height, x, y = map(int, re.findall(r'\d+', geometry))


        # 捕获窗口
        img = pyautogui.screenshot(region=(x, y, width, height))

        # 将图片转换为numpy数组
        frame = np.array(img)

        # 将BGR图像转化为RGB图像
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # 写入帧
        self.out.write(frame)








# start game
def start_game():
    game = SnakeGame()
    game.mainloop()





if __name__ == '__main__':
    start_game()




