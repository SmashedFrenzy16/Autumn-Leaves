import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Autumn Leaves")

# Background picture from freepik.com

background = pygame.image.load("autumn_background.png")

leaf_img = []
leaf_y = []
leaf_y_change = []
leaf_num = 20

text_font = pygame.font.Font("freesansbold.ttf", 50)

for i in range(leaf_num):

    # <a href="https://www.flaticon.com/free-icons/autumn" title="autumn icons">Autumn icons created by iconixar - Flaticon</a>

    leaf_img.append(pygame.image.load("leaf-fall.png"))
    leaf_y.append(random.randint(0, 20))
    leaf_y_change.append(40)

running = True

while running:

    screen.fill((255, 255, 255))

    screen.blit(background, (0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

    # Leaf movement

    for i in range(leaf_num):

        while True:

            leaf_y[i] -= leaf_y_change[i]