import sys
import pygame
import random
import math

pygame.init()
clock = pygame.time.Clock()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)

running = True
black = (0, 0, 0)

# Precompute constants
G_GREEN = -0.32
G_RED = -0.17
G_BLUE = 0.34
G_RED_RED = -0.10
G_RED_GREEN = -0.34
G_BLUE_BLUE = 0.15
G_BLUE_GREEN = -0.20

particles = []

class Particle:
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.vx = 0.0
        self.vy = 0.0
        self.color = c

def createParticleGroup(number, color):
    return [Particle(random.random() * width, random.random() * height, color) for _ in range(number)]

def rule(group1, group2, g):
    for a in group1:
        fx = 0
        fy = 0
        for b in group2:
            dx = a.x - b.x
            dy = a.y - b.y
            d_sq = dx * dx + dy * dy

            if 0 < d_sq < 6400:  # Square of 80 (range of effect)
                inv_d = 1.0 / math.sqrt(d_sq)
                F = g * inv_d
                fx += F * dx
                fy += F * dy

        a.vx = (a.vx + fx) * 0.5
        a.vy = (a.vy + fy) * 0.5
        a.x += a.vx
        a.y += a.vy

        # Reverse direction of particles that leave the screen
        if a.x <= 0 or a.x >= width: a.vx *= -1
        if a.y <= 0 or a.y >= height: a.vy *= -1

# Initializing particle groups
red = createParticleGroup(200, (255, 0, 0))
green = createParticleGroup(200, (0, 255, 0))
blue = createParticleGroup(200, (0, 0, 255))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Interaction logic
    rule(green, green, G_GREEN)
    rule(green, red, G_RED)
    rule(green, blue, G_BLUE)
    rule(red, red, G_RED_RED)
    rule(red, green, G_RED_GREEN)
    rule(blue, blue, G_BLUE_BLUE)
    rule(blue, green, G_BLUE_GREEN)

    # Update graphics
    screen.fill(black)
    for i in particles:
        pygame.draw.circle(screen, i.color, (int(i.x), int(i.y)), 1)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
