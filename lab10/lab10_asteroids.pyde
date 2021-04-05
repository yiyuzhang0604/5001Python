#circle's global variables
size_x = 600
size_y = 600
circle_x = 300
circle_y = 300
circle_rad = 75

#spaceship's global variables
SIZE = (600, 600)
thrust_factor = 0
spaceship_x = 300
spaceship_y = 300
x_vel = 0
y_vel = 0
rotation = 0

#Initalization
def setup():
    size(size_x, size_y)
    
    COLOR_INDEX = 1
    STROKE_WEIGHT = 3
    colorMode(RGB, COLOR_INDEX)
    strokeWeight(STROKE_WEIGHT)
    
    
def draw():
    BACKGROUND = 0
    background(BACKGROUND)
    blue_circle()
    pushMatrix()
    draw_spaceship()
    popMatrix()
    grey_circle_top_bottom()
    
    
def keyPressed():
    global rotation
    global thrust_factor
    
    THRUST_DIFF = 0.5
    ROTATION_DIFF = 3
    
    if (key == CODED):
    # key is one of the special key
        if keyCode == UP:
            thrust_factor = THRUST_DIFF
        if keyCode == RIGHT:
            rotation += ROTATION_DIFF
        if keyCode == LEFT:
            rotation -= ROTATION_DIFF
            
            
def draw_spaceship():
    global spaceship_x
    global spaceship_y
    global x_vel
    global y_vel
    global thrust_factor
    global rotation 
    
    x_vel = (x_vel + sin(radians(rotation))) * thrust_factor
    y_vel = (y_vel - cos(radians(rotation))) * thrust_factor
    
    spaceship_x = spaceship_x + x_vel
    spaceship_y = spaceship_y + y_vel
    
    translate(spaceship_x, spaceship_y) # move to this point 
    
    rotate(radians(rotation))
    
    # convert number to constant 
    FILL = 0
    STROKE = 1
    STROKE_WEIGHT = 3
    X1 = -16
    Y1 = 10
    X2 = 0
    Y2 = -30
    X3 = 16
    Y3 = 10
    
    fill(FILL)
    stroke(STROKE) # white
    strokeWeight(STROKE_WEIGHT)
    triangle(X1, Y1, X2, Y2, X3, Y3)
    
    
    
def grey_circle_top_bottom():
    #The grey circles method (top and bottom circle)
    global circle_x
    
    CIRCLE_CONSTANT = 1
    circle_x = circle_x + CIRCLE_CONSTANT
    
    if circle_x > size_x + circle_rad:
        circle_x = circle_x - size_x
        
    elif circle_x > size_x - circle_rad:
        draw_circle_1(circle_x - size_x)
        draw_circle_3(circle_x - size_x)
        
    draw_circle_1(circle_x)
    draw_circle_3(circle_x)
    
    
def blue_circle():
    #The light blue circle method
    global circle_y
    
    CIRCLE_CONSTANT = 1
    circle_y = circle_y + CIRCLE_CONSTANT 
    
    if circle_y > size_y + circle_rad:
        circle_y = circle_y - size_y
    elif circle_y > size_y - circle_rad:
        draw_circle_2(circle_y - size_y)
    draw_circle_2(circle_y)
    
    
def draw_circle_1(x):
    FILL = 0.5
    fill(FILL, FILL, FILL)
    
    STROKE = 1.0
    stroke(STROKE, STROKE, STROKE)
    
    Y_COORDINATE = 100
    ellipse(x, Y_COORDINATE, circle_rad * 2, circle_rad * 2)


def draw_circle_2(y):
    RED = 0.8 
    GREEN = 0.9
    BLUE = 1.0
    
    fill(RED, GREEN, BLUE)
    
    STROKE = 1.0 
    stroke(STROKE, STROKE, STROKE)
    
    X_COORDINATE = 300
    ellipse(X_COORDINATE, y, circle_rad * 2, circle_rad * 2)


def draw_circle_3(x):
    FILL = 0.5
    fill(FILL, FILL, FILL)
    
    STROKE = 1.0
    stroke(STROKE, STROKE, STROKE)
    
    Y_COORDINATE = 500
    ellipse(x, Y_COORDINATE, circle_rad * 2, circle_rad * 2)
