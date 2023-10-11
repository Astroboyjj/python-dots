import sys
import pygame
import random

pygame.init()
clock = pygame.time.Clock()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)

class Colors:
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.vx = 0.0
        self.vy = 0.0
        self.color = color

def create_particle_group(number, color):
    return [Particle(random.random() * size[0], random.random() * size[1], color) for _ in range(number)]

def rule(group1, group2, g):
    for a in group1:
        fx = 0
        fy = 0
        for b in group2:
            dx = a.x - b.x
            dy = a.y - b.y
            dsq = dx * dx + dy * dy
            if 0 < dsq < 6400:  # Squared range of effect (80 * 80)
                inv_d = 1.0 / (dsq + 1e-6)
                F = g * inv_d
                fx += F * dx
                fy += F * dy

        a.vx = (a.vx + fx) * 0.5
        a.vy = (a.vy + fy) * 0.5
        a.x += a.vx
        a.y += a.vy

        if not 0 <= a.x <= size[0]:
            a.vx *= -1
        if not 0 <= a.y <= size[1]:
            a.vy *= -1

# Initializing the particles
red_particles = create_particle_group(200, Colors.RED)
green_particles = create_particle_group(200, Colors.GREEN)
blue_particles = create_particle_group(200, Colors.BLUE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    rule(green_particles, green_particles, -0.32)
    rule(green_particles, red_particles, -0.17)
    rule(green_particles, blue_particles, 0.34)
    rule(red_particles, red_particles, -0.10)
    rule(red_particles, green_particles, -0.34)
    rule(blue_particles, blue_particles, 0.15)
    rule(blue_particles, green_particles, -0.20)

    screen.fill(Colors.BLACK)

    for particle_group in [red_particles, green_particles, blue_particles]:
        for particle in particle_group:
            pygame.draw.circle(screen, particle.color, (int(particle.x), int(particle.y)), 1)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
