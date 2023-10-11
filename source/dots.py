# particle simulation of attraction and repulsion
# Based on this YouTube video: https://www.youtube.com/watch?v=0Kx4Y9TVMGg

import sys, pygame, random, math
pygame.init()
clock = pygame.time.Clock()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)

running = True
black = 0,0,0
red = 255,0,0
particles = []


class Particle:
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.vx = 0.0
        self.vy = 0.0
        self.color = c

def createParticleGroup(number, color):
    group = []
    for i in range(number):
        group.append(Particle(random.random() * size[0], random.random() * size[1], color))
        particles.append(group[i])
    return group

def rule(group1, group2, g):
    for i in group1:
        fx = 0
        fy = 0
        for j in group2:
            a = i
            b = j
            dx = a.x-b.x
            dy = a.y-b.y
            d = math.sqrt(dx*dx + dy*dy)
            if(d > 0 and d < 80): # the anded part of this statment is the range of effect of the attraction
                F = g * 1/d
                fx += (F * dx)
                fy += (F * dy)

        a.vx = (a.vx + fx)*0.5 # These velocities are multiplied by a constant to
        a.vy = (a.vy + fy)*0.5 # reduce their speed to a viewable level
        a.x += a.vx
        a.y += a.vy
        #for reversing direction of particles that leave the screen
        if a.x <= 0 or a.x >= size[0]: a.vx *= -1
        if a.y <= 0 or a.y >= size[1]: a.vy *= -1

# INITIALIZING THE PARTICLES
red = createParticleGroup(200, red) 
green = createParticleGroup(200, (0,255,0))
blue = createParticleGroup(200, (0,0,255))
#white = createParticleGroup(200, (255,255,255))
#cyan = createParticleGroup(200, (0,255,255))
#purple = createParticleGroup(200, (255,0,255))
#yellow = createParticleGroup(200, (255,255,0))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            rule(red, red, 0.3)

    # INTERACTION LOGIC 
    rule(green,green,0.32)
    rule(green,red,-0.17)
    rule(green,blue,0.34)
    rule(red,red,-0.10)
    rule(red,green,-0.34)
    rule(blue,blue,0.15)
    rule(blue,green,-0.20)
    
#    rule(white, white, 0.5)
#    rule(cyan, cyan, 0.5)
#    rule(purple, purple, 0.5)
#    rule(yellow, yellow, 0.5)
#    rule(green, red, 0.3)
#    rule(blue, red, 0.3)
#    rule(white, red, 0.3)
#    rule(cyan, red, 0.3)
#    rule(purple, red, 0.3)
#    rule(yellow, red, 0.3)
#    rule(red, green, -0.2)
#    rule(green, blue, -0.3)
#    rule(blue, red, 0.1)


    # UPDATE GRAPHICS
    screen.fill(black) # wipe out the screen for new frame
    # draw all the particles
    for i in particles:
        pygame.draw.circle(screen, i.color, (i.x,i.y), 1) 
    pygame.display.flip() # update what is visible to show the draws

    clock.tick(60)

pygame.quit()
