app.background = gradient('mediumSeaGreen', 'seaGreen')

# variables representing the card's suit
app.diamonds = 0
app.hearts = 1
app.clubs = 2
app.spades = 3

# variables for the red suit color and black suit color
app.redColor = 'tomato'
app.blackColor = 'dimGrey'

def drawHearts(x, y, color):
    # draws a heart
    Polygon(x - 22, y - 10, x - 2, y - 10, x - 12, y - 20, fill=color)
    Polygon(x + 22, y - 10, x + 2, y - 10, x + 12, y - 20, fill=color)
    Polygon(x - 22, y - 5, x + 22, y - 5, x, y + 20, fill=color)

def drawDiamonds(x, y, color):
    # draws a diamond
    Rect(x, y, 30, 30, fill=color, rotateAngle=45, align='center')

def drawClubs(x, y, color):
    # draws a clover (clubs)
    Rect(x, y - 10, 12, 12, fill=color, rotateAngle=45, align='center')
    Rect(x - 12, y + 5, 12, 12, fill=color, rotateAngle=45, align='center')
    Rect(x + 12, y + 5, 12, 12, fill=color, rotateAngle=45, align='center')

def drawSpades(x, y, color):
    # draws a spade
    Polygon(x, y - 20, x - 20, y + 10, x + 20, y + 10, fill=color)
    Polygon(x, y + 12, x - 8, y + 20, x + 8, y + 20, fill=color)

def drawCard(x, y, rank, suit):
    # draws the base of the card and its shadow
    Rect(x - 10, y, 100, 150, opacity=10)
    Rect(x, y, 100, 150, fill='white', border='darkGrey')

    # Depending on the card's suit, set the helper variable, suitColor, accordingly.
    # Then draw the correct symbol for the suit at the middle of the card.
    ### (HINT: Hearts and diamonds are red cards, clubs and spades are black cards.)
    ### Fix Your Code Here ###
    if(suit==app.diamonds):
        suitColor=app.redColor
        Rect(x+50, y+75, 30, 30, fill='tomato', rotateAngle=45, align='center')
    if(suit==app.hearts):
        suitColor=app.redColor
        Polygon(x+28, y+65, x+48, y+65, x+38, y+55, fill=suitColor)
        Polygon(x+72, y+65, x +52, y+65, x+62, y+55, fill=suitColor)
        Polygon(x+28, y+70, x+72, y+70, x+50, y+95, fill=suitColor)
    if(suit==app.clubs):
        suitColor=app.blackColor
        Rect(x+50, y+65, 12, 12, fill=suitColor, rotateAngle=45, align='center')
        Rect(x+38, y+80, 12, 12, fill=suitColor, rotateAngle=45, align='center')
        Rect(x+62, y+80, 12, 12, fill=suitColor, rotateAngle=45, align='center')
    if(suit==app.spades):
        suitColor=app.blackColor
        Polygon(x+50, y+55, x+30, y+85, x+70, y+85, fill=suitColor)
        Polygon(x+50, y+87, x+42, y+95, x+58, y+95, fill=suitColor)

    # draws the card using the determined suit color
    Rect(x + 5, y + 5, 90, 140, fill=None, border=suitColor, dashes=True)
    Polygon(x, y, x + 15, y, x, y + 15, fill=suitColor)
    Polygon(x + 100, y, x + 85, y, x + 100, y + 15, fill=suitColor)
    Polygon(x, y + 150, x + 15, y + 150, x, y + 135, fill=suitColor)
    Polygon(x + 100, y + 150, x + 85, y + 150, x + 100, y + 135, fill=suitColor)
    Label(rank, x + 20, y + 20, fill=suitColor)
    Label(rank, x + 80, y + 130, fill=suitColor)

##### Place your code above this line, code below is for testing purposes #####
# test case:
drawCard(50, 125, 'A', app.diamonds)
drawCard(100, 125, 'K', app.diamonds)
drawCard(150, 125, 'Q', app.diamonds)
drawCard(200, 125, 'J', app.diamonds)
drawCard(250, 125, '10', app.diamonds)
