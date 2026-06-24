import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Custom Event - Change Sprite Colour")

clock = pygame.time.Clock()

# Custom event
CHANGE_COLOUR = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOUR, 1000)  # every 1 second

class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, colour):
        super().__init__()
        self.image = pygame.Surface((80, 80))
        self.image.fill(colour)
        self.rect = self.image.get_rect(center=(x, y))

    def change_colour(self):
        new_colour = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        self.image.fill(new_colour)

# Create two sprites
sprite1 = Sprite(200, 200, (255, 0, 0))
sprite2 = Sprite(400, 200, (0, 0, 255))

all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1, sprite2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == CHANGE_COLOUR:
            sprite1.change_colour()
            sprite2.change_colour()

    screen.fill((240, 240, 240))
    all_sprites.draw(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()