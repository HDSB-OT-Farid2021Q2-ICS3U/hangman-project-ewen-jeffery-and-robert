import turtle
# imports turtle program so we can draw

def startDraw(word):
  ''' Function to draw the gallows and start the game, 
  as well as print the word using a separate turtle '''

  # first turtle
  # draws gallows and title
  t = turtle.Turtle()
  t.getscreen()._root.attributes('-topmost', 1)
  screen = t.getscreen()
  screen.bgcolor("#faed27")
  t.hideturtle() # hides the arrow that is displayed on screen
  t.speed(50)
  t.penup()
  t.left(90)
  t.forward(250)
  t.write("HANGMAN", move = False, align = 'center',\
 font = ("Helvetica", 24, "normal"))
  t.right(180)
  t.forward(250)
  t.left(90)
  t.pencolor("brown")
  t.right(180)
  t.forward(250)
  t.right(180)
  t.pendown()
  t.forward(150)
  t.right(180)
  t.forward(75)
  t.right(90)
  t.forward(250)
  t.right(180)
  t.forward(45)
  t.left(135)
  t.forward(62)
  t.left(135)
  t.forward(45)
  t.right(180)
  t.forward(150)
  t.right(90)
  t.forward(50)
  t.penup()
  
  # Second turtle for guess word only
  global write
  write = turtle.Turtle(visible = False)
  write.penup()
  write.goto(0,-200)
  write.pencolor("#0000ff")
  write.write(word, move = False, align = 'center',\
 font = ("Verdana", 24, "normal"))

def drawParts(wrong, t):
  ''' Draw body parts after each 
  individual wrong answer '''
  t.hideturtle()

  if wrong == 5:  # head
    t.speed(100)
    t.right(90)
    t.penup()
    t.setx(-51)
    t.sety(175)
    t.pencolor("blue")
    t.speed(10)
    t.pendown()
    t.circle(25)
  elif wrong == 4:  # chest
    t.penup()
    t.pencolor("blue")
    t.setx(-26)
    t.sety(150)
    t.pendown()
    t.forward(100)
  elif wrong == 3:  # left leg
    t.pencolor("blue")
    t.setx(-26)
    t.sety(50)
    t.pendown()
    t.right(45)
    t.forward(50)
  elif wrong == 2:  # right leg
    t.penup()
    t.pencolor("blue")
    t.setx(-26)
    t.sety(50)
    t.pendown()
    t.left(90)
    t.forward(50)
  elif wrong == 1:  # left arm
    t.pencolor("blue")
    t.penup()
    t.setx(-26)
    t.sety(100)
    t.left(90)
    t.pendown()
    t.forward(50)
  elif wrong == 0:  # right arm (body complete)
    t.pencolor("blue")
    t.penup()
    t.setx(-26)
    t.sety(100)
    t.left(90)
    t.pendown()
    t.forward(50)
    t.penup()

def clearWrite():
  ''' Clears text so it can be reprinted '''
  write.undo()

def reset(t):
  ''' Resets all turtles (whole canvas) '''
  t.reset()
  write.reset()