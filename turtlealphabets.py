from turtle import *
from math import *
from sys import *
import math
from functools import partial
import sys
global len, save_x, save_y

def savepos(self):
    global save_y, save_x
    save_x = self.xcor()
    save_y = self.ycor()

def setpen(self, perpendicular = 100.0, base = 20.0):
    global save_x, save_y
    self.seth(0)
    self.up()
    self.goto(save_x + perpendicular + base, save_y)
    self.down()

def ellipse(self, x_radius, y_radius,heading = 0,angle = 2 * math.pi, steps = 60):
    down = self.isdown()  # record pen state for restoration later

    if not down:
        self.pendown()

    heading_radians = math.radians(heading)
    theta_radians = -math.pi / 2
    extent_radians = angle
    step_radians = extent_radians / steps
    extent_radians += theta_radians
    x_center, y_start = self.position()
    y_center = y_start + y_radius

    cos_heading, sin_heading = math.cos(heading_radians), math.sin(heading_radians)

    while True:
        x, y = x_center + math.cos(theta_radians) * x_radius, y_center + math.sin(theta_radians) * y_radius
        # readjust x & y to set the angle of the ellipse based on the original heading of the turtle
        x, y = x - x_center, y - y_start
        x, y = x * cos_heading - y * sin_heading, x * sin_heading + y * cos_heading
        x, y = x + x_center, y + y_start

        self.setheading(self.towards(x, y))  # turtle faces direction in which ellipse is drawn
        self.goto(x, y)

        if theta_radians == extent_radians:
            break

        theta_radians = min(theta_radians + step_radians, extent_radians)  # don't overshoot our starting point

    self.setheading(self.towards(x_center, y_start))  # set correct heading for the next thing we draw

    if not down:  # restore pen state on return
        self.penup()

def a(self):
    global len
    perpendicular = len

    # saving coordinates for orignial location
    savepos(self)

    # calculating base , perp, hyp and angle
    base = perpendicular / 2
    hyp = hypot(base / 2, perpendicular)
    angle = acos((base / 2) / hyp) * (180 / pi)

    # making forward slash
    self.lt(angle)
    self.fd(hyp)

    # making backward slash
    self.right(2 * angle)
    self.fd(hyp)
    self.up()
    self.bk(hyp / 2)
    getx = self.xcor()
    self.bk(hyp / 2)
    self.right(- 2 * angle)
    self.bk(hyp / 2)
    self.lt(- angle)
    self.down()

    # making the cross of alphabet a and saveing the x coordinate
    self.fd(abs(getx - self.xcor()))

    # setting the cursor for next alphabet
    setpen(self, base)

def b(self):
    global len
    perpendicular = len

    # saving coordinates for original location
    savepos(self)
    # making the two curves of b
    self.ellipse(perpendicular / 2, perpendicular / 4, angle = pi)
    self.ellipse(perpendicular / 2, perpendicular / 4, angle = pi)

    # making the line of B
    self.seth(self.towards(save_x, save_y))
    self.fd(perpendicular)

    # setting the cursor for next alphabet
    setpen(self, perpendicular / 2)

def c(self):
    global len
    perpendicular = len

    # saving coordinates for original location
    savepos(self)
    '''
    #setting the position of the pen at the top right corner
    self.up()
    self.goto(save_x + perpendicular / 2, save_y + perpendicular)
    self.down()
    self.ellipse(perpendicular / 4, perpendicular / 2, heading = 180, angle = pi)
    #go to original position
    self.up()
    self.goto(save_x, save_y)
    self.down()
    setpen(self, perpendicular / 2)
    '''
    # going to top right corner to make the curve
    self.seth(180)
    self.up()
    self.goto(save_x + perpendicular / 2, save_y + perpendicular)
    self.down()
    self.circle(perpendicular / 2, 180)

    # setting the cursor for next alphabet
    setpen(self, perpendicular / 2)

def d(self):
    global len
    perpendicular = len

    # saving coordinates for original location
    savepos(self)

    # drawing curve of D
    self.ellipse(perpendicular / 2, perpendicular / 2,heading = pi / 2,angle = radians(180.0))
    self.seth(self.towards(save_x, save_y))

    # drawing the perpendicular line of d
    self.fd(perpendicular)

    # setting the cursor for next alphabet
    setpen(self, perpendicular / 2)

def e(self):
    global len
    perpendicular = len

    # saving coordinates for original location
    savepos(self)

    # making the perpendicular
    self.seth(self.towards(save_x, save_y + perpendicular))
    self.fd(perpendicular)

    # making the top most dash
    self.seth(0)
    self.fd(perpendicular / 2)
    self.up()
    self.bk(perpendicular / 2)
    self.lt(90)
    self.bk(perpendicular / 2)

    # making the middle dash
    self.seth(0)
    self.down()
    self.fd(perpendicular / 4)
    self.up()
    self.bk(perpendicular / 4)
    self.down()
    self.lt(90)
    self.bk(perpendicular / 2)

    # making the lowest dash
    self.seth(0)
    self.fd(perpendicular / 2)

    # setting cursor for next alphabet
    setpen(self, perpendicular / 2)

def f(self):
    global len
    perpendicular = len

    # saving coordinates for original location
    savepos(self)

    # making the perpendicular
    self.seth(self.towards(save_x, save_y + perpendicular))
    self.fd(perpendicular)

    # making the top most dash
    self.seth(0)
    self.fd(perpendicular / 2)
    self.up()
    self.bk(perpendicular / 2)
    self.lt(90)
    self.bk(perpendicular / 2)

    # making the middle dash
    self.seth(0)
    self.down()
    self.fd(perpendicular / 4)
    self.up()
    self.bk(perpendicular / 4)
    self.down()
    self.lt(90)
    self.bk(perpendicular / 2)

    # setting the cursor for next alphabet
    setpen(self, perpendicular / 2)

def g(self):
    global len
    perpendicular = len

    # saving coordinates for original location
    savepos(self)

    '''
    #setting the position of the pen at the top right corner
    self.up()
    self.goto(save_x + perpendicular / 2, save_y + perpendicular)
    self.down()


    self.ellipse(perpendicular / 4 , perpendicular / 2, heading = 180, angle = 3 * pi / 2)

    # making longer perpendicular
    self.seth(180)
    self.fd(perpendicular / 4)
    self.up()
    self.bk(perpendicular / 4)
    self.rt(270)
    self.down()

    #making small peprendicular of g
    self.fd(perpendicular / 2)
    '''

    # making the the largest curve
    self.seth(180)
    self.up()
    self.goto(save_x + perpendicular / 2, save_y + perpendicular)
    self.down()
    self.circle(perpendicular / 2, 180)

    # going few steps further to make g look good
    self.fd(5)
    self.seth(90)
    self.fd(perpendicular / 2)
    self.seth(180)
    self.fd(perpendicular / 4 + perpendicular / 40)

    # setting the cursor for next alphabet
    setpen(self, perpendicular / 2)

def h(self):
    global len
    perpendicular = len

    # saving coordinates for original location
    savepos(self)

    # making the left perpendicular
    self.lt(90)
    self.fd(perpendicular)
    self.up()
    self.bk(perpendicular / 2)
    self.down()

    # making the joining dash and right perpendicular upper part
    self.seth(0)
    self.fd(perpendicular / 2)
    self.lt(90)
    self.fd(perpendicular / 2)
    self.up()
    self.bk(perpendicular / 2)
    self.down()

    #making the right perpendicular lower part
    self.rt(180)
    self.fd(perpendicular / 2)

    # setting the cursor for next alphabet
    setpen(self, perpendicular / 2)

def i(self):
    global len
    perpendicular =len

    # saving coordinates for original location
    savepos(self)

    #making the lower dash
    self.seth(0)
    self.fd(perpendicular / 2)
    self.up()
    self.bk(perpendicular / 4)
    self.down()

    #making the pependicular line
    self.lt(90)
    self.fd(perpendicular)
    self.lt(90)
    self.fd(perpendicular / 4)
    self.up()
    self.bk(perpendicular / 4)
    self.down()

    # making the upper right dash
    self.rt(180)
    self.fd(perpendicular / 4)

    # setting the cursor for next alphabet
    setpen(self, perpendicular / 2)

def j(self):
    global len, save_x, save_y
    perpendicular = len

    # saving coordinates for original location
    savepos(self)

    # making the upper dash of j
    self.up()
    self.goto(self.xcor(), self.ycor() + perpendicular)
    self.down()
    self.fd(perpendicular / 2)
    self.up()
    self.bk(perpendicular / 4)
    self.down()
    self.seth(-90)

    # making the perpendicular of length 3/4 of len
    self.fd(3 * perpendicular / 4)

    # going back perpendicular / 4 len in x direction
    self.up()
    self.goto(save_x, save_y)
    self.down()

    # making the curve
    self.ellipse(perpendicular / 4, perpendicular / 4, angle = (pi / 3) + 0.5)

    # setting the cursor for next alphabet
    setpen(self, perpendicular / 2)

def k(self):
    global len
    perpendicular = len

    # saving coordinates of original location
    savepos(self)

    # calculating base, hyp, perpendicular and angle
    base = perpendicular / 2
    hyp = hypot(base, base)
    angle = acos(base / hyp) * (180 / pi)

    # making the perpendicular
    self.seth(90)
    self.fd(perpendicular)
    self.up()
    self.bk(perpendicular / 2)
    self.down()

    # making right upward slash
    self.rt(angle)
    self.fd(hyp)
    self.up()
    self.bk(hyp)
    self.down()

    # making lower backward slash
    self.rt(180 - 2 * angle)
    self.fd(hyp)
    self.up()
    self.bk(hyp)

    # setting the cursor for next alphabet
    setpen(self, perpendicular / 2)

def l(self):
    global len
    perpendicular = len

    # saving coordinates for original location
    savepos(self)

    # making the upward perpendicular
    self.seth(90)
    self.fd(perpendicular)
    self.up()
    self.bk(perpendicular)
    self.down()

    # making the horizontal line
    self.seth(0)
    self.fd(perpendicular / 2)
    self.up()
    self.bk(perpendicular / 2)
    self.down()

    # setting the cursor for next alphabet
    setpen(self, perpendicular / 2)

def m(self):
    global len
    perpendicular = len

    # saving coordinates for original location
    savepos(self)

    # making the upward perpendicular
    self.seth(90)
    self.fd(perpendicular)

    # calculating angle
    perp = perpendicular / 2
    base = perpendicular / 4
    hyp = hypot(perp, base)
    angle = asin(perp / hyp) * (180 / pi)
    angle2 = acos(base / hyp) * (180 / pi)

    # now making the downward and upward lines
    self.seth(-angle)
    self.fd(hyp)
    self.seth(0)
    self.lt(angle2)
    self.fd(hyp)

    # making another perpendicular
    self.seth(0)
    self.right(90)
    self.fd(perpendicular)

    # setting the cursor for next alphabet
    setpen(self, perpendicular / 2)

def n(self):
    global len
    perpendicular = len

    # saving coordinates of original location
    savepos(self)

    # calculating the base, hyp, perp and angle
    base = perpendicular / 2
    perp = perpendicular
    hyp = hypot(base, perp)
    angle = asin(perp / hyp) * (180.0 / pi)

    # making the first perpendicular
    self.seth(90)
    self.fd(perpendicular)

    # making the slash
    self.seth(- angle)
    self.fd(hyp)

    # making the upward perpendicular
    self.seth(90)
    self.fd(perpendicular)

    # setting the cursor for next alphabet
    setpen(self, perpendicular / 2)

def o(self):
    global len, save_x, save_y
    perpendicular = len

    # saving coordinates of original location
    savepos(self)

    # moving by distance perp / 4 to begin the circle
    self.up()
    self.goto(save_x + perpendicular / 4, save_y)
    self.down()

    # making the ellipse
    self.ellipse(perpendicular / 4, perpendicular / 2)

    # making a small arc
    self.up()
    self.goto(save_x + perpendicular / 4, save_y + perpendicular)
    self.down()
    self.ellipse(perpendicular / 10, perpendicular / 10 , angle =  pi, heading = 180)
    self.ellipse(perpendicular / 4, perpendicular / 4, angle=(pi / 3) + 0.5)

    # setting the cursor for next alphabet
    setpen(self, perpendicular / 2)

def p(self):
    global len
    perpendicular = len

    # saving coordinates of original location
    savepos(self)

    # making the perpendicular
    self.seth(90)
    self.fd(perpendicular)
    self.up()
    self.bk(perpendicular / 2)
    self.down()

    # making the ellipse
    self.ellipse(perpendicular / 2, perpendicular / 4, angle = pi)

    # setting cursor for next alphabet
    setpen(self, perpendicular / 2)

def q(self):
    global len, save_x, save_y
    perpendicular = len

    # saving coordinates of original location
    savepos(self)

    # moving by distance perp / 4 to begin the circle
    self.up()
    self.goto(save_x + perpendicular / 4, save_y)
    self.down()

    # making the ellipse
    self.ellipse(perpendicular / 4, perpendicular / 2)
    self.up()
    self.goto(save_x + perpendicular / 2, save_y)
    self.down()

    # making the small dash
    base = perpendicular / 4
    perp = perpendicular / 10
    hyp = hypot(base, perp)
    angle = acos(base / hyp) * (180 / pi)
    self.seth(180)
    self.rt(angle)
    self.fd(hyp)

    # setting the cursor for next alphabet
    setpen(self, perpendicular / 2)

def r(self):
    global len
    perpendicular = len

    # saving coordinates of original location
    savepos(self)

    # making the perpendicular
    self.seth(90)
    self.fd(perpendicular)
    self.up()
    self.bk(perpendicular / 2)
    self.down()

    # making the ellipse
    self.ellipse(perpendicular / 2, perpendicular / 4, angle = pi)
    self.up()
    self.fd(perpendicular / 2)
    self.down()
    self.seth(0)

    # making the lower dash
    hyp = hypot(perpendicular / 2, perpendicular / 2)
    angle = asin(perpendicular / 2 / hyp) * (180 / pi)

    # making the dash
    self.seth(-angle)
    self.fd(hyp)

    # setting cursor for next alphabet
    setpen(self, perpendicular / 2)

def s(self):
    global len, save_x, save_y
    perpendicular = len

    # saving coordinates of original location
    savepos(self)

    # making the lower curve
    self.ellipse(perpendicular / 2, perpendicular / 4 + perpendicular / 60, angle = pi - pi / 6)

    # making the upper curve
    self.up()
    self.goto(save_x + perpendicular / 2, save_y + perpendicular )
    self.ellipse(perpendicular / 2 , perpendicular / 4 + perpendicular / 60 , heading = 180,angle = pi - pi / 6)

    # setting the cursor for next alphabet
    setpen(self, perpendicular / 2)

def t(self):
    global len
    perpendicular = len

    # saving coordinates of original location
    savepos(self)

    # going to the middle of the location
    self.up()
    self.seth(0)
    self.fd(perpendicular / 4)
    self.down()

    # making the pependicular line
    self.lt(90)
    self.fd(perpendicular)
    self.lt(90)
    self.fd(perpendicular / 4)
    self.up()
    self.bk(perpendicular / 4)
    self.down()

    # making the upper right dash
    self.rt(180)
    self.fd(perpendicular / 4)

    # setting the cursor for next alphabet
    setpen(self, perpendicular / 2)

def u(self):
    global len
    perpendicular = len

    # save coordinates of original location
    savepos(self)

    # making the upper perpendicular
    self.up()
    self.goto(self.xcor(), self.ycor() + perpendicular)
    self.down()
    self.seth(-90)

    # making the forward upward perpendicular
    self.fd(3 * perpendicular / 4)

    # drawing the curve
    self.circle(perpendicular / 4, 180)

    # drawing the rightmost perpendicular
    self.fd(3 * perpendicular / 4)

    # setting the cursor for next alphabet
    setpen(self, perpendicular / 2)

def v(self):
    global len
    perpendicular = len

    # saving coordinates of original location
    savepos(self)

    # getting the angle
    perp = perpendicular
    base = perpendicular / 4
    hyp = hypot(perp, base)
    angle = asin(perp / hyp) * (180 / pi)
    self.seth(90)
    self.up()
    self.fd(perpendicular)
    self.down()

    # making the backward slash
    self.seth(-angle)
    self.fd(hyp)

    #making the forward slash
    self.seth(angle)
    self.fd(perpendicular)

    # setting the cursor for next alphabet
    setpen(self, perpendicular / 2)

def w(self):
    global len
    perpendicular = len

    # saving coordinates for original location
    savepos(self)

    # making the upward perpendicular
    self.seth(90)
    self.fd(perpendicular)
    self.up()
    self.bk(perpendicular)
    self.down()

    # calculating angle
    perp = perpendicular / 2
    base = perpendicular / 4
    hyp = hypot(perp, base)
    angle = asin(perp / hyp) * (180 / pi)
    angle2 = acos(base / hyp) * (180 / pi)

    # now making the downward and upward lines
    self.seth(angle)
    self.fd(hyp)
    self.seth(-angle2)
    self.fd(hyp)

    # making another perpendicular
    self.seth(90)
    self.fd(perpendicular)

    # setting the cursor for next alphabet
    setpen(self, perpendicular / 2)

def x(self):
    global len
    perpendicular = len

    # saving coordinates for original location
    savepos(self)

    # calculating base, perp , hyp and angle
    base = perpendicular / 2
    hyp = hypot(base, perpendicular)
    angle = acos(base / hyp) * (180 / pi)

    # making the forward slash
    self.lt(angle)
    self.fd(hyp)
    self.up()
    self.bk(hyp / 2)

    # making the lower part of the backward slash
    self.rt(2 * angle)
    self.down()
    self.fd(hyp / 2)
    self.up()
    self.bk(hyp / 2)
    self.down()

    # making the upper part of the backward slash
    self.lt((180))
    self.fd(hyp / 2)

    # setting the cursor for next alphabet
    setpen(self, perpendicular / 2)

def y(self):
    global len
    perpendicular = len

    # save coordinates of original location
    savepos(self)

    # calculating base, perp , hyp and angle
    base = perpendicular / 2
    hyp = hypot(base, perpendicular)
    angle = asin(perpendicular / hyp) * (180 / pi)
    angle2 = acos(base / hyp) * (180 / pi)
    self.up()
    self.seth(0)
    self.goto(self.xcor(), self.ycor() + perpendicular)
    self.down()

    # making the half backward slash and the half perpendicular line
    self.seth(- angle)
    self.fd(hyp / 2)
    self.seth(-90)
    self.fd(perpendicular / 2)
    self.up()
    self.bk(perpendicular / 2)
    self.seth(0)
    self.down()

    # making the half forward slash
    self.seth(angle2)
    self.fd(hyp / 2)

    # setting the cursor for next alphabet
    setpen(self, perpendicular / 2)

def z(self):
    global len
    perpendicular = len

    # saving coordinates of original location
    savepos(self)

    # getting angle
    perp = perpendicular
    base = perpendicular / 2
    hyp = hypot(base, perp)
    angle = acos(base / hyp) * (180 / pi)
    self.up()
    self.goto(self.xcor(), self.ycor() + perpendicular)
    self.down()
    self.seth(0)

    # making upward horizontal dash
    self.fd(perpendicular / 2)
    self.seth(180)
    self.lt(angle)

    # making the slash
    self.fd(hyp)
    self.seth(0)
    self.fd(perpendicular / 2)

    # setting the cursor for next alphabet
    setpen(self, perpendicular / 2)

def _1(self):
    global len
    perpendicular = len

    # saving coordinates for original location
    savepos(self)

    # making the lower dash
    self.seth(0)
    self.fd(perpendicular / 2)
    self.up()
    self.bk(perpendicular / 4)
    self.down()

    # making the pependicular line
    self.lt(90)
    self.fd(perpendicular)
    self.lt(90)


    # calculating angle
    perp = perpendicular / 4
    hyp = hypot(perp, perp)
    angle = asin(perp/hyp) * (180 / pi)

    # now making the slash
    self.seth(180)
    self.lt(angle)
    self.fd(hyp)

    # setting the cursor for next number
    setpen(self, perpendicular / 2)

def _2(self):
    global len
    perpendicular = len

    # saving coordinates for original location
    savepos(self)

    # setting the cursor to the top to draw the semi circle
    self.up()
    self.seth(0)
    self.goto(save_x + perpendicular / 2, save_y + 3 * perpendicular / 4)
    self.down()

    # drawing the semi circle
    self.seth(90)
    self.circle(perpendicular / 4, 180)
    self.seth(180)
    self.up()
    self.bk(perpendicular / 2)

    # calculating angle and hypotenuse
    perp = 3 * perpendicular / 4
    base = perpendicular / 2
    hyp = hypot(perp, base)
    angle = asin(perp / hyp) * (180 / pi)
    self.lt(angle)
    self.down()

    # making the slash downward
    self.fd(hyp)

    # making the downward dash
    self.seth(0)
    self.fd(perpendicular / 2)

    # setting the cursor for next number
    setpen(self, perpendicular / 2)

def _3(self):
    global len
    perpendicular = len

    # saving coordinates for original location
    savepos(self)

    # moving the cursor and drawing the upper arc
    self.seth(0)
    self.up()
    self.goto(save_x + perpendicular / 4, save_y + perpendicular / 2)
    self.down()
    self.circle(perpendicular / 4, 270)

    # moving the cursor and drawing the lower arc
    self.up()
    self.seth(270)
    self.goto(save_x, save_y + perpendicular / 4)
    self.down()
    self.circle(perpendicular / 4, 270)

    # setting the cursor for next number
    setpen(self, perpendicular / 2)

def _4(self):
    global len
    perpendicular = len

    # saving coordinates for original location
    savepos(self)

    # making the perpendicular
    self.up()
    base = perpendicular / 2
    self.fd( 3 * base / 4)
    self.seth(90)
    self.down()
    self.fd(perpendicular)

    # making the slash
    base = 3 * base / 4
    perp = 3 * perpendicular / 4
    hyp = hypot(base, perp)
    angle = asin(perp / hyp) * (180 / pi)
    self.seth(180)
    self.lt(angle)
    self.fd(hyp)

    # making the forward dash
    self.seth(0)
    self.fd(perpendicular / 2)

    # setting the cursor for next number
    setpen(self, perpendicular / 2)

def _5(self):
    global len
    perpendicular = len

    # saving coordinates for original location
    savepos(self)

    # making the upper dash
    self.up()
    self.goto(save_x + perpendicular / 2, save_y + perpendicular)
    self.down()
    self.seth(180)
    self.fd(perpendicular / 2)

    # making the vertical dash
    self.seth(270)
    self.fd(perpendicular / 2 - perpendicular / 20)

    # making the curve
    self.up()
    self.seth(270)
    self.goto(save_x, save_y)
    self.down()
    self.ellipse(perpendicular / 2, perpendicular / 4 + perpendicular / 60, angle = pi )

    # setting the cursor for next number
    setpen(self, perpendicular / 2)

def _6(self):
    global len
    perpendicular = len

    # saving coordinates for original location
    savepos(self)

    # making the small arc
    self.up()
    self.goto(save_x + perpendicular / 2.5, save_y + perpendicular - perpendicular / 8)
    self.down()
    self.ellipse(perpendicular / 4, perpendicular / 1.5, angle = pi / 5, heading = 90)

    # making the upper curve and the inner circle
    self.ellipse(perpendicular / 4, perpendicular / 2, heading = 180, angle = pi)
    self.seth(0)
    self.ellipse(perpendicular / 4, perpendicular / 4 , angle = 2 * pi - pi / 1.5)

    # setting the cursor for next number
    setpen(self, perpendicular / 2)

def _7(self):
    global len, save_x, save_y
    perpendicular = len

    # saving coordinates of original location
    savepos(self)

    # making the top dash
    self.up()
    self.goto(save_x, save_y + perpendicular)
    self.down()
    self.fd(perpendicular / 2)

    # making the vertical dash
    base = perpendicular / 2
    hyp = hypot(perpendicular, base)
    angle = acos(perpendicular / hyp) * (180 / pi)
    self.seth(-90)
    self.rt(angle)
    self.fd(hyp)

    # setting the cursor for next alphabet
    setpen(self, perpendicular / 2)

def _8(self):
    global len
    perpendicular = len

    # saving coordinates for original location
    savepos(self)

    # moving the cursor and drawing the upper arc
    self.seth(0)
    self.up()
    self.goto(save_x + perpendicular / 4, save_y + perpendicular / 2)
    self.down()
    self.circle(perpendicular / 4, 360)

    # moving the cursor and drawing the lower arc
    self.up()
    self.seth(270)
    self.goto(save_x, save_y + perpendicular / 4)
    self.down()
    self.circle(perpendicular / 4, 360)

    # setting the cursor for next number
    setpen(self, perpendicular / 2)

def _9(self):
    global len
    perpendicular = len

    # saving coordinates for original location
    savepos(self)

    # moving the cursor and drawing the upper arc
    self.seth(0)
    self.up()
    self.goto(save_x + perpendicular / 4, save_y + perpendicular / 2)
    self.down()
    self.circle(perpendicular / 4, 360)

    # moving the cursor and drawing the cursor
    self.up()
    self.goto(save_x , save_y + perpendicular / 5)
    self.down()
    self.ellipse(perpendicular / 4, perpendicular / 2, angle=pi / 3, heading=270)
    self.up()
    self.goto(save_x + perpendicular / 4, save_y)
    self.down()
    self.ellipse(perpendicular / 4, perpendicular / 2, angle = pi / 2 + pi / 10)

    # setting the cursor for next number
    setpen(self, perpendicular / 2)

def _0(self):
    global len, save_x, save_y
    perpendicular = len

    # saving coordinates of original location
    savepos(self)

    # moving by distance perp / 4 to begin the circle
    self.up()
    self.goto(save_x + perpendicular / 4, save_y)
    self.down()

    # making the ellipse
    self.ellipse(perpendicular / 4, perpendicular / 2)

    # setting the cursor for next alphabet
    setpen(self, perpendicular / 2)


if __name__ == '__main__':
    # global len, save_x, save_y
    # setting the coordinates of the axis
    save_x = 0
    save_y = 0

    # creating a turtle cursor
    apen = Turtle()

    # creating a method ellipse and attaching it to the turtle cursor
    apen.ellipse = partial(ellipse, apen)

    # getting the name of the string from the user
    name = input('enter a string to be written \n').strip()

    # setting the screen for the turtle cursor
    screen = Screen()
    screen.screensize(apen.xcor(), apen.ycor())
    screen.setup(width = 1.0, height = 1.0, startx = None, starty = None)
    screen_width = 1366.00
    screen_height = 768.00
    screen.setworldcoordinates(0.00, 0.00, screen_width, screen_height)

    # getting the size of the alphabet
    len = 100

    # setting the pen attributes and it's coordinates
    apen.pensize(5)
    apen.pencolor("red")
    apen.speed("slow")
    apen.up()
    apen.goto(apen.xcor() + 50, apen.ycor() + screen_height - 100)
    apen.down()

    # storing function names
    alphabets = {'0':_0,'9':_9,'8':_8,'7':_7,'6':_6,'5':_5,'4':_4,'3':_3,'2':_2,'1':_1, 'a':a,'b':b,'c':c,'d':d,
                 'e':e,'f':f,'g':g,'h':h,'i':i,'j':j,'k':k,'l':l,'m':m,'n':n,'o':o,'p':p,'q':q,'r':r,'s':s,'t':t,
                 'u':u,'v':v,'w':w,'x':x,'y':y,'z':z}

    # storing validated input
    storeinput = []

    # validating the input if wrong then print to stderr
    for i in name:
        if i.isalnum() or i.isspace():
            if i.islower() is False:
                i = i.swapcase()
            storeinput.append(i)
        else:
            sys.stderr.write('Wrong input may be a special character')
            exit(1)

    for i in storeinput:
        if i.isalnum():
            alphabets[i](apen)
        else:
            apen.up()
            apen.goto(apen.xcor() + 20.0, apen.ycor())
            apen.down()
    done()

