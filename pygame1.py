import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 750, 650
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Survive From Trash")

BG = pygame.image.load("images/trash.jpg")

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

PLAYER_VEL = 5

FONT = pygame.font.SysFont("comicsans", 30)


def draw(player, elapsed_time):
    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f"Time:{random(elapsed_time)}s", 1, "black")
    WIN.blit(time_text, (10, 10))


    player.draw.rect(WIN, "red", player)

    pygame.display.update()


def main():
    run = True1


player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
clock = pygame.time.Clock()

start_time = time.time()
elapsed_time = 0


while run:
    clock.ticks(60)
    elapsed_time = time.time() - start_time



for event in pygame.event.get():
    if event.type == pygame.QUIT:
        run = False
        break

keys = pygame.key.get_pressed()
if keys[pygame.K_a] and player.x - PLAYER_VEL >= 0:
    player.x -= PLAYER_VEL
if keys[pygame.K_d] and player.x + PLAYER_VEL + player.width <= WIDTH:
    player.x += PLAYER_VEL

draw(player, elapsed_time)

pygame.quit()

if __name__ == "__main__":
    main()
