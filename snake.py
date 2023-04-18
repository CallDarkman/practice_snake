import sys

import pygame
import random

from pygame.locals import QUIT

# 初始化pygame
pygame.init()

# 设置游戏界面的大小
WIDTH = 600
HEIGHT = 600
# 创建游戏窗口
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# 设置窗口标题
pygame.display.set_caption('肖总的贪吃蛇')
# 设置游戏界面的背景颜色
BACKGROUND_COLOR = (0, 0, 0)  # 黑色

# 绘制游戏界面
screen.fill(BACKGROUND_COLOR)
# 刷新速度
clock = pygame.time.Clock()
# 设置蛇和食物的大小
SIZE = 10
# 设置蛇和食物的颜色
SNAKE_COLOR = (0, 255, 0)  # 绿色
FOOD_COLOR = (255, 0, 0)  # 红色
# 假设蛇的身体由一系列坐标组成，存储在列表snake中
# 初始时，蛇的长度为3，位于游戏界面的中央
snake = [(300, 300), (310, 300), (320, 300)]
weiba = []

# 随机生成食物的位置
food = (random.randint(0, WIDTH-SIZE)//SIZE*SIZE, random.randint(0, HEIGHT-SIZE)//SIZE*SIZE)
# 绘制蛇
for x, y in snake:
    # 在(x,y)处绘制一个SIZE*SIZE的矩形表示蛇的身体
    pygame.draw.rect(screen, SNAKE_COLOR, (x, y, SIZE, SIZE))

# 绘制食物
# 在food处绘制一个SIZE*SIZE的矩形表示食物
pygame.draw.rect(screen, FOOD_COLOR, (food[0], food[1], SIZE, SIZE))

# 更新游戏界面
pygame.display.update()

# 设置蛇移动的初始方向
jishuqi = 1
shuliang = 1
FPS = 30
SPEED = 5
speed = 10 - SPEED
direction_chushi = ['UP', 'DOWN', 'LEFT']
direction = random.choice(direction_chushi)
# direction = 'LEFT'
new_direction = None
score = 0
food_count = 0
def game_over():
    global snake
    global direction
    global speed
    global jishuqi
    global shuliang
    screen.fill(BACKGROUND_COLOR)
    # 显示得分
    font = pygame.font.Font(None, 36)
    text = font.render(f'Score: {score}', True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (WIDTH // 2, HEIGHT // 2)
    screen.blit(text, text_rect)

    # 显示重新开始的选项
    text = font.render('Press SPACE to restart', True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (WIDTH // 2, HEIGHT // 2 + 50)
    screen.blit(text, text_rect)
    tuichu = True
    # 更新游戏界面
    pygame.display.update()
    # 处理用户输入
    while tuichu:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        # if event.type == QUIT:
        #     sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    snake = [(300, 300), (310, 300), (320, 300)]
                    direction_chushi = ['UP', 'DOWN', 'LEFT']
                    direction = random.choice(direction_chushi)
                    speed = SPEED
                    jishuqi = 1
                    shuliang = 1
                    tuichu = False


# 假设蛇的身体由一系列坐标组成，存储在列表snake中
# 假设direction为蛇移动的方向，可以取值为'UP'、'DOWN'、'LEFT'、'RIGHT'
# 处理用户输入
while True:
    pygame.display.update()
    head = (snake[0][0], snake[0][1])# clock.tick(1)
    new_head = (snake[0][0], snake[0][1])
    clock.tick(FPS)
    b = False
    if jishuqi >60:
        jishuqi = 1
        jishuqi += 1
    else:
        jishuqi += 1
    if jishuqi % speed == 0:
        b = True
    screen.fill(BACKGROUND_COLOR)

    if direction == 'UP':
            new_head = (snake[0][0], snake[0][1] - SIZE)
            head = new_head
    elif direction == 'DOWN':
            new_head = (snake[0][0], snake[0][1] + SIZE)
            head = new_head
    elif direction == 'LEFT':
            new_head = (snake[0][0] - SIZE, snake[0][1])
            head = new_head
    elif direction == 'RIGHT':
            new_head = (snake[0][0] + SIZE, snake[0][1])
            head = new_head
    # direction2 = new_direction
    w = snake[0][1] - SIZE
    s = snake[0][1] + SIZE
    a = snake[0][0] - SIZE
    d = snake[0][0] + SIZE
    # 处理用户输入
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and w != snake[1][1]:
                new_direction = 'UP'
            elif event.key == pygame.K_DOWN and s != snake[1][1]:
                new_direction = 'DOWN'
            elif event.key == pygame.K_LEFT and a != snake[1][0]:
                new_direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and d != snake[1][0]:
                new_direction = 'RIGHT'
        # 根据方向移动蛇头
    # if new_direction == direction:
    #         new_head = head
    if jishuqi % speed == 0:
        b = True
    if new_direction == 'UP':# and w != snake[1][1]:
            new_head = (snake[0][0], snake[0][1] - SIZE)
            head = new_head
    elif new_direction == 'DOWN':# and s != snake[1][1]:
            new_head = (snake[0][0], snake[0][1] + SIZE)
            head = new_head
    elif new_direction == 'LEFT':# and a != snake[1][0]:
            new_head = (snake[0][0] - SIZE, snake[0][1])
            head = new_head
    elif new_direction == 'RIGHT':# and d != snake[1][0]:
            new_head = (snake[0][0] + SIZE, snake[0][1])
            head = new_head


# 将新的蛇头添加到蛇身体的开头
    if b:
        snake.insert(0, head)

# 删除蛇尾（如果蛇没有吃到食物）
        snake.pop()
        # weiba = snake.pop()
# 检测蛇是否吃到食物
    weiba = [snake[-1][0],snake[-1][1]]
    if snake[0] == food:
        # 增加蛇的长度
        snake.append(weiba)
        # 随机生成新的食物位置
        food = (random.randint(0, WIDTH-SIZE)//SIZE*SIZE, random.randint(0, HEIGHT-SIZE)//SIZE*SIZE)
        # 增加食物计数器
        food_count += 1
        score += 1
        # 每吃到3个食物，增加蛇的移动速度
        if food_count % shuliang == 0:
            if speed > 1:
                speed -= 1
                food_count = 0
                shuliang += 1

    for x, y in snake:
        pygame.draw.rect(screen, SNAKE_COLOR, (x, y, SIZE, SIZE))
    pygame.draw.rect(screen, FOOD_COLOR, (food[0], food[1], SIZE, SIZE))
        # pygame.display.update()

    # 检测蛇是否撞到墙壁
    if snake[0][0] < 0 or snake[0][0] >= WIDTH or snake[0][1] < 0 or snake[0][1] >= HEIGHT:
        # 游戏结束
        game_over()

    # # 检测蛇是否撞到自己的身体
    for block in snake[1:]:
        if block == snake[0]:
            # 游戏结束
            game_over()

    pygame.display.update()
    #
    # # 重新绘制游戏界面
    # screen.fill(BACKGROUND_COLOR)
    # # 假设score为游戏得分
    # score = 0





