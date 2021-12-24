#Tic Tac Toe Game
import turtle as t
import time

#----game config----
wn = t.Screen()
wn.setup(500, 500)
wn.bgpic('TicTacToe.gif')
xo = t.Turtle()
winner = t.Turtle()
#variables to determine whether a spot is taken or not
# NOTE: will get overwritten later (1 = taken and 0 = open)
a1 = ''
a2 = ''
a3 = ''
b1 = ''
b2 = ''
b3 = ''
c1 = ''
c2 = ''
c3 = ''
position = ''
wintie = 0
style = ('Courier', 30, 'bold')

#----initialize turtle----
winner.hideturtle()
winner.pu()
winner.goto(-230,-245)
winner.write('' , font=style, align='center')
xo.hideturtle()

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

def positionO():
    cont = 0
    while(cont == 0):
        global a1
        global a2
        global a3
        global b1
        global b2
        global b3
        global c1
        global c2
        global c3
        position = input('Where would you like to place Player 2? ')
        xo.pu()
        if (position == 'a1'):
            if (a1 == 'x' or a1 == 'o'):
                print('That spot is already taken! Please choose another one')
            else:
                xo.goto(-160, 145)
                xo.setheading(0)
                drawO()
                a1 = 'o'
                cont = 1
        elif (position == 'a2'):
            if (a2 == 'x' or a2 == 'o'):
                print('That spot is already taken! Please choose another one')
            else:
                xo.goto(-160, 0)
                xo.setheading(0)
                drawO()
                a2 = 'o'
                cont = 1
        elif (position == 'a3'):
            if (a3 == 'x' or a3 == 'o'):
                print('That spot is already taken! Please choose another one')
            else:
                xo.goto(-160, -145)
                xo.setheading(0)
                drawO()
                a3 = 'o'
                cont = 1
        elif (position == 'b1'):
            if (b1 == 'x' or b1 == 'o'):
                print('That spot is already taken! Please choose another one')
            else:
                xo.goto(0, 145)
                xo.setheading(0)
                drawO()
                b1 = 'o'
                cont = 1
        elif (position == 'b2'):
            if (b2 == 'x' or b2 == 'o'):
                print('That spot is already taken! Please choose another one')
            else:
                xo.goto(0, 0)
                xo.setheading(0)
                drawO()
                b2 = 'o'
                cont = 1
        elif (position == 'b3'):
            if (b3 == 'x' or b3 == 'o'):
                print('That spot is already taken! Please choose another one')
            else:
                xo.goto(0, -145)
                xo.setheading(0)
                drawO()
                b3 = 'o'
                cont = 1
        elif (position == 'c1'):
            if (c1 == 'x' or c1 == 'o'):
                print('That spot is already taken! Please choose another one')
            else:
                xo.goto(160, 145)
                xo.setheading(0)
                drawO()
                c1 = 'o'
                cont = 1
        elif (position == 'c2'):
            if (c2 == 'x' or c2 == 'o'):
                print('That spot is already taken! Please choose another one')
            else:
                xo.goto(160, 0)
                xo.setheading(0)
                drawO()
                c2 = 'o'
                cont = 1
        elif (position == 'c3'):
            if (c3 == 'x' or c3 == 'o'):
                print('That spot is already taken! Please choose another one')
            else:
                xo.goto(160, -145)
                xo.setheading(0)
                drawO()
                c3 = 'o'
                cont = 1
        else:
            print('That\'s not an option!! Please pick a different one.')

def positionX():
    cont = 0
    while(cont == 0):
        global a1
        global a2
        global a3
        global b1
        global b2
        global b3
        global c1
        global c2
        global c3
        position = input('Where would you like to place Player 1? ')
        xo.pu()
        if (position == 'a1'):
            if (a1 == 'x' or a1 == 'o' ):
                print('That spot is already taken! Please choose another one')
            else:
                xo.goto(-160, 145)
                xo.setheading(0)
                drawX()
                a1 = 'x'
                cont = 1
        elif (position == 'a2'):
            if (a2 == 'x' or a2 == 'o'):
                print('That spot is already taken! Please choose another one')
            else:
                xo.goto(-160, 0)
                xo.setheading(0)
                drawX()
                a2 = 'x'
                cont = 1
        elif (position == 'a3'):
            if (a3 == 'x' or a3 == 'o'):
                print('That spot is already taken! Please choose another one')
            else:
                xo.goto(-160, -145)
                xo.setheading(0)
                drawX()
                a3 = 'x'
                cont = 1
        elif (position == 'b1'):
            if (b1 == 'x' or b1 == 'o'):
                print('That spot is already taken! Please choose another one')
            else:
                xo.goto(0, 145)
                xo.setheading(0)
                drawX()
                b1 = 'x'
                cont = 1
        elif (position == 'b2'):
            if (b2 == 'x' or b2 == 'o'):
                print('That spot is already taken! Please choose another one')
            else:
                xo.goto(0, 0)
                xo.setheading(0)
                drawX()
                b2 = 'x'
                cont = 1
        elif (position == 'b3'):
            if (b3 == 'x' or b3 == 'o'):
                print('That spot is already taken! Please choose another one')
            else:
                xo.goto(0, -145)
                xo.setheading(0)
                drawX()
                b3 = 'x'
                cont = 1
        elif (position == 'c1'):
            if (c1 == 'x' or c1 == 'o'):
                print('That spot is already taken! Please choose another one')
            else:
                xo.goto(160, 145)
                xo.setheading(0)
                drawX()
                c1 = 'x'
                cont = 1
        elif (position == 'c2'):
            if (c2 == 'x' or c2 == 'o'):
                print('That spot is already taken! Please choose another one')
            else:
                xo.goto(160, 0)
                xo.setheading(0)
                drawX()
                c2 = 'x'
                cont = 1
        elif (position == 'c3'):
            if (c3 == 'x' or c3 == 'o'):
                print('That spot is already taken! Please choose another one')
            else:
                xo.goto(160, -145)
                xo.setheading(0)
                drawX()
                c3 = 'x'
                cont = 1
        else:
            print('That\'s not an option!! Please pick a different one.')

def checkX():
    global wintie
    if (a1 == 'x' and a2 == 'x' and a3 == 'x'):
        print('You won Player 1!!')
        win()
        winner.write('Player 1 Wins!!')
        wintie = 1
    elif (b1 == 'x' and b2 == 'x' and b3 == 'x'):
        print('You won Player 1!!')
        win()
        winner.write('Player 1 Wins!!')
        wintie = 1
    elif (c1 == 'x' and c2 == 'x' and c3 == 'x'):
        print('You won Player 1!!')
        win()
        winner.write('Player 1 Wins!!')
        wintie = 1
    elif (a1 == 'x' and b1 == 'x' and c1 == 'x'):
        print('You won Player 1!!')
        win()
        winner.write('Player 1 Wins!!')
        wintie = 1
    elif (a2 == 'x' and b2 == 'x' and c2 == 'x'):
        print('You won Player 1!!')
        win()
        winner.write('Player 1 Wins!!')
        wintie = 1
    elif (a3 == 'x' and b3 == 'x' and c3 == 'x'):
        print('You won Player 1!!')
        win()
        winner.write('Player 1 Wins!!')
        wintie = 1
    elif (a1 == 'x' and b2 == 'x' and c3 == 'x'):
        print('You won Player 1!!')
        win()
        winner.write('Player 1 Wins!!')
        wintie = 1
    elif (a3 == 'x' and b2 == 'x' and c1 == 'x'):
        print('You won Player 1!!')
        win()
        winner.write('Player 1 Wins!!')
        wintie = 1
    elif (a1 == 'x' and b1 == 'x' and c2 == 'x' and a3 == 'x' and b3 == 'x'):
        print('It\'s a tie!!')
        winner.write('It\'s a tie!!')
        wintie = 1
    elif (b1 == 'x' and c1 == 'x' and a2 == 'x' and b3 == 'x' and c3 == 'x'):
        print('It\'s a tie!!')
        winner.write('It\'s a tie!!')
        wintie = 1
    elif (a2 == 'x' and a3 == 'x' and b1 == 'x' and c2 == 'x' and c3 == 'x'):
        print('It\'s a tie!!')
        winner.write('It\'s a tie!!')
        wintie = 1
    elif (a1 == 'x' and a2 == 'x' and b3 == 'x' and c1 == 'x' and c2 == 'x'):
        print('It\'s a tie!!')
        winner.write('It\'s a tie!!')
        wintie = 1
    else:
            wintie = 0

def checkO():
    global wintie
    if (a1 == 'o' and a2 == 'o' and a3 == 'o'):
        print('You won Player 2!!')
        win()
        winner.write('Player 2 Wins!!')
        wintie = 1
    elif (b1 == 'o' and b2 == 'o' and b3 == 'o'):
        print('You won Player 2!!')
        win()
        winner.write('Player 2 Wins!!')
        wintie = 1
    elif (c1 == 'o' and c2 == 'o' and c3 == 'o'):
        print('You won Player 2!!')
        win()
        winner.write('Player 2 Wins!!')
        wintie = 1
    elif (a1 == 'o' and b1 == 'o' and c1 == 'o'):
        print('You won Player 2!!')
        win()
        winner.write('Player 2 Wins!!')
        wintie = 1
    elif (a2 == 'o' and b2 == 'o' and c2 == 'o'):
        print('You won Player 2!!')
        win()
        winner.write('Player 2 Wins!!')
        wintie = 1
    elif (a3 == 'o' and b3 == 'o' and c3 == 'o'):
        print('You won Player 2!!')
        win()
        winner.write('Player 2 Wins!!')
        wintie = 1
    elif (a1 == 'o' and b2 == 'o' and c3 == 'o'):
        print('You won Player 2!!')
        win()
        winner.write('Player 2 Wins!!')
        wintie = 1
    elif (a3 == 'o' and b2 == 'o' and c1 == 'o'):
        print('You won Player 2!!')
        win()
        winner.write('Player 2 Wins!!')
        wintie = 1
    elif (a1 == 'o' and b1 == 'o' and c2 == 'o' and a3 == 'o' and b3 == 'o'):
        print('It\'s a tie!!')
        winner.write('It\'s a tie!!')
        wintie = 1
    elif (b1 == 'o' and c1 == 'o' and a2 == 'o' and b3 == 'o' and c3 == 'o'):
        print('It\'s a tie!!')
        winner.write('It\'s a tie!!')
        wintie = 1
    elif (a2 == 'o' and a3 == 'o' and b1 == 'o' and c2 == 'o' and c3 == 'o'):
        print('It\'s a tie!!')
        winner.write('It\'s a tie!!')
        wintie = 1
    elif (a1 == 'o' and a2 == 'o' and b3 == 'o' and c1 == 'o' and c2 == 'o'):
        print('It\'s a tie!!')
        winner.write('It\'s a tie!!')
        wintie = 1
    else:
            wintie = 0

def win():
    xo.color('black')
    xo.pu()
    if (a1 == 'o' and a2 == 'o' and a3 == 'o') or (a1 == 'x' and a2 == 'x' and a3 == 'x'):
        xo.goto(-160, 210)
        xo.setheading(270)
        xo.pd()
        xo.forward(420)
    elif (b1 == 'o' and b2 == 'o' and b3 == 'o') or (b1 == 'x' and b2 == 'x' and b3 == 'x'):
        xo.goto(0, 210)
        xo.setheading(270)
        xo.pd()
        xo.forward(420)
    elif (c1 == 'o' and c2 == 'o' and c3 == 'o') or (c1 == 'x' and c2 == 'x' and c3 == 'x'):
        xo.goto(160, 210)
        xo.setheading(270)
        xo.pd()
        xo.forward(420)
    elif (a1 == 'o' and b1 == 'o' and c1 == 'o') or (a1 == 'x' and b1 == 'x' and c1 == 'x'):
        xo.goto(-225, 145)
        xo.setheading(0)
        xo.pd()
        xo.forward(450)
    elif (a2 == 'o' and b2 == 'o' and c2 == 'o') or (a2 == 'x' and b2 == 'x' and c2 == 'x'):
        xo.goto(-225, 0)
        xo.setheading(0)
        xo.pd()
        xo.forward(450)
    elif (a3 == 'o' and b3 == 'o' and c3 == 'o') or (a3 == 'x' and b3 == 'x' and c3 == 'x'):
        xo.goto(-225, -145)
        xo.setheading(0)
        xo.pd()
        xo.forward(450)
    elif (a1 == 'o' and b2 == 'o' and c3 == 'o') or (a1 == 'x' and b2 == 'x' and c3 == 'x'):
        xo.goto(-225, 210)
        xo.setheading(-42)
        xo.pd()
        xo.forward(615.54)
    elif (a3 == 'o' and b2 == 'o' and c1 == 'o') or (a3 == 'x' and b2 == 'x' and c1 == 'x'):
        xo.goto(-225, 210)
        xo.setheading(42)
        xo.pd()
        xo.forward(615.54)

#----events----
print('It\'s time to play Tic Tac Toe!')
time.sleep(2)
print('I\'m sure you already know how it works, but let me explain the rules anyway.')
time.sleep(2)
print('You and your opponent take turns picking spots on the board')
time.sleep(2)
print('If you or your opponent get three in a row, you win!')
time.sleep(2)
print('(Because of coding limitations, player 1 will always be X and player 2 will always be O)')
time.sleep(2)
print('Alright! Let\'s get into it!')
time.sleep(2)
rpt = 'y'
while(rpt == 'y'):
    a1 = ''
    a2 = ''
    a3 = ''
    b1 = ''
    b2 = ''
    b3 = ''
    c1 = ''
    c2 = ''
    c3 = ''
    xo.clear()
    winner.clear()
    turn = 0
    wintie = 0
    while(wintie == 0 and turn <= 9):
        if (turn % 2 == 0):
            positionX()
            checkX()
            turn += 1
        else:
            positionO()
            checkO()
            turn += 1

    time.sleep(2)
    rpt = input('Would you like to play again? (y or n) ')

wn = t.Screen()
wn.mainloop()