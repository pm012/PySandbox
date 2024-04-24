import pygame
import random
import os
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

pygame.init()

FPS = pygame.time.Clock()

HEIGHT = 900
WIDTH = 1600

FONT = pygame.font.SysFont('Verdana', 60)

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_RED = (255, 0, 0)
PLAYER_SIZE = (20, 20)

# Dialogue box properties
dialogue_box_width = 400
dialogue_box_height = 200
dialogue_box_x = (WIDTH - dialogue_box_width) // 2
dialogue_box_y = (HEIGHT - dialogue_box_height) // 2
dialogue_box = False

main_display = pygame.display.set_mode((WIDTH, HEIGHT))

bg = pygame.transform.scale(pygame.image.load('Game/res/background.png'), (WIDTH, HEIGHT))
bg_X1 = 0
bg_X2 = bg.get_width()
bg_move = 3

IMAGE_PATH = "Game/res/Goose"
PLAYER_IMAGES = os.listdir(IMAGE_PATH)

player = pygame.image.load('Game/res/player.png').convert_alpha()
player_rect = player.get_rect()
player_move_down = [0, 4]
player_speed_right = [4, 0]
player_speed_up = [0, -4]
player_speed_left = [-4, 0]


def create_enemy():
    enemy = pygame.image.load('Game/res/enemy.png').convert_alpha()
    enemy = pygame.transform.scale(enemy, (100, 35))
    enemy_size = enemy.get_size()
    enemy_rect = pygame.Rect(WIDTH, random.randint(30, HEIGHT - enemy_size[1]), *enemy_size)
    enemy_move = [random.randint(-6, -4), 0]
    return [enemy, enemy_rect, enemy_move]


def create_bonus():
    bonus = pygame.image.load('Game/res/bonus.png').convert_alpha()
    bonus = pygame.transform.scale(bonus, (90, 150))
    bonus_size = bonus.get_size()
    # set starting point -230 for bonuses to make the bounus start moving beyond the playfield edges
    bonus_rect = pygame.Rect(random.randint(0, WIDTH - bonus_size[0]), -230, *bonus_size)
    bonus_move = [0, random.randint(4, 6)]
    return [bonus, bonus_rect, bonus_move]


CREATE_ENEMY = pygame.USEREVENT + 1
CREATE_BONUS = CREATE_ENEMY + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)
pygame.time.set_timer(CREATE_BONUS, 1500)
CHANGE_IMAGE = pygame.USEREVENT + 3
pygame.time.set_timer(CHANGE_IMAGE, 200)

enemies = []
bonuses = []

score = 0
image_index = 0

playing = True

while playing:
    FPS.tick(120)
    # Events handling
    #event = pygame.event.wait()
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False

        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())

        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())

        if event.type == CHANGE_IMAGE:
            player = pygame.image.load(os.path.join(IMAGE_PATH, PLAYER_IMAGES[image_index]))
            image_index += 1
            if image_index >= len(PLAYER_IMAGES):
                image_index = 0

    bg_X1 -= bg_move
    bg_X2 -= bg_move

    if bg_X1 < -bg.get_width():
        bg_X1 = bg.get_width()

    if bg_X2 < -bg.get_width():
        bg_X2 = bg.get_width()

    main_display.blit(bg, (bg_X1, 0))
    main_display.blit(bg, (bg_X2, 0))

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

        if player_rect.colliderect(enemy[1]):
            playing = False

    for bonus in bonuses:
        bonus[1] = bonus[1].move(bonus[2])
        main_display.blit(bonus[0], bonus[1])
        if bonus[1].bottom > HEIGHT:
            bonuses.pop(bonuses.index(bonus))

        # Remove bonus if collide
        if player_rect.colliderect(bonus[1]):
            score += 1
            bonuses.pop(bonuses.index(bonus))

    main_display.blit(FONT.render(str(score), True, COLOR_RED), (WIDTH - 80, 60))
    main_display.blit(player, player_rect)

    pygame.display.flip()
