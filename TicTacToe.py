import turtle as t

#----game config----
wn = t.Screen()
wn.setup(500, 500)
wn.bgpic('TicTacToe.gif')
xo = t.Turtle()
winner = t.Turtle()
spots_taken = []
#variables to determine whether a spot is taken or not
# NOTE: will get overwritten later (1 = taken and 0 = open)
a1 = 0
a2 = 0
a3 = 0
b1 = 0
b2 = 0
b3 = 0
c1 = 0
c2 = 0
c3 = 0
p1_or_p2s = ''
position = ''

#----initialize turtle----
winner.hideturtle()
winner.pu()
winner.goto(-230,-230)

#----game functions----
def drawX():
  xo.color('red')
  xo.pensize(12)
  xo.pu()
  xo.left(90)
  xo.forward(65)
  xo.left(90)
  xo.forward(65)
  xo.left(140)
  xo.pd()
  xo.forward(170)
  xo.pu()
  xo.left(130)
  xo.forward(110)
  xo.left(130)
  xo.pd()
  xo.forward(170)

def drawO():
  xo.color('blue')
  xo.pensize(12)
  xo.pu()
  xo.right(90)
  xo.forward(45)
  xo.left(90)
  xo.pd()
  xo.circle(55)

def position():
  position = input('Where would you like to place? (a1, b2, c3, etc...)')
  if (position == 'a1'):
    xo.pu()
    xo.goto(-160, 145)
    drawX()

def p1Win():
  #placeholder for function
  print('You won player 1!!')

def p2Win():
  #placeholder
  print('You won player 2!!')

#----events----
rpt = 'y'
while(rpt == 'y'):
  wintie = 0
  while(wintie == 0):
    position()
    wintie = 1;

  rpt = input('Would you like to play again? (y or n)')

wn = t.Screen()
wn.mainloop()
