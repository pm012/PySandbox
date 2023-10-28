import pygame
import random
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

pygame.init()

FPS = pygame.time.Clock()

HEIGHT = 800
WIDTH = 1200

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_RED = (255, 0, 0)
PLAYER_SIZE = (20, 20)

main_display = pygame.display.set_mode((WIDTH, HEIGHT))

player = pygame.Surface(PLAYER_SIZE)
player.fill(COLOR_WHITE)
player_rect = player.get_rect()
# player_speed = [1, 1]
player_move_down = [0, 1]
player_speed_right = [1, 0]
player_speed_up = [0, -1]
player_speed_left = [-1, 0]


def create_enemy():
    enemy_size = (30, 30)
    enemy = pygame.Surface(enemy_size)
    enemy.fill(COLOR_BLUE)
    enemy_rect = pygame.Rect(WIDTH, random.randint(0, HEIGHT - enemy_size[1]), *enemy_size)
    enemy_move = [random.randint(-6, -1), 0]
    return [enemy, enemy_rect, enemy_move]


def create_bonus():
    bonus_size = (25, 25)
    bonus = pygame.Surface(bonus_size)
    bonus.fill(COLOR_RED)
    bonus_rect = pygame.Rect(random.randint(0, WIDTH - bonus_size[0]), 0, *bonus_size)
    bonus_move = [0, random.randint(1, 5)]
    return [bonus, bonus_rect, bonus_move]


CREATE_ENEMY = pygame.USEREVENT + 1
CREATE_BONUS = CREATE_ENEMY + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)
pygame.time.set_timer(CREATE_BONUS, 1500)

enemies = []
bonuses = []

plaing = True

while plaing:
    FPS.tick(120)

    for event in pygame.event.get():
        if event.type == QUIT:
            plaing = False

        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())

        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())

    main_display.fill(COLOR_BLACK)
    """ if (player_rect.bottom >= HEIGHT) or (player_rect.top < 0):
        player_speed[1] = -player_speed[1]

    if (player_rect.right >= WIDTH) or (player_rect.left < 0):
        player_speed[0] = -player_speed[0]       """

    keys = pygame.key.get_pressed()
    if keys[K_DOWN] and player_rect.bottom < HEIGHT:
        player_rect = player_rect.move(player_move_down)

    if keys[K_RIGHT] and player_rect.right < WIDTH:
        player_rect = player_rect.move(player_speed_right)

    if keys[K_UP] and player_rect.top > 0:
        player_rect = player_rect.move(player_speed_up)

    if keys[K_LEFT] and player_rect.left > 0:
        player_rect = player_rect.move(player_speed_left)

    for enemy in enemies:
        enemy[1] = enemy[1].move(enemy[2])
        main_display.blit(enemy[0], enemy[1])
        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))

    for bonus in bonuses:
        bonus[1] = bonus[1].move(bonus[2])
        main_display.blit(bonus[0], bonus[1])
        if bonus[1].bottom > HEIGHT:
            bonuses.pop(bonuses.index(bonus))

    # enemy_rect = enemy_rect.move(enemy_move)

    main_display.blit(player, player_rect)
    # main_display.blit(enemy, enemy_rect)
    # player_rect = player_rect.move(player_speed)
    print("bonuses:" + str(len(bonuses)))

    pygame.display.flip()
