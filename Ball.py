import pygame as pg
import settings

FPS = settings.FPS
dt = 1 / FPS

center_mass = pg.Vector2(0,0)

window_size = settings.window_size
prev_center = pg.Vector2(0,0)

time = 0
def calculate_center_mass_vector(objects):
    global center_mass, time
    mass_list = []
    x_list = []
    y_list = []
    max_mass = 1
    for obj in objects:
        mass_list.append(obj.mass)
        y_list.append(obj.center.y)
        x_list.append(obj.center.x)

    if len(mass_list) != 0:
        max_mass = max(mass_list)

    center_x = 0
    center_y = 0


    for i in range(len(mass_list)):
        center_x += x_list[len(x_list)-1] * (mass_list[i] / max_mass)
        center_y += y_list[len(x_list)-1] * (mass_list[i] / max_mass)

    if len(mass_list) != 0:
        center_x = center_x / len(mass_list)
        center_y = center_y / len(mass_list)
        time+=1
        return  pg.Vector2(center_x, center_y), max_mass
    else:
        time+=1
        return pg.Vector2(0, 0), 1




class Ball:
    def __init__(self, center, radius, color=(255, 255, 255), mass = 1):
        self.center = pg.math.Vector2(center)
        self.radius = radius
        self.color = color
        self.vel = pg.math.Vector2(0, 0)
        self.a = pg.math.Vector2(0, 0)
        self.mass = mass
        # self.color = (mass*10, mass*10, mass*10)

    def update(self, center_mass, max_mass):
        temp = (center_mass - self.center)
        if temp.length() != 0:
            # self.a = temp.normalize() * max_mass**2 / self.center.distance_to(center_mass)
            self.a = temp.normalize()* self.mass * dt * 1000
        self.vel += self.a * dt
        self.center += self.vel * dt

        # self.a += pg.Vector2(0,9.8)
        # self.vel += self.a * dt
        # self.center += self.vel

    def draw(self, surface: pg.Surface):
        if 0 <= self.center.x <= window_size[0] and 0 <= self.center.y <= window_size[1]:
            pg.draw.circle(surface, self.color, self.center, self.radius)

            # pg.draw.line(surface,(255,255,255), (0,0), self.a )
