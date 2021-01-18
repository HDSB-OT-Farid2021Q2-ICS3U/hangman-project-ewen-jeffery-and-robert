import turtle

# s = turtle.getscreen()

def startDraw(word):
  ''' Function to draw the gallows and start the game '''
  wrong = 6

  t = turtle.Turtle() # must be within function for game.py to work
  
  t.getscreen()._root.attributes('-topmost', 1)
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
  t.goto(0,-200)
  t.write(word, move = False, align = 'center', font = ("Verdana", 24, "normal"))

  print("HANGMAN".center(40, "~"))

  for i in range(6):  # just to test the body draw
    drawParts(t, wrong)
    wrong -= 1

  turtle.Screen().exitonclick()

def drawParts(t, wrong):
  ''' Draw body parts after each individual wrong answer '''
  if wrong == 5:  # head
    t.setx(-51)
    t.sety(175)
    t.pencolor("blue")
    t.speed(10)
    t.pendown()
    t.circle(25)
  elif wrong == 4:  # chest
    t.penup()
    t.setx(-26)
    t.sety(150)
    t.pendown()
    t.forward(100)
  elif wrong == 3:  # left leg
    t.right(45)
    t.forward(50)
  elif wrong == 2:  # right leg
    t.penup()
    t.right(180)
    t.forward(50)
    t.pendown()
    t.right(90)
    t.forward(50)
  elif wrong == 1:  # left arm
    t.penup()
    t.setx(-26)
    t.sety(100)
    t.left(90)
    t.pendown()
    t.forward(50)
  elif wrong == 0:  # right arm (body complete)
    t.penup()
    t.setx(-26)
    t.sety(100)
    t.left(90)
    t.pendown()
    t.forward(50)

if __name__ == "__main__":  # @Ewen what does this do?
  startDraw("Haha")  # temp argument for sake of testing

# TODO: Draw body part whenever a certain condition is met (each time user guesses wrong) DONE
# TODO: Draw word in turtle! Also integrate this into main where @Jeffery is working