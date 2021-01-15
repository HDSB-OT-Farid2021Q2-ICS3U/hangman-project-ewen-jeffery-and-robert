import turtle

# s = turtle.getscreen()

def startDraw(word):
  ''' Function to draw the gallows and start the game '''
  wrong = 1

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

  drawParts(t, wrong)
  wrong += 1
  drawParts(t, wrong)

  turtle.Screen().exitonclick()

def drawParts(t, wrong):
  ''' Draw body parts after each individual wrong answer '''
  if wrong == 1:
    t.setx(-51)
    t.sety(175)
    t.pencolor("blue")
    t.speed(10)
    t.pendown()
    t.circle(25)
  elif wrong == 2:
    t.penup()
    t.setx(-26)
    t.sety(150)
    t.pendown()
    t.forward(100)

if __name__ == "__main__":
  startDraw("Haha")

# TODO: Draw body part whenever a certain condition is met (each time user guesses wrong)
# Legs and arms left