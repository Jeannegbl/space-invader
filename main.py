import pygame
import random
import math
from pygame import mixer

# initializing pygame
pygame.init()

# creating screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,
                                  screen_height))

clock = pygame.time.Clock()

# caption and icon
pygame.display.set_caption("Welcome to Space\
Invaders Game by:- styles")

# Score
score_val = 0
scoreX = 5
scoreY = 5
font = pygame.font.Font('freesansbold.ttf', 20)

# Game Over
game_over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Points: " + str(score_val),
                        True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over():
    game_over_text = game_over_font.render("GAME OVER",
                                           True, (255, 255, 255))
    screen.blit(game_over_text, (190, 250))


# Background Sound
mixer.music.load('data/background.wav')
mixer.music.play(-1)

# player
playerImage = (pygame.transform.scale(pygame.image.load('data/player.png'), (64,64)))
player_X = 370
player_Y = 523
player_Xchange = 0

# Invader
class invader_tab():
    image = []
    x = []
    y = []
    x_change = []
    y_change = []
    nb = 13

for num in range(invader_tab.nb):
    invader_tab.image.append(pygame.transform.scale(pygame.image.load('data/invader.png'), (64, 64)))
    invader_tab.x.append(random.randint(64, 737))
    invader_tab.y.append(random.randint(30, 180))
    invader_tab.x_change.append(1.2)
    invader_tab.y_change.append(50)

# Bullet
# rest - bullet is not moving
# fire - bullet is moving
bulletImage = (pygame.transform.scale(pygame.image.load('data/bullet.png'), (32, 32)))
bullet_X = 0
bullet_Y = 500
bullet_Xchange = 0
bullet_Ychange = 3
bullet_state = "rest"


# Collision Concept
def isCollision(x1, x2, y1, y2):
    distance = math.sqrt((math.pow(x1 - x2, 2)) +
                         (math.pow(y1 - y2, 2)))
    if distance <= 50:
        return True
    else:
        return False


def player(x, y):
    screen.blit(playerImage, (x - 16, y + 10))


def invader(x, y, i):
    screen.blit(invader_tab.image[i], (x, y))


def bullet(x, y):
    global bullet_state
    screen.blit(bulletImage, (x, y))
    bullet_state = "fire"


# game loop
running = True
while running:
    clock.tick(60)

    # RGB
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Controlling the player movement
        # from the arrow keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                player_Xchange = -1.7
            if event.key == pygame.K_d:
                player_Xchange = 1.7
        if event.type == pygame.MOUSEBUTTONDOWN:

            # Fixing the change of direction of bullet
            if bullet_state is "rest":
                bullet_X = player_X
                bullet(bullet_X, bullet_Y)
                bullet_sound = mixer.Sound('data/catch.wav')
                bullet_sound.play()
        if event.type == pygame.KEYUP:
            player_Xchange = 0

    # adding the change in the player position
    player_X += player_Xchange
    for i in range(invader_tab.nb):
        invader_tab.x[i] += invader_tab.x_change[i]

    # bullet movement
    if bullet_Y <= 0:
        bullet_Y = 600
        bullet_state = "rest"
    if bullet_state == "fire":
        bullet(bullet_X, bullet_Y)
        bullet_Y -= bullet_Ychange

    # movement of the invader
    for i in range(invader_tab.nb):

        if invader_tab.y[i] >= 450:
            if abs(player_X - invader_tab.x[i]) < 80:
                for j in range(invader_tab.nb):
                    invader_tab.y[j] = 2000
                    explosion_sound = mixer.Sound('data/death.wav')
                    explosion_sound.play()
                game_over()
                break

        if invader_tab.x[i] >= 735 or invader_tab.x[i] <= 0:
            invader_tab.x_change[i] *= -1
            invader_tab.y[i] += invader_tab.y_change[i]
        # Collision
        collision = isCollision(bullet_X, invader_tab.x[i],
                                bullet_Y, invader_tab.y[i])
        if collision:
            score_val += 1
            bullet_Y = 600
            bullet_state = "rest"
            invader_tab.x[i] = random.randint(64, 736)
            invader_tab.y[i] = random.randint(30, 200)
            invader_tab.x_change[i] *= -1

        invader(invader_tab.x[i], invader_tab.y[i], i)

    # restricting the spaceship so that
    # it doesn't go out of screen
    if player_X <= 16:
        player_X = 16;
    elif player_X >= 750:
        player_X = 750

    player(player_X, player_Y)
    show_score(scoreX, scoreY)
    pygame.display.update()
