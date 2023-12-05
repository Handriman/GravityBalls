import pygame as pg
import pygame.event
from random import randint

import settings
from Ball import Ball, calculate_center_mass_vector

pg.init()
screen = pg.display.set_mode(settings.window_size)
clock = pg.time.Clock()
running = True

FPS = settings.FPS

objects: [Ball] = []
center_mass, max_mass = pg.Vector2(0,0), 1
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.MOUSEBUTTONUP:
            a = pg.mouse.get_pos()
            objects.append(Ball(a, 10,(randint(1, 255),randint(1, 255),randint(1, 255)), randint(20, 100)))
            center_mass, max_mass = calculate_center_mass_vector(objects)




    # mouse_keys = pg.mouse.()
    # if mouse_keys[0]:
    #     objects.append(Ball(pg.mouse.get_pos(), 25))

    center_mass = pg.Vector2(pg.mouse.get_pos())
    pg.draw.circle(surface=screen, radius=20, center=center_mass, color=(100, 100, 100))
    for object in objects:
        object.update(center_mass, max_mass)

        object.draw(surface=screen)
    pg.display.flip()
    clock.tick(FPS)

pg.quit()
