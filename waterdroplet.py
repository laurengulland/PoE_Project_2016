#water droplet simulation code				Kimberly Winter					10/25/16

import pygame, time
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
screen = pygame.display.set_mode((1000,1000))


class droplet(object):
    def __init__(self):
        self.radius =1
        self.reset()

    def step(self):
        self.y += self.dy
        self.dy += -1

    def reset(self):
        self.y = 0
        self.dy = -1


class dropletView(object):
    def __init__(self, nozzles):
        self.nozzles = nozzles

    def draw(self, surface):
        for nozzle in self.nozzles:
            for drop in nozzle.drops:
                pygame.draw.circle(surface, BLUE, (nozzle.x, drop.y), drop.radius)

class nozzle(object):
    def __init__(self,x):
        self.x=x
        drop1=droplet()
        self.drops=[drop1]

    def dropWater(self):
        screen.fill(BLACK)
        for drop in self.drops:
            drop.step()

    def turn_on(self):
        self.drops.append(droplet())


pygame.init()
pygame.display.set_caption("Water Simulation")
Testnozzle=nozzle(320)
Testnozzle1=nozzle(480)
droplet_View=dropletView([Testnozzle, Testnozzle1])

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
        droplet_View.draw(screen)
        pygame.display.update()
    #Testnozzle.x=320
        Testnozzle.turn_on()
        Testnozzle.dropWater()
        Testnozzle1.dropWater()


main()