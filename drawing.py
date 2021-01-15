import turtle

# s = turtle.getscreen()

wrong = 1

def startDraw(word):
  t = turtle.Turtle() # must be within function for game.py to work
  
  t.getscreen()._root.attributes('-topmost', 1)
  '''
  Function to draw the gallows and start the game
  '''
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
  t.speed(50)
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
  t.hideturtle() # hides the arrow that is displayed on screen
  t.penup()
  t.goto(0,-200)
  t.write(word, move = False, align = 'center', font = ("Verdana", 24, "normal"))

  print("HANGMAN".center(40, "~"))

  turtle.Screen().exitonclick()

if __name__ == "__main__":
  startDraw("Haha")
  drawParts()

# TODO: Draw body whenever a certain condition is met (each time user guesses wrong)

def drawParts():
  t = turtle.Turtle() # must be within function for game.py to work.

  if wrong == 1:
    t.pendown()
    t.circle(20)
    t.hideturtle