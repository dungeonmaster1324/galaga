import pygame
import os

pygame.init()
size = width, height = 800, 800
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
fps = 60
balls = []
x, y = 400, 700
def load_image(name, colorkey=None):
    fullname = os.path.join('', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == 276 and x >= 0 and x <= 800:
                x -= 20
            elif event.key == 273 and y <= 800 and y >= 600:
                y -= 20
            elif event.key == 275 and x >= 0 and x <= 800:
                x += 20
            elif event.key == 274 and y <= 800 and y >= 600:
                y += 20
            if event.key == 32:
                balls.append([x + 15, y + 15, 0, -150])

    for ball in balls:
        pygame.draw.circle(screen, (255, 255, 255), (ball[0], ball[1]), 10)
        if ball[0] < 10 or ball[0] > width - 10:
            ball[2] *= -1
        if ball[1] < 10 or ball[1] > height - 10:
            ball[3] *= -1
        ball[0] += int(ball[2] / fps)
        ball[1] += int(ball[3] / fps)

    clock.tick(fps)
    image = load_image("bomb.png")
    screen.blit(image, (x, y))
    pygame.display.flip()