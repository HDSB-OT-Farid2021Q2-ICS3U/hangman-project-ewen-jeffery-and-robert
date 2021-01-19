import turtle

# s = turtle.getscreen()

def startDraw(word):
  ''' Function to draw the gallows and start the game '''

  global right #,t
  t = turtle.Turtle() # must be within function for game.py to work
  
  t.getscreen()._root.attributes('-topmost', 1)
  screen = t.getscreen()
  screen.bgcolor("pink")
  t.hideturtle() # hides the arrow that is displayed on screen
  t.speed(50)
  t.penup()
  t.left(90)
  t.forward(250)
  t.write("HANGMAN", move = False, align = 'center', font = ("Verdana", 24, "normal"))
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
  # print(t.position())
  
  right = turtle.Turtle(visible = False)
  right.penup()
  right.goto(0,-200)
  right.pencolor("green")
  right.write(word, move = False, align = 'center', font = ("Verdana", 24, "normal"))

  # turtle.Screen().exitonclick()

def drawParts(wrong, t):
  ''' Draw body parts after each individual wrong answer '''
  screen = t.getscreen()
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
    # screen.delay(200)  not needed right now because of input

def clearRight():
  right.undo()

def clear(t):
  t.reset()
  right.reset()

#if __name__ == "__main__":  # @Ewen what does this do?  -- when importing a package the code will run. this is to stop it until the function is called like drawing.start() 
  #startDraw("hey")  # temp argument for sake of testing
  # drawParts()
# TODO: Draw body part whenever a certain condition is met (each time user guesses wrong) DONE
# TODO: Draw word in turtle! Also integrate this into main where @Jeffery is working