app.background = gradient('sienna', 'chocolate')

def drawCabbage(x, y):
    cabbage = Group(
        Star(200, 200, 50, 8, fill='mediumSeaGreen', rotateAngle=30, roundness=80),
        Star(200, 200, 40, 8, fill='lightGreen', rotateAngle=50, roundness=80),
        Star(200, 200, 30, 8, fill='paleGreen', rotateAngle=70, roundness=80)
        )
    cabbage.centerX = x
    cabbage.centerY = y

def drawCabbages():
    # Draw 5 rows of cabbages using a for loop. In each loop you should draw
    # 5 cabbages. They should all be 100 pixels apart.
    ### Place Your Code Here ###
    for loopVar1 in range(5):
        for loopVar2 in range(5):
            drawCabbage(100*loopVar2, 100*loopVar1)

##### Place your code above this line, code below is for testing purposes #####
# test case:
drawCabbages()
