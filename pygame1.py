import pygame
import time
import random

WIDTH, HEIGHT = 750, 650
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Survive From Trash")

BG = pygame.image.load("images/trash.jpg")

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

PLAYER_VEL = 5


def draw(player):
    WIN.blit(BG,(0, 0))

    player.draw.rect(WIN, "red", player)

    pygame.display.update()


def main():
    run = True


player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.x -= PLAYER_VEL
    if keys[pygame.K_d]:
        player.x += PLAYER_VEL

    draw(player)

pygame.quit()

if __name__ == "__main__":
    main()
