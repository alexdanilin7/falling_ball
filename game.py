import pygame
import random

pygame.init()
size = width, height = 400, 300
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

running = True
screen2 = pygame.Surface(screen.get_size())

vel = []
ball_color = []

x1, y1 = 0, 0
start_ball = False
y_pos = 0
v = 100
fps = 60
radius = 10

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            start_ball = True
            x, y_pos = event.pos
            r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            vel.append((int(x), int(y_pos)))
            ball_color.append((r, g, b))

    screen.fill(pygame.Color("black"))
    screen.blit(screen2, (0, 0))
    if start_ball:
        for i in range(len(vel)):
            x, y_pos = vel[i]
            pygame.draw.circle(screen, ball_color[i], (int(x), int(y_pos)), radius)
            if y_pos < height - radius:
                y_pos += v / fps
            else:
                y_pos = height - radius
            vel[i] = (x, y_pos)

        clock.tick(fps)

    pygame.display.flip()

pygame.quit()
