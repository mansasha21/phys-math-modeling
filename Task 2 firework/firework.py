import random
import time
import sys
import pygame
import numpy as np

velocity = 20
g = 10
N = 3
WIDTH = 1000
HEIGHT = 700
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
color3 = [WHITE, BLUE, RED]
color5 = [WHITE, BLUE, RED, GREEN, CYAN]


class Particle:
    def __init__(
        self,
        width,
        height,
        radius=3 * random.random(),
        color=(random.random() * 255, random.random() * 255, random.random() * 255),
    ):
        self.alpha = random.random() * np.pi * 2
        self.tetha = random.random() * np.pi
        self.color = color
        self.pos = [
            width + radius * np.sin(self.tetha) * np.cos(self.alpha),
            height + radius * np.sin(self.tetha) * np.sin(self.alpha),
        ]
        self.in_pos = self.pos.copy()
        self.finished = False

    def update(self, t):
        if not self.finished:
            self.pos[0] = self.in_pos[0] + velocity * np.cos(self.alpha) * t * np.sin(
                self.tetha
            )
            self.pos[1] = (
                self.in_pos[1]
                + velocity * np.sin(self.alpha) * np.sin(self.tetha) * t
                + g * (t ** 2) * 0.5
            )
            if self.pos[1] > HEIGHT - 10:
                self.pos[1] = HEIGHT - 10
                self.finished = True
        # self.pos[2] = self.in_pos[2] + velocity * np.cos(self.alpha) * t


class Rocket(pygame.sprite.Sprite):
    def __init__(
        self, filename, x_start, velocity=0.0000002, particles_amount=400, color=WHITE
    ):
        pygame.sprite.Sprite.__init__(self)
        self.texture = pygame.image.load(filename).convert_alpha()
        self.rect = self.texture.get_rect(center=(x_start, HEIGHT - 10))
        self.height = 300
        self.particles = [
            Particle(x_start, self.height, color=color) for _ in range(particles_amount)
        ]
        self.destroyed = False
        self.velocity = velocity
        self.start_time = time.time()

    def update_particles(self, t):
        for particle in self.particles:
            particle.update(t)
            # if particle.pos[1] == HEIGHT - 10:
            #     self.particles.remove(particle)

    def update_rocket(self, t):
        if self.destroyed:
            self.update_particles(t - self.start_time)
        else:
            if self.rect.y > self.height:
                # pygame.time.delay(50)
                self.rect.y -= self.velocity
            else:
                self.destroyed = True
                self.start_time = time.time()


pygame.init()
size = WIDTH, HEIGHT
screen = pygame.display.set_mode(size)

in_t = time.time()
filename = f"C:\\Users\\surzh\\Documents\\mansasha\\learn\\data exploring\\rocket.png"
rockets = [
    Rocket(filename, x, velocity=0.0002 * vel, color=color)
    for x, vel, color in zip(
        range(200, WIDTH, 300), [(10 ** i) for i in range(0, N)], color3,
    )
]

last_launched_ind = 0
last_launched_destroyed = False

while True:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    for rocket, ind in zip(rockets, range(0, 5)):
        # if not last_launched_destroyed and ind > last_launched_ind:
        #     continue
        rocket.update_rocket(time.time())
        if not rocket.destroyed:
            screen.blit(rocket.texture, rocket.rect)
            last_launched_destroyed = False
        else:
            last_launched_ind = ind + 1
            last_launched_destroyed = True
            for Particle in rocket.particles:
                color = (
                    int(random.random() * 255),
                    int(random.random() * 255),
                    int(random.random() * 255),
                )
                pygame.draw.circle(
                    screen,
                    Particle.color,
                    (int(Particle.pos[0]), int(Particle.pos[1])),
                    2,
                )
    pygame.display.update()


