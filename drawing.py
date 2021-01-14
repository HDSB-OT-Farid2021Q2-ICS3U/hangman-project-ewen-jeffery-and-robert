import turtle

# s = turtle.getscreen()

t = turtle.Turtle()

def startDraw():
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

  print("HANGMAN".center(40, "~"))
<<<<<<< Updated upstream

startDraw()

turtle.Screen().exitonclick()
=======
  turtle.Screen().exitonclick()
  
if __name__ == "__main__":
  startDraw()
>>>>>>> Stashed changes
