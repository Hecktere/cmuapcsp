app.background = gradient('lightSkyBlue', 'deepSkyBlue', start='top')

app.hatIndex = 0

# koala
Oval(200, 425, 220, 360, fill=gradient('darkGrey', 'grey', start='top'))
Oval(200, 425, 160, 280, fill='lightGrey')
Circle(130, 150, 40, fill=gradient('grey', 'silver', start='right-bottom'))
Circle(130, 150, 25, fill='lightGrey')
Circle(270, 150, 40, fill=gradient('grey', 'silver', start='right-bottom'))
Circle(270, 150, 25, fill='lightGrey')
Circle(200, 200, 80, fill=gradient('silver', 'grey', start='top'))
Oval(200, 210, 20, 40)
mouth = Rect(188, 238, 20, 2)

# koala's eyes
Oval(180, 180, 10, 20)
Oval(220, 180, 10, 20)
pupils = Group(
    Oval(180, 185, 3, 6, fill='white'),
    Oval(220, 185, 3, 6, fill='white')
    )

# leaf
Oval(218, 250, 25, 45, fill=gradient('seaGreen', 'green', start='bottom'),
     rotateAngle=-60)
Line(197, 238, 235, 260, fill='darkGreen')

baldSpot = Group(
    Oval(200, 138, 50, 28, fill=gradient('moccasin', 'gainsboro'))
    )

bowler = Group(
    Oval(200, 145, 180, 40),
    Oval(200, 115, 80, 100),
    Arc(200, 125, 80, 20, 90, 180, border='white', borderWidth=10),
    )

sombrero = Group(
    Arc(200, 130, 270, 50, 70, 220, fill='orange', border='red',
        borderWidth=3),
    Arc(200, 130, 270, 50, 70, 220, fill=None, border='green', dashes=(20, 20),
        borderWidth=3),
    Oval(200, 90, 75, 100, fill='gold'),
    Rect(200, 90, 75, 60, fill=gradient('orange', 'gold', start='bottom'),
         align='center-top')
    )

wizard = Group(
    Oval(125, 115, 80, 15, fill=gradient('midnightBlue', 'blue', start='bottom')),
    Polygon(107, 110, 125, 30, 143, 110, fill='blue'),
    Oval(125, 110, 36, 5, fill='blue'),
    Star(116, 105, 5, 5, fill='white'),
    Star(134, 105, 5, 5, fill='white'),
    Star(125, 90, 5, 5, fill='white'),
    Star(125, 70, 5, 5, fill='white'),
    Oval(275, 115, 80, 15, fill=gradient('midnightBlue', 'blue', start='bottom')),
    Polygon(257, 110, 275, 30, 293, 110, fill='blue'),
    Oval(275, 110, 36, 5, fill='blue'),
    Star(266, 105, 5, 5, fill='white'),
    Star(284, 105, 5, 5, fill='white'),
    Star(275, 90, 5, 5, fill='white'),
    Star(275, 70, 5, 5, fill='white'),
    Oval(200, 150, 200, 30, fill=gradient('midnightBlue', 'blue', start='bottom')),
    Polygon(150, 145, 200, -10, 250, 145, fill='blue'),
    Oval(200, 145, 100, 10, fill='blue'),
    Star(225, 125, 10, 5, fill='white'),
    Star(200, 85, 10, 5, fill='white'),
    Star(175, 125, 10, 5, fill='white'),
    Star(200, 40, 10, 5, fill='white')
    )

sombrero.visible = False
bowler.visible = False
wizard.visible = False

hats = [ baldSpot, bowler, sombrero, wizard ]

def onMousePress(mouseX, mouseY):
    # Help this koala during his midlife crisis. With each mouse press,
    # set the current hat invisible and set the next hat visible.
    ### Place Your Code Here ###
    pass
    hats[app.hatIndex].visible = False
    app.hatIndex = (app.hatIndex + 1) % 4
    hats[app.hatIndex].visible = True
    # Changes the facial features depending on the hat.
    if (hats[app.hatIndex] == baldSpot):
        pupils.centerY = 185
        mouth.rotateAngle = 0
    else:
        pupils.centerY = 175
        mouth.rotateAngle = 12
    if (hats[app.hatIndex] == wizard):
        pupils.width = 48
    else:
        pupils.width = 43
