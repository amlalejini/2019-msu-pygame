'''
3D asteroid shooter w/OpenGL
'''
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from random import *
import numpy
import math


class Enemy1:
    vertices = (
        (0, 0, 1),
        (0, 0, -1),
        (0, 1, 0),
        (0, -1, 0),
        (1, 0, 0),
        (-1, 0, 0),

    )

    enemylist = []

    edges = (
        (0, 2),
        (0, 3),
        (0, 4),
        (0, 5),
        (1, 2),
        (1, 3),
        (1, 4),
        (1, 5),
        (2, 4),
        (2, 5),
        (3, 4),
        (3, 5),
    )

    surfaces = (
        (0, 2, 4),
        (0, 3, 4),
        (0, 2, 5),
        (0, 3, 5),
        (1, 2, 4),
        (1, 3, 4),
        (1, 2, 5),
        (1, 3, 5),
    )

    def __init__(self):
        self.edges = Enemy1.edges
        self.vertices = Enemy1.vertices
        self.enemylist = Enemy1.enemylist
        self.surfaces = Enemy1.surfaces

    def draw_sides(self, enemyno):
        tempb = tuple(self.enemylist[enemyno])
        glLineWidth(10)
        glBegin(GL_TRIANGLES)
        for surface in self.surfaces:
            for vertex in surface:
                glColor3f(0.5, 0.5, 0.5)
                glVertex3fv(tempb[vertex])
        glEnd()
        del tempb

    def draw(self, enemyno):
        self.draw_sides(enemyno)
        tempb = tuple(self.enemylist[enemyno])
        glLineWidth(5)
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glColor3f(0.3, 0.3, 0.3)
                glVertex3fv(tempb[vertex])
        glEnd()
        del tempb

    def setvertices(self, x, y, z):
        newvertices = []
        for vert in self.vertices:
            newvert = []
            newx = vert[0] + x
            newy = vert[1] + y
            newz = vert[2] + z
            newvert.extend([newx, newy, newz])
            newvertices.append(newvert)
        self.enemylist.append(newvertices)

    def delete(self, enemyno):
        self.enemylist.pop(enemyno)

    def move(self, x, y, z):
        for i in range(len(self.enemylist)):
            self.enemylist[i] = list(
                map(lambda vert: (vert[0] + x, vert[1] + y, vert[2] + z), self.enemylist[i]))


class Enemy2:
    vertices = (
        (0, 1, 0),
        (0, 0.25, -1),
        (math.sqrt(3)/2, 0.25, 0.5),
        (math.sqrt(3)/-2, 0.25, 0.5),
        (0, -0.25, 1),
        (math.sqrt(3)/2, -0.25, -0.5),
        (math.sqrt(3)/-2, -0.25, -0.5),
        (0, -1, 0),
    )

    enemylist = []

    edges = (
        (0, 1),
        (0, 2),
        (0, 3),
        (7, 4),
        (7, 5),
        (7, 6),
        (1, 5),
        (1, 6),
        (2, 4),
        (2, 5),
        (3, 4),
        (3, 6),
    )

    surfaces = (
        (0, 1, 5, 2),
        (0, 1, 6, 3),
        (0, 3, 4, 2),
        (7, 5, 2, 4),
        (7, 4, 3, 6),
        (7, 6, 1, 5),
    )

    def __init__(self):
        self.edges = Enemy2.edges
        self.vertices = Enemy2.vertices
        self.enemylist = Enemy2.enemylist
        self.surfaces = Enemy2.surfaces

    def draw_sides(self, enemyno):
        tempb = tuple(self.enemylist[enemyno])
        glLineWidth(5)
        glBegin(GL_QUADS)
        for surface in self.surfaces:
            for vertex in surface:
                glColor3f(0.5, 0.5, 0.5)
                glVertex3fv(tempb[vertex])
        glEnd()
        del tempb

    def draw(self, enemyno):
        self.draw_sides(enemyno)
        tempb = tuple(self.enemylist[enemyno])
        glLineWidth(5)
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glColor3f(0.3, 0.3, 0.3)
                glVertex3fv(tempb[vertex])
        glEnd()
        del tempb

    def setvertices(self, x, y, z):
        newvertices = []
        for vert in self.vertices:
            newvert = []
            newx = vert[0] + x
            newy = vert[1] + y
            newz = vert[2] + z
            newvert.extend([newx, newy, newz])
            newvertices.append(newvert)
        self.enemylist.append(newvertices)

    def delete(self, enemyno):
        self.enemylist.pop(enemyno)

    def move(self, x, y, z):
        for i in range(len(self.enemylist)):
            self.enemylist[i] = list(
                map(lambda vert: (vert[0] + x, vert[1] + y, vert[2] + z), self.enemylist[i]))


class Player:
    vertices = (
        (0, 0, 2),
        (0, 3, 0),
        (1, -1, 0),
        (-1, -1, 0),
        (0, -2, 0),
        (0, 0, -1),

        (2, 1, 0),
        (2, -2, 1),
        (2, -2, -1),

        (-2, 1, 0),
        (-2, -2, 1),
        (-2, -2, -1),
    )

    edges = (
        (0, 1),
        (0, 2),
        (0, 3),
        (0, 4),
        (5, 1),
        (5, 2),
        (5, 3),
        (5, 4),
        (1, 2),
        (1, 3),
        (4, 2),
        (4, 3),
        (2, 6),
        (2, 7),
        (2, 8),
        (6, 7),
        (6, 8),
        (7, 8),
        (3, 9),
        (3, 10),
        (3, 11),
        (9, 10),
        (9, 11),
        (10, 11)
    )

    surfaces = (
        (0, 1, 2),
        (0, 1, 3),
        (0, 4, 2),
        (0, 4, 3),
        (5, 1, 2),
        (5, 1, 3),
        (5, 4, 2),
        (5, 4, 3),
        (2, 6, 7),
        (2, 6, 8),
        (2, 7, 8),
        (3, 9, 10),
        (3, 9, 11),
        (3, 10, 11)
    )

    def __init__(self):
        self.edges = Player.edges
        self.vertices = Player.vertices
        self.surfaces = Player.surfaces

    def draw(self, x, y, z):
        self.move(x, y, z)
        self.draw_sides()
        glLineWidth(10)
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glColor3f(randint(0, 1), randint(0, 1), randint(0, 1))
                glVertex3fv(self.vertices[vertex])
        glEnd()

    def draw_sides(self):
        glLineWidth(10)
        glBegin(GL_TRIANGLES)
        for surface in self.surfaces:
            for vertex in surface:
                glColor3f(0, 0, 0)
                glVertex3fv(self.vertices[vertex])
        glEnd()

    def move(self, x, y, z):
        self.vertices = list(
            map(lambda vert: (vert[0] + x, vert[1] + y, vert[2] + z), self.vertices))


class Bullet:
    vertices = (
        (0, 0.5, 0),
        (0.2, -0.5, 0),
        (-0.2, -0.5, 0),
        (0, -0.5, 0.2),
        (0, -0.5, -0.2),
    )

    edges = (
        (0, 1),
        (0, 2),
        (0, 3),
        (0, 4),
    )

    bulletlist = []

    def __init__(self):
        self.edges = Bullet.edges
        self.vertices = Bullet.vertices
        self.bulletlist = Bullet.bulletlist

    def draw(self, bulletno):
        tempb = tuple(self.bulletlist[bulletno])
        glLineWidth(5)
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glColor3f(1, 1, 1)
                glVertex3fv(tempb[vertex])
        glEnd()
        del tempb

    def setvertices(self, x, z):
        newvertices = []
        for vert in self.vertices:
            newvert = []
            newx = vert[0] + x
            newz = vert[2] + z
            newvert.extend([newx, vert[1], newz])
            newvertices.append(newvert)
        self.bulletlist.append(newvertices)

    def delete(self):
        self.bulletlist.pop(0)

    def move(self, speed):
        for bullet in range(len(self.bulletlist)):
            self.bulletlist[bullet] = list(map(lambda b: (
                b[0], b[1] + speed, b[2]), self.bulletlist[bullet]))
            bullet += 1


def render():
    pygame.init()
    display = (1400, 780)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Space Video Game", "Space Video Game")
    gluPerspective(60, (display[0]/display[1]), 0.1, 50)

    glTranslatef(0, 0, -15)
    glRotatef(-90, 1, 0, 0)
    glEnable(GL_DEPTH_TEST)

    def spawnenemy(depth):
        if randint(0, 10) >= 5:
            e2.setvertices(randrange(-10, 10, 1),
                           depth, randrange(-6, 6, 1))
        else:
            e1.setvertices(randrange(-10, 10, 1),
                           depth, randrange(-6, 6, 1))

    gamespeed = 0.1
    b1 = False
    b2 = False
    b3 = False
    ppos = [0, 0]
    bstatus = [False, False, 1]
    p = Player()
    e1 = Enemy1()
    e2 = Enemy2()
    b = Bullet()
    o = True
    vel = 0.25
    clock = pygame.time.Clock()
    while True:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        clock.tick(60)
        currenttime = pygame.time.get_ticks()

        if currenttime > 7500:
            gamespeed = 0.15
            if currenttime > 12500:
                gamespeed = 0.2
                if currenttime > 20000:
                    gamespeed = 0.25

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if bstatus[0] == False:
                        bstatus[2] = currenttime
                        bstatus[0] = True
                        b1 = True
                        b2 = True
                        b3 = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    bstatus[0] = False
                    for i in range(len(b.bulletlist)):
                        b.delete()
                        i += 1

        keys = pygame.key.get_pressed()
        if ppos[0] >= -10.5:
            if keys[pygame.K_a]:
                ppos[0] -= vel
                p.draw(-vel, 0, 0)
        if ppos[0] <= 10.5:
            if keys[pygame.K_d]:
                ppos[0] += vel
                p.draw(vel, 0, 0)
        if ppos[1] <= 6.25:
            if keys[pygame.K_w]:
                ppos[1] += vel
                p.draw(0, 0, vel)
        if ppos[1] >= -6.25:
            if keys[pygame.K_s]:
                ppos[1] -= vel
                p.draw(0, 0, -vel)

        if bstatus[0] == True:
            if bstatus[2] <= currenttime:
                if b1 == True:
                    b.setvertices(ppos[0], ppos[1])
                    b1 = False
                b.draw(len(b.bulletlist) - 1)
            if (bstatus[2] + 1000/3) <= currenttime:
                if b2 == True:
                    b.setvertices(ppos[0], ppos[1])
                    b2 = False
                b.draw(len(b.bulletlist) - 2)
            if (bstatus[2] + 2000/3) <= currenttime:
                if b3 == True:
                    b.setvertices(ppos[0], ppos[1])
                    b3 = False
                b.draw(len(b.bulletlist) - 3)
            if bstatus[2] + 1000 <= currenttime:
                bstatus[2] = currenttime
                b1 = True
                b2 = True
                b3 = True

        if currenttime % (100/gamespeed) >= 80/gamespeed and o == True:
            spawnenemy(20)
            o = False
        if currenttime % (100/gamespeed) <= 20 and o == False:
            o = True

        if int(len(e1.enemylist)) > 0:
            for i in range(len(e1.enemylist)):
                e1.draw(i - 1)
                i += 1
        if int(len(e2.enemylist)) > 0:
            for j in range(len(e2.enemylist)):
                e2.draw(j - 1)
                j += 1

        for bullet in b.bulletlist:
            pos_btip = [bullet[0][0] + 1, bullet[0]
                        [1] + 1, bullet[0][2] + 1]
            neg_btip = [bullet[0][0] - 1, bullet[0]
                        [1] - 1, bullet[0][2] - 1]
            for enemy in e1.enemylist:
                enemypt = enemy[1]
                if (neg_btip[0] < enemypt[0] < pos_btip[0] and neg_btip[1] < enemypt[1] < pos_btip[1] and neg_btip[2] < enemypt[2] < pos_btip[2]) == True:
                    e1.delete(e1.enemylist.index(enemy))
            for enemy in e2.enemylist:
                enemypt = enemy[1]
                if (neg_btip[0] < enemypt[0] < pos_btip[0] and neg_btip[1] < enemypt[1] < pos_btip[1] and neg_btip[2] < enemypt[2] < pos_btip[2]) == True:
                    e2.delete(e2.enemylist.index(enemy))

        for enemy in e1.enemylist:
            enemypt = enemy[1]
            if enemy[1][1] < -15:
                e1.delete(e1.enemylist.index(enemy))
        for enemy in e2.enemylist:
            enemypt = enemy[1]
            if enemy[1][1] < -15:
                e2.delete(e2.enemylist.index(enemy))

        e1.move(0, -gamespeed, 0)
        e2.move(0, -gamespeed, 0)
        b.move(1)
        p.draw(0, 0, 0)
        pygame.display.flip()

render()
