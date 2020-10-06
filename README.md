# cmuapcsp
### Unit 3.1
* 3.1.5 Flag of Sweeden <br/>`Rect(50, 100, 300, 200, fill='steelBlue')`<br/>`Rect(50, 180, 300, 40, fill='gold')`<br/>`Rect(140, 100, 40, 200, fill='gold')` 
* 3.1.5 Flag of Chad <br/>`Rect(50, 100, 100, 200, fill='blue')`<br/>`Rect(150, 100, 100, 200, fill='yellow')`<br/>`Rect(250, 100, 100, 200, fill='red')`
* 3.1.7 Diamond Pickaxe <br/>`Rect(125, 125, 75, 75, fill=gradient('peru', 'maroon'))`<br/> `Rect(200, 200, 75, 75, fill=gradient('peru', 'maroon'))`<br/> `Rect(275, 275, 75, 75, fill=gradient('peru', 'maroon'))`<br/> `Rect(50, 50, 40, 40, fill=gradient('peru', 'maroon'))` <br/>`Rect(100, 50, 200, 40, fill=gradient('royalBlue', 'deepSkyBlue', 'dodgerBlue', start='top'))`<br/> `Rect(50, 100, 40, 200, fill=gradient('royalBlue', 'deepSkyBlue', 'dodgerBlue', start='left'))`
* 3.1.7 Orange Juice <br/>`Rect(0, 0, 400, 400, fill=gradient('turquoise', 'paleTurquoise'))`<br/> `Rect(110, 100, 180, 250, fill='azure')`<br/> `Rect(120, 150, 160, 190, fill=gradient('gold', 'yellow', start='bottom'))`<br/> `Rect(130, 170, 40, 40, fill=rgb(255, 255, 200))`<br/> `Rect(190, 200, 30, 30, fill=rgb(255, 255, 200))`<br/> `Rect(240, 50, 50, 10, fill='red')`<br/> `Rect(240, 60, 10, 270, fill=gradient('orange', 'orange', 'orange', 'red', start='bottom'))`
### Unit 3.2
* 3.2.2 Soccer Field <br/>`Rect(0, 0, 400, 400, fill='forestGreen')`<br/> `Rect(50, 100, 300, 200, fill=None, border='white')`<br/>
penalty box<br/>
`Circle(85, 200, 25, fill=None, border='white')`<br/>
`Circle(315, 200, 25, fill=None, border='white')`<br/>
`Rect(50, 150, 50, 100, fill='forestGreen', border='white')`<br/>
`Rect(300, 150, 50, 100, fill='forestGreen', border='white')`<br/>
center field<br/>
`Line(200, 100, 200, 300, fill='white')`<br/>
`Circle(200, 200, 25, fill=None, border='white')`<br/>
goals<br/>
`Rect(40, 180, 20, 40, fill='white')`<br/>
`Rect(340, 180, 20, 40, fill='white')`<br/>

* 3.2.2 Sunny Road <br/>
sky<br/>
`Rect(0, 0, 400, 250, fill=gradient('deepSkyBlue', 'lightSkyBlue', start='top'))`<br/>
grass<br/>
`Rect(0, 250, 400, 150, fill=gradient('lawnGreen', 'green', 'lawnGreen',
                                     'lawnGreen', 'green', start='top'))`<br/>
The center line in the road is missing. Add it in!<br/>
`Rect(0, 275, 400, 100, fill=gradient('darkGray', 'dimGray', start='top'))`<br/>
`Line(0, 325, 400, 325, fill='white', lineWidth=3, dashes=True)`<br/>
car 1<br/>
`Rect(20, 270, 70, 30, fill=gradient('crimson', 'darkRed', start='top'))`<br/>
`Rect(30, 250, 50, 20, fill=gradient('red', 'crimson', start='top'))`<br/>
`Circle(35, 300, 10)`<br/>
`Circle(75, 300, 10)`<br/>
car 2<br/>
`Rect(300, 330, 70, 30, fill=gradient('darkOrange', 'orangeRed', start='top'))`<br/>
`Rect(310, 310, 50, 20, fill=gradient('orange', 'darkOrange', start='top'))`<br/>
`Circle(315, 360, 10)`<br/>
`Circle(355, 360, 10)`<br/>
Fix the rays of the sun so that they are dashed.<br/>
`Circle(0, 0, 70, fill=gradient('orange', 'yellow'))`<br/>
`Line(10, 75, 10, 155, fill=gradient('yellow',  'skyBlue', start='top'),
     lineWidth=5, dashes=True)`<br/>
`Line(35, 70, 75, 140, fill=gradient('yellow',  'skyBlue', start='top'),
     lineWidth=5, dashes=True)`<br/>
`Line(55, 55, 125, 100, fill=gradient('yellow',  'skyBlue', start='top'),
     lineWidth=5, dashes=True)`<br/>
`Line(70, 30, 145, 50, fill=gradient('yellow',  'skyBlue', start='top'),
     lineWidth=5, dashes=True)`<br/>
`Line(75, 5, 155, 5, fill=gradient('yellow',  'skyBlue', start='top'),
     lineWidth=5, dashes=True)`<br/>
* 3.2.2 Scotty Dog<br/>
`Polygon(130, 60, 150, 140, 150, 70, 170, 130, 260, 130, 220, 150, 325, 160,
        315, 260, 290, 240, 210, 240, 210, 270, 250, 310, 180, 380, 80, 280,
        130, 205)`<br/>
Draw the scarf around the neck.<br/>
`Polygon(130, 205, 80, 280, 250, 310, 210, 270, fill='red')`<br/>
* 3.2.2 Monarch<br/>
background<br/>
`Rect(0, 0, 400, 400, fill=gradient('white', 'skyBlue'))`<br/>
wings<br/>
`Rect(110, 130, 200, 130, fill='orange')`<br/>
`Polygon(190, 100, 200, 80, 210, 100, 210, 285, 200, 330, 190, 285)`<br/>
`Circle(290, 130, 80)`<br/>
`Circle(110, 130, 80)`<br/>
`Oval(270, 240, 150, 100)`<br/>
`Oval(130, 240, 150, 100)`<br/>
dots<br/>
`Circle(99, 68, 7, fill='white')`<br/>
`Circle(301, 68, 7, fill='white')`<br/>
`Circle(69, 85, 7, fill='white')`<br/>
`Circle(331, 85, 7, fill='white')`<br/>
`Circle(50, 111, 7, fill='white')`<br/>
`Circle(350, 111, 7, fill='white')`<br/>
antennae<br/>
`Line(195, 92, 174, 57)`<br/>
`Line(205, 92, 226, 57)`<br/>
top half of the pattern<br/>
`Polygon(220, 150, 255, 85, 280, 75, 275, 100, fill='orange')`<br/>
`Polygon(240, 165, 275, 115, 330, 100, 300, 140, fill='orange')`<br/>
`Polygon(260, 180, 295, 155, 330, 155, 310, 185, fill='orange')`<br/>
Finish the top half of the pattern.<br/>
`Polygon(180, 150, 125, 100, 120, 75, 145, 85, fill='orange')`<br/>
`Polygon(160, 165, 100, 140, 70, 100, 125, 115, fill='orange')`<br/>
`Polygon(140, 180, 90, 185, 70, 155, 105, 155, fill='orange')`<br/>
bottom half of the pattern<br/>
`Polygon(80, 225, 120, 210, 160, 230, 115, 240, fill='white')`<br/>
`Polygon(180, 250, 125, 245, 105, 270, 145, 270, fill='white')`<br/>
`Polygon(75, 250, 80, 235, 110, 245, 95, 265, fill='white')`<br/>
Finish the bottom half of the pattern.<br/>
`Polygon(240, 230, 285, 240, 320, 225, 280, 210, fill='white')`<br/>
`Polygon(220, 250, 255, 270, 295, 270, 275, 245, fill='white')`<br/>
`Polygon(290, 245, 305, 265, 325, 250, 320, 235, fill='white')`<br/>
* 3.2.4 Stick Person Comic- [See 3.2.4.py](https://github.com/jamxu88/cmuapcsp/blob/main/3.2.4.py)
* 3.2.4 Target <br/>
draw the target<br/>
`Circle(200, 150, 100, fill='red')`<br/>
`Circle(200, 150, 70, fill='white')`<br/>
`Circle(200, 150, 35, fill='red')`<br/>
You are given the target. Use Label to add the name and complete the logo.<br/>
`Label('TARGET', 200, 300, fill='red', size=65, bold=True, font='arial')`<br/>
