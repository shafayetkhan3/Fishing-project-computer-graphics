from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random


def draw_points(x, y):
  glPointSize(5)
  glBegin(GL_POINTS)
  glVertex2f(x, y)
  glEnd()

def findZone(dx, dy):
  if dx >= 0 and dy >= 0:
      if abs(dx) >= abs(dy):
          return 0
      else:
          return 1
  if dx <= 0 and dy >= 0:
      if abs(dx) >= abs(dy):
          return 3
      else:
          return 2
  if dx <= 0 and dy <= 0:
      if abs(dx) >= abs(dy):
          return 4
      else:
          return 5
  if dx >= 0 and dy <= 0:
      if abs(dx) >= abs(dy):
          return 7
      else:
          return 6

def con_zone0(x1, y1, x2, y2, zo):
      if zo == 0:
          return x1, y1, x2, y2
      elif zo == 1:
          return y1, x1, y2, x2
      elif zo == 2:
          return y1, -x1, y2, -x2
      elif zo == 3:
          return -x1, y1, -x2, y2
      elif zo == 4:
          return -x1, -y1, -x2, -y2
      elif zo == 5:
          return -y1, -x1, -y2, -x2
      elif zo == 6:
          return -y1, x1, -y2, x2
      elif zo == 7:
          return x1, -y1, x2, -y2


def org_zone(x, y, zo):
      if zo == 0:
          return x, y
      if zo == 1:
          return y, x
      if zo == 2:
          return -y, x
      if zo == 3:
          return -x, y
      if zo == 4:
          return -x, -y
      if zo == 5:
          return -y, -x
      if zo == 6:
          return y, -x
      if zo == 7:
          return x, -y

def DrawLine(x1, y1, x2, y2):
      dx = x2 - x1
      dy = y2 - y1
      zo = findZone(dx, dy)

      x1, y1, x2, y2 = con_zone0(x1, y1, x2, y2, zo)
      list1 = []
      list2 = []
      d1 = []

      dx = x2 - x1
      dy = y2 - y1
      D = 2 * dy - dx

      d1 += [D]
      NE = 2 * (dy - dx)
      E = 2 * dy

      x = x1
      y = y1

      for j in range(x, x2 + 1):
          va = x
          vb = y
          list1 += [x]
          list2 += [y]

          va, vb = org_zone(va, vb, zo)
          draw_points(va, vb)
          x = x + 1
          if D > 0:
              y = y + 1
              D = D + NE
          else:
              D = D + E
              d1 += [D]




def draw_midpoint_circle(c_x,c_y,r):
   x=0
   y=r
   d=1-r

   while (x<y):
       draw_circle_p(x,y,c_x,c_y)
       if d>=0:
           d=d+2*x-2*y+5
           x=x+1
           y=y-1

       else:
           d=d+2*x+3
           x=x+1

def draw_circle_p(x,y,c_x,c_y):
   draw_points(x+c_x, y+c_y)
   draw_points(y+c_x, x+c_y)
   draw_points(-x+c_x, y+c_y)
   draw_points(-y+c_x, x+c_y)
   draw_points(-x+c_x, -y+c_y)
   draw_points(-y+c_x, -x+c_y)
   draw_points(x+c_x, -y+c_y)
   draw_points(y+c_x, -x+c_y)

def draw_quads():
   glBegin(GL_QUADS)
   glColor3f(0.0, 0.0, 1.0)
   glVertex2f(0,250)
   glVertex2f(700,250)
   glVertex2f(700,0)
   glVertex2f(0,0)
   glVertex2f(0, 250)
   glEnd()

def iterate():
          glViewport(0, 0, 700, 700)
          glMatrixMode(GL_PROJECTION)
          glLoadIdentity()
          glOrtho(0.0, 700, 0.0, 700, 0.0, 1.0)
          glMatrixMode(GL_MODELVIEW)
          glLoadIdentity()
boat_x = 150  # Initial x-coordinate of the boat
boat_speed = 2  # Speed of boat movement
human_x = 220  # Initial x-coordinate of the human
human_speed = 2  # Speed of human movement
fish_hook_x = 290  # Initial x-coordinate of the fish-hook
fish_hook_speed = 2  # Speed of fish-hook movement

def showScreen():
    global boat_x,human_x,fish_hook_x,fish_hook_y
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(0.0, 0.0, 1.0)
    draw_points(275,210)
    draw_points(480,210)

    draw_quads() #river

    #fish
    glColor3f(1.0, 0.0, 0.0)
    DrawLine(250, 200, 280, 230)
    DrawLine(250, 200, 280, 180)
    DrawLine(280, 180, 350, 210)
    DrawLine(280, 230, 350, 190)
    DrawLine(350, 210, 350, 190)
    DrawLine(450, 200, 480, 230)
    DrawLine(450, 200, 480, 180)
    DrawLine(480, 180, 550, 210)
    DrawLine(480, 230, 550, 190)
    DrawLine(550, 210, 550, 190)

    #boat
    glColor3f(0.0, 1.0, 0.0)
    DrawLine(150, 320, 200, 250)
    DrawLine(550, 320, 500, 250)
    DrawLine(150, 320, 190, 310)
    DrawLine(550, 320, 510, 310)
    DrawLine(190, 310, 510, 310)

    #person
    glColor3f(0.0, 1.0, 1.0)
    DrawLine(220, 310, 220, 490)
    DrawLine(220, 430, 290, 450)

    #fish-hook
    glColor3f(1.0, 1.0, 0.0)
    DrawLine(290,450,350,230)

    #handling movements
    boat_x += boat_speed #Boat will move according to the speed we initialized
    human_x += human_speed #Human will move according to the speed we initialized
    fish_hook_x += fish_hook_speed #Fish Hook will move according to the speed we initialized

    #boat translating
    glColor3f(0.0, 1.0, 0.0)
    DrawLine(boat_x, 320, boat_x + 50, 250)
    DrawLine(boat_x + 400, 320, boat_x + 350, 250)
    DrawLine(boat_x, 320, boat_x + 40, 310)
    DrawLine(boat_x + 400, 320, boat_x + 360, 310)
    DrawLine(boat_x + 40, 310, boat_x + 360, 310)

    # Human translating
    glColor3f(0.0, 1.0, 1.0)
    DrawLine(human_x, 310, human_x, 490)
    DrawLine(human_x, 430, human_x + 70, 450)

    # Fish Hook translating
    glColor3f(1.0, 1.0, 0.0)
    DrawLine(fish_hook_x,450,fish_hook_x+60, 230)

    #Human Head drawn with midpoint circle
    r = 40
    glColor3f(0.0, 1.0, 1.0)
    draw_midpoint_circle(human_x, 530, r)
    draw_midpoint_circle(220, 530, r)

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(700, 700)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice")
glutDisplayFunc(showScreen)


glutMainLoop()