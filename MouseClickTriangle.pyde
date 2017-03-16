p1, p2, p3 = None, None, None
n = 3

'''
Param:
    px = P point x coodinate
    py = P point y coodinate
    qx = Q point x coodinate
    qy = Q point y coodinate
    theta = the angle between P and Q
'''
def rotation(px, py, qx, qy, theta):
    p2x = px - qx
    p2y = py - qy
    p3x = p2x*cos(theta)+p2y*sin(theta)
    p3y = p2y*cos(theta)-p2x*sin(theta)
    p3x += qx
    p3y += qy
    return (p3x,p3y)

def setup():
    size(800, 600)
    

def draw():
    background('#000000')
    global p1, p2
    stroke('#FFFFFF')
    strokeWeight(5)
    noFill()
    
    
    if(p1 is not None):
        point(p1[0], p1[1])
        if(p2 is not None):
            beginShape()
            vertex(p1[0], p1[1])
            vertex(p2[0], p2[1])
            p3 = rotation(p1[0], p1[1], p2[0], p2[1], -PI/3)
            vertex(p3[0], p3[1])
            print(p1, p2, p3)
            endShape(CLOSE)
    
def mouseClicked():
    global p1, p2
    if(p1 == None):
        p1 = (mouseX, mouseY)
    elif(p2 == None):
        p2 = (mouseX, mouseY)
        
def keyTyped():
    if(key >= '3' && key <= '9'):
        global n
        n = key-'0'


    