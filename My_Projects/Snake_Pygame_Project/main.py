import random
import pygame
from pygame_widgets import Button

pygame.init()

new_game = False

root_bg_color = (51, 153, 0)
snake_body_color = (153, 255, 102)
snake_head_color = (17, 51, 0)
apple_color = (255, 0, 0)
root_dimensions = (600, 600)

score_color = (255, 255, 51)
score_count = 0
best_score = 0
score_font = pygame.font.Font("fonts/atari.ttf", 15)
game_over_font = pygame.font.Font("fonts/atari.ttf", 50)
game_over_score_font = pygame.font.Font("fonts/atari.ttf", 20)

x = 300
y = 300
snake_list = [[x, y]]

d = 20
dx = 0
dy = 0
x_apple = round(random.randrange(0, 600 - d) / 20) * 20
y_apple = round(random.randrange(0, 600 - d) / 20) * 20

root = pygame.display.set_mode(root_dimensions)
root.fill(root_bg_color)
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

pygame.mixer.music.load("sound/game_music.wav")
pygame.mixer.music.play(-1)

apple_eat_sound = pygame.mixer.Sound("sound/apple_eat.wav")
game_over_sound = pygame.mixer.Sound("sound/game_over.wav")

def snake_draw(snake_list):
    root.fill(root_bg_color)
    head = snake_list[-1]

    if len(snake_list) > 1:
        body = snake_list.copy()
        del body[-1]

        for position in body:
            pygame.draw.rect(root, snake_body_color, [position[0], position[1], d, d])

    pygame.draw.rect(root, snake_head_color, [head[0], head[1], d, d])


def snake_move(dx, dy, snake_list):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -d
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = d
                dy = 0
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -d
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = d
        elif event.type == pygame.QUIT:
                pygame.quit()
                quit()

    x_new = snake_list[-1][0] + dx
    y_new = snake_list[-1][1] + dy

    snake_list.append([x_new, y_new])

    del snake_list[0]

    return dx, dy, snake_list


def apple_collision_check(dx, dy, x_apple, y_apple, snake_list):
    head = snake_list[-1]
    x_new = head[0] + dx
    y_new = head[1] + dy


    if head[0] == x_apple and head[1] == y_apple:
        snake_list.append([x_new, y_new])
        x_apple = round(random.randrange(0, 600 - d) / 20) * 20
        y_apple = round(random.randrange(0, 600 - d) / 20) * 20
        apple_eat_sound.play()

    pygame.draw.rect(root, apple_color, [x_apple, y_apple, d, d])
    return x_apple, y_apple, snake_list


def wall_collision_check(snake_list):
    head = snake_list[-1]
    x = head[0]
    y = head[1]

    if x not in range(600) or y not in range(600):
        end_game()


def body_collision_check(snake_list):
    head = snake_list[-1]
    body = snake_list.copy()
    del body[-1]

    for x,y in body:
        if x == head[0] and y == head[1]:
            end_game()


def score_update(snake_list):
    global score_count, best_score
    score_count = len(snake_list) - 1
    score = score_font.render(f'Score: {score_count:04}',  True, score_color)
    game_best_score = score_font.render(f'Best: {best_score:04}',  True, snake_head_color)
    root.blit(score, [5, 5])
    root.blit(game_best_score, [455, 5])


def end_game():
    global score_count, best_score, new_game
    pygame.mixer.music.pause()
    game_over_sound.play()
    root.fill(root_bg_color)
    if int(score_count) > int(best_score):
        best_score = score_count
    game_over_message = game_over_font.render('GAME OVER', True, (0, 0, 0))
    game_over_score = game_over_score_font.render(f'SCORE : {score_count:04}', True, (0, 0, 0))
    game_best_score = game_over_score_font.render(f'BEST : {best_score:04}', True, (0, 0, 0))
    root.blit(game_over_message, [80, 150])
    root.blit(game_over_score, [200, 250])
    root.blit(game_best_score, [210, 310])

    restart_button = Button(
                        root, 80, 400, 200, 40, text='New Game',
                        font=pygame.font.Font("fonts/atari.ttf", 15),
                        fontSize=30,
                        inactiveColour=(0, 0, 0),
                        pressedColour=(0, 255, 0),
                        textColour=(255, 255, 255),
                        onClick=lambda: game_restart()
                        )
    exit_button = Button(
                        root, 320, 400, 200, 40, text='Exit Game',
                        font=pygame.font.Font("fonts/atari.ttf", 15),
                        fontSize=30,
                        inactiveColour=(0, 0, 0),
                        pressedColour=(0, 255, 0),
                        textColour=(255, 255, 255),
                        onClick=lambda: pygame.quit()
                        )

    run = True
    while run:
        events = pygame.event.get()
        restart_button.listen(events)
        exit_button.listen(events)
        restart_button.draw()
        exit_button.draw()
        if new_game:
            root.fill(root_bg_color)
            new_game = False
            run = False
            pygame.mixer.music.play()

        pygame.display.update()


def game_restart():
    global new_game, score_count, snake_list
    new_game = True
    snake_list = [[300, 300]]
    score_count = 0


while True:
    snake_draw(snake_list)
    score_update(snake_list)
    dx, dy, snake_list = snake_move(dx, dy, snake_list)
    x_apple, y_apple, snake_list = apple_collision_check(dx, dy, x_apple, y_apple, snake_list)
    body_collision_check(snake_list)
    wall_collision_check(snake_list)
    pygame.display.update()
    clock.tick(6)

