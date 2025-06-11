import pygame as pg
from random import *

def set_defauld_values():
    # x, y, apple_x, apple_y, direction, score, snake
    return 200, 320, 400, 120, "right", 0, [[200, 320],[200, 320]]
def check_end_game(x, y, snake):
    if x < 0 or x >= 800 or y >= 480 or y < 0:
        return True
    elif len(snake) > 4 and snake[-1] in snake[:-1]:
        return True
    else:
        return False

pg.init()
disp = pg.display.set_mode((800, 480))
pg.display.set_caption("Snake")
pg.display.update()

GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
VL = (125, 0, 125)

apple_img = pg.image.load("images\\apple.png")
body3_img = pg.image.load("images\\body3.png")
heard2_img = pg.image.load("images\\heard2.png")

game_over = False
clock = pg.time.Clock()
font = pg.font.Font(None, 40)
direction = "right"

x = 200
y = 320
apple_x = 400
apple_y = 120
score = 0
snake = [(x - 40, y), (x, y)]
best_score = 0

while not game_over:
    clock.tick(5)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_over = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT and direction != "right":
                direction = "left"
            if event.key == pg.K_RIGHT and direction != "left":
                direction = "right"
            if event.key == pg.K_UP and direction != "down":
                direction = "up"
            if event.key == pg.K_DOWN and direction != "up":
                direction = "down"
    if direction == "left":
        x -= 40
    if direction == "right":
        x += 40
    if direction == "up":
        y -= 40
    if direction == "down":
        y += 40

    for i in range(len(snake) - 1):
        snake[i] = snake[i + 1]
    snake[-1] = [x, y]


    if x == apple_x and y == apple_y:
        snake = [snake[0]] + snake
        score += 1
        while [apple_x, apple_y] in snake:
            apple_x = randint(1, 19) * 40
            apple_y = randint(1, 11) * 40

    if check_end_game(x, y, snake):
        # game_over = True
        if score > best_score:
            best_score = score
        x, y, apple_x, apple_y, direction, score, snake = set_defauld_values()
        mess = font.render("Ты проиграл", True, VL)
        disp.blit(mess, [300, 240])
        pg.display.update()
        pg.time.delay(1000)
        # break[200, 320]
        continue

    disp.fill(BLACK)
    for i in range(len(snake) - 1):
        #pg.draw.rect(disp, GREEN, [snake[i][0], snake[i][1], 40, 40])
        disp.blit(body3_img, snake[i])
    if direction == "up":
        disp.blit(heard2_img, [x, y])
    if direction == "left":
        disp.blit(pg.transform.rotate(heard2_img, 90), [x, y])
    if direction == "down":
        disp.blit(pg.transform.rotate(heard2_img, 180), [x, y])
    if direction == "right":
        disp.blit(pg.transform.rotate(heard2_img, 270), [x, y])
    #pg.draw.rect(disp, RED, (apple_x, apple_y, 40, 40))
    disp.blit(apple_img, [apple_x, apple_y])


    #mess = font.render("Счет: " + str(score) + "  лучший счет: " + str(best_score), True, VL)
    mess = f"Счет: {score}    Лучший счет: {best_score}"
    messsange = font.render(mess, True, VL)
    disp.blit(messsange, [0, 0])
    pg.display.update()
pg.quit()
quit()