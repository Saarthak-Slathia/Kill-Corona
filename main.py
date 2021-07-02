import pygame
import math
import random

pygame.init()
shots = 10


# Images
icon = pygame.image.load("Images/icon.png")
background = pygame.image.load("Images/bg.jpg")
vaccine = pygame.image.load("Images/vaccine.png")
virus = pygame.image.load("Images/coronavirus.png")
noVirus = pygame.image.load("Images/no-virus.png")
bullet = pygame.image.load("Images/shot.png")
danger = pygame.image.load("Images/deadly.png")
winner = pygame.image.load("Images/winner.png")
loss = pygame.image.load("Images/loss.png")

# Vaccine
vaccineX = 380
vaccineY = 400
vaccineXchange = 0
vaccineY_change = 0


def vaccineMover(x, y):
    screen.blit(vaccine, (x, y))

# Virus
virusX = random.randint(0, 800)
virusY = 0
virusY_change = 0


def virusMove(x, y):
    screen.blit(virus, (x, y))

# Bullet
bulletX = 0
bulletY = 300
bulletY_change = 5
bullet_state = "invisible"


def fired_state(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x, y))


font = pygame.font.Font('freesansbold.ttf', 33)
font2 = pygame.font.Font('freesansbold.ttf', 20)

def bullet_collision(bulletX, bulletY, virusX, virusY):
    distance = math.sqrt(math.pow(virusX - bulletX, 2) + (math.pow(virusY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


def virus_collision(vaccineX, vaccineY, virusX, virusY):
    distance = math.sqrt(math.pow(virusY - vaccineY, 2) + (math.pow(virusX - vaccineX , 2)))
    if distance < 27:
        return True
    else:
        return False

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption(" Kill Corona")
pygame.display.set_icon(icon)

running = True
while running:
    clock = pygame.time.Clock()
    clock.tick(1000)
    virusY_change = 1
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                vaccineXchange = -2
                # print("Left")
            if event.key == pygame.K_RIGHT:
                # print("Right")
                vaccineXchange = 2
            if event.key == pygame.K_SPACE:
                bulletX = vaccineX
                # print(bulletY)
                shots = shots - 1
                bulletY -= bulletY_change
                fired_state(bulletX, bulletY)
                # print(shots)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                vaccineXchange = 0

    if vaccineX > 800:
        vaccineX = 0

    if vaccineX < 0:
        vaccineX = 800

    shotText = font2.render(f"Shots Remaining: {shots}", True, (0, 255, 255))
    screen.blit(shotText, (10, 10))

    collision = bullet_collision(virusX, virusY, bulletX, bulletY)
    v_collision = virus_collision(virusX, virusY, vaccineX, vaccineY)
    if collision:
        bullet_state = "ready"
        bulletY_change = 0
        virusY_change = 0
        virus = noVirus
        vaccine = winner
        screen.fill((2, 255, 2))
        win_text = font.render("Yes !!! You Defeated The Coronavirus", True, (255, 255, 255))
        subtext = font2.render("Get vaccinated and wear mask.", True, (255, 0, 0))
        screen.blit(win_text, (120, 50))
        screen.blit(subtext, (250, 100))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                vaccineXchange = 0
                # print("Left")
            if event.key == pygame.K_RIGHT:
                # print("Right")
                vaccineXchange = 0

    elif v_collision:
        bullet_state = "ready"
        bulletY_change = 0
        virus = danger
        vaccine = loss
        virusY_change = 0
        screen.fill((255, 0, 0))
        win_text = font.render("Oh No !!! You Lost ! Try Again", True, (255, 255, 255))
        subtext = font2.render("Get vaccinated and wear mask.", True, (0, 255, 0))
        screen.blit(win_text, (170, 50))
        screen.blit(subtext, (250, 100))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                vaccineXchange = 0
                # print("Left")
            if event.key == pygame.K_RIGHT:
                # print("Right")
                vaccineXchange = 0


    elif shots <= 0:
        bullet_state = "ready"
        bulletY_change = 0
        virusY_change = 0
        screen.fill((8, 0, 0))
        win_text = font.render("You have run out of attempts. Try Again", True, (255, 255, 255))
        subtext = font2.render("Get vaccinated and wear mask.", True, (0, 255, 0))
        screen.blit(win_text, (120, 50))
        screen.blit(subtext, (250, 100))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                vaccineXchange = 0
                # print("Left")
            if event.key == pygame.K_RIGHT:
                # print("Right")
                vaccineXchange = 0

    if virusY > 600:
        virusY = 0
        virusX = random.randint(0, 800)

    if virusY < 0:
        virusY = 0
        virusX = random.randint(0, 800)

    if bulletY <= 0:
        bulletY = vaccineY
        bullet_state = "ready"
        # print(bulletY)

    if bullet_state == "fire":
        fired_state(bulletX, bulletY)
        bulletY -= bulletY_change
        # print(bulletY)

    virusY += virusY_change
    vaccineX += vaccineXchange
    vaccineMover(vaccineX, vaccineY)
    virusMove(virusX, virusY)
    pygame.display.update()

pygame.quit()
