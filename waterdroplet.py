#water droplet simulation code				Kimberly Winter					10/25/16

import pygame, time
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

class droplet(object):
    def __init__(self):
        self.radius = 1
        self.reset()

    def step(self):
        self.y += self.dy
        self.dy += -9

    def reset(self):
        self.x = 320
        self.y = 0
        self.dy = -1


class dropletView(object):
    def __init__(self, model):
        self.model = model

    def draw(self, surface):
        model = self.model
        pygame.draw.circle(surface, BLUE, (model.x, model.y), model.radius)

    def dropWater(self,)


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    drop1 = droplet()
    droplet_View = dropletView(drop1)
    while True:
    	for event in pygame.event.get():
    		if event.type == pygame.QUIT: 
    			sys.exit()
    	screen.fill(BLACK)
    	drop1.step()
    	droplet_View.draw(screen)
    	pygame.display.update()

class nozzle(object):
	def __init__(self):
		self.timeBetweenDrops =5


main()