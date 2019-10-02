import pygame

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

running = True
screen2 = pygame.Surface(screen.get_size())
x1, y1 = 0, 0
start_ball = False
y_pos = 0
v = 20
fps = 60
r=10

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            start_ball=True
            x, y_pos=event.pos
        #   pygame.draw.circle(screen, (255,255,255), event.pos, 10)
    screen.fill(pygame.Color("black"))
    if start_ball:
        pygame.draw.circle(screen, (255,255,255), (int(x), int(y_pos)), r)
        if y_pos<height-r:
            y_pos += v / fps
        else:
            y_pos = height - r

        clock.tick(fps)

    pygame.display.flip()

pygame.quit()