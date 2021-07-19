"""
Name: Edward Chang
UCI ID: 19355784
"""


import tkinter

class BoardClass():
    row1 = ['','','']
    row2 = ['','','']
    row3 = ['','','']
    player1 = ''
    player2 = ''
    turnPlayer = ''
    numGames = 0
    p1win = 0
    p1tie = 0
    p1loss = 0
    p2win = 0
    p2tie = 0
    p2loss = 0
    gameProgress = True


    def __init__(self):
        self.row1 = ['','','']
        self.row2 = ['','','']
        self.row3 = ['','','']
        self.player1 = 'player 1'
        self.player2 = 'player 2'
        self.turnPlayer = 'player 2'
        self.numGames = 0
        self.p1win = 0
        self.p1tie = 0
        self.p1loss = 0
        self.p2win = 0
        self.p2tie = 0
        self.p2loss = 0
        self.gameProgress = True


    def recordGamePlayed(self):
        self.numGames += 1


    def resetGameBoard(self):
        self.row1 = ['','','']
        self.row2 = ['','','']
        self.row3 = ['','','']
        self.gameProgress = True
        self.turnPlayer = self.player2


    def playMoveOnBoard(self, rowMove, colMove):
        if self.gameProgress == False:
            self.resetGameBoard()
        if self.gameProgress == True:
            if rowMove == 1:
                if self.row1[colMove] == '':
                    if self.turnPlayer == self.player2:
                        self.row1[colMove] = 'x'
                        if self.isGameFinished() == True:
                            self.gameProgress = False
                        else:
                            self.turnPlayer = self.player1
                    elif self.turnPlayer == self.player1:
                        self.row1[colMove] = 'o'
                        if self.isGameFinished() == True:
                            self.gameProgress = False
                        else:                
                            self.turnPlayer = self.player2
            elif rowMove == 2:
                if self.row2[colMove] == '':
                    if self.turnPlayer == self.player2:
                        self.row2[colMove] = 'x'
                        if self.isGameFinished() == True:
                            self.gameProgress = False
                        else:
                            self.turnPlayer = self.player1
                    elif self.turnPlayer == self.player1:
                        self.row2[colMove] = 'o'
                        if self.isGameFinished() == True:
                            self.gameProgress = False
                        else:
                            self.turnPlayer = self.player2
            elif rowMove == 3:
                if self.row3[colMove] == '':
                    if self.turnPlayer == self.player2:
                        self.row3[colMove] = 'x'
                        if self.isGameFinished() == True:
                            self.gameProgress = False
                        else:
                            self.turnPlayer = self.player1
                    elif self.turnPlayer == self.player1:
                        self.row3[colMove] = 'o'
                        if self.isGameFinished() == True:
                            self.gameProgress = False
                        else:
                            self.turnPlayer = self.player2
            boardMatrix = (self.row1,self.row2,self.row3)
            print(boardMatrix) #can be commented out
                    

    def isBoardFull(self):
        boardFull = True
        boardMatrix = (self.row1,self.row2,self.row3)
        for rows in boardMatrix:
            for space in rows:
                if space == '':
                    boardFull = False
        return boardFull
                


    def isGameFinished(self):
        col1 = [self.row1[0],self.row2[0],self.row3[0]]
        col2 = [self.row1[1],self.row2[1],self.row3[1]]
        col3 = [self.row1[2],self.row2[2],self.row3[2]]
        diag1 = [self.row1[0],self.row2[1],self.row3[2]]
        diag2 = [self.row1[2],self.row2[1],self.row3[0]]

        if self.row1 == ['x','x','x']:
            self.p2win += 1
            self.p1loss += 1
            self.recordGamePlayed()
            return True
        elif self.row2 == ['x','x','x']:
            self.p2win += 1
            self.p1loss += 1
            self.recordGamePlayed()
            return True
        elif self.row3 == ['x','x','x']:
            self.p2win += 1
            self.p1loss += 1
            self.recordGamePlayed()
            return True
        elif self.row1 == ['o','o','o']:
            self.p1win += 1
            self.p2loss += 1
            self.recordGamePlayed()
            return True
        elif self.row2 == ['o','o','o']:
            self.p1win += 1
            self.p2loss += 1
            self.recordGamePlayed()
            return True
        elif self.row3 == ['o','o','o']:
            self.p1win += 1
            self.p2loss += 1
            self.recordGamePlayed()
            return True
        elif col1 == ['x','x','x']:
            self.p2win += 1
            self.p1loss += 1
            self.recordGamePlayed()
            return True
        elif col2 == ['x','x','x']:
            self.p2win += 1
            self.p1loss += 1
            self.recordGamePlayed()
            return True
        elif col3 == ['x','x','x']:
            self.p2win += 1
            self.p1loss += 1
            self.recordGamePlayed()
            return True
        elif col1 == ['o','o','o']:
            self.p1win += 1
            self.p2loss += 1
            self.recordGamePlayed()
            return True
        elif col2 == ['o','o','o']:
            self.p1win += 1
            self.p2loss += 1
            self.recordGamePlayed()
            return True
        elif col3 == ['o','o','o']:
            self.p1win += 1
            self.p2loss += 1
            self.recordGamePlayed()
            return True
        elif diag1 == ['x','x','x']:
            self.p2win += 1
            self.p1loss += 1
            self.recordGamePlayed()
            return True
        elif diag2 == ['x','x','x']:
            self.p2win += 1
            self.p1loss += 1
            self.recordGamePlayed()
            return True
        elif diag1 == ['o','o','o']:
            self.p1win += 1
            self.p2loss += 1
            self.recordGamePlayed()
            return True
        elif diag2 == ['o','o','o']:
            self.p1win += 1
            self.p2loss += 1
            self.recordGamePlayed()
            return True
        elif self.isBoardFull() == True:
            self.p1tie += 1
            self.p2tie += 1
            self.recordGamePlayed()
            return True
        else:
            return False
        
            
    def computeStats(self):
        players = (self.player1, self.player2) 
        lastTurn = self.player2
        if self.turnPlayer == self.player2:
            lastTurn = self.player1
        elif self.turnPlayer == self.player1:
            lastTurn = self.player2
        totalGames = self.numGames 
        totalWins = (self.p1win,self.p2win) 
        totalTies = (self.p1tie,self.p2tie) 
        totalLosses = (self.p1loss,self.p2loss)
        return players, lastTurn, totalGames, totalWins, totalTies, totalLosses


"""
class boardUI():
    board = ()
    r11 = ''
    r12 = ''
    r13 = ''
    r21 = ''
    r22 = ''
    r23 = ''
    r31 = ''
    r32 = ''
    r33 = ''
    p1Name = ''
    p2Name = ''
    lastTurnPlayer = ''
    thisTurnPlayer = ''
    totalGames = ''
    p1WinsUI = ''
    p2WinsUI = ''
    p1TiesUI = ''
    p2TiesUi = ''
    p1LossesUI = ''
    p2LossesUI = ''
    resetMessageUI = ''


    def __init__(self):
        self.board = BoardClass()
        self.canvasSetup()
        self.uiVar()
        self.createButtons()
        self.statLabel()
        self.runUI()


    def uiVar(self):
        self.r11 = tkinter.StringVar()
        self.r12 = tkinter.StringVar()
        self.r13 = tkinter.StringVar()
        self.r21 = tkinter.StringVar()
        self.r22 = tkinter.StringVar()
        self.r23 = tkinter.StringVar()
        self.r31 = tkinter.StringVar()
        self.r32 = tkinter.StringVar()
        self.r33 = tkinter.StringVar()
        self.p1Name = tkinter.StringVar()
        self.p2Name = tkinter.StringVar()
        self.lastTurnPlayer = tkinter.StringVar()
        self.thisTurnPlayer = tkinter.StringVar()
        self.totalGames = tkinter.StringVar()
        self.p1WinsUI = tkinter.StringVar()
        self.p2WinsUI = tkinter.StringVar()
        self.p1TiesUI = tkinter.StringVar()
        self.p2TiesUI = tkinter.StringVar()
        self.p1LossesUI = tkinter.StringVar()
        self.p2LossesUI = tkinter.StringVar()
        self.resetMessageUI = tkinter.StringVar()


    def uiUpdate(self):
        self.r11.set(self.board.row1[0])
        self.r12.set(self.board.row1[1])
        self.r13.set(self.board.row1[2])
        self.r21.set(self.board.row2[0])
        self.r22.set(self.board.row2[1])
        self.r23.set(self.board.row2[2])
        self.r31.set(self.board.row3[0])
        self.r32.set(self.board.row3[1])
        self.r33.set(self.board.row3[2])
        statTuple = self.board.computeStats()
        self.p1Name.set('P1: ' + statTuple[0][0])
        self.p2Name.set('P2: ' + statTuple[0][1])
        self.lastTurnPlayer.set('Last Turn: ' + statTuple[1])
        self.thisTurnPlayer.set('This Turn: ' + self.board.turnPlayer)
        if self.board.gameProgress == False:
            self.totalGames.set('Total Games: ' + str(statTuple[2]))
            self.p1WinsUI.set('P1 Wins: ' + str(statTuple[3][0]))
            self.p2WinsUI.set('P2 Wins: ' + str(statTuple[3][1]))
            self.p1TiesUI.set('P1 Ties: ' + str(statTuple[4][0]))
            self.p2TiesUI.set('P2 Ties: ' + str(statTuple[4][1]))
            self.p1LossesUI.set('P1 Losses: ' + str(statTuple[5][0]))
            self.p2LossesUI.set('P2 Losses: ' + str(statTuple[5][1]))
            self.resetMessageUI.set('Do you want to play again?')
        else:
            self.totalGames.set('')
            self.p1WinsUI.set('')
            self.p2WinsUI.set('')
            self.p1TiesUI.set('')
            self.p2TiesUI.set('')
            self.p1LossesUI.set('')
            self.p2LossesUI.set('')
            self.resetMessageUI.set('')
        
        

    def canvasSetup(self):
        self.master = tkinter.Tk()
        self.master.title('Tic-Tac-Toe: Edward Chang')
        self.master.geometry('500x500')


    def gameLoop(self):
        pass

    def createButtons(self):
        self.r1c1 = tkinter.Button(self.master,textvariable=self.r11,command=lambda:[self.board.playMoveOnBoard(1,0),self.uiUpdate()],height='4',width='8').grid(row=2,column=2)
        self.r1c2 = tkinter.Button(self.master,textvariable=self.r12,command=lambda:[self.board.playMoveOnBoard(1,1),self.uiUpdate()],height='4',width='8').grid(row=2,column=3)
        self.r1c3 = tkinter.Button(self.master,textvariable=self.r13,command=lambda:[self.board.playMoveOnBoard(1,2),self.uiUpdate()],height='4',width='8').grid(row=2,column=4)
        self.r2c1 = tkinter.Button(self.master,textvariable=self.r21,command=lambda:[self.board.playMoveOnBoard(2,0),self.uiUpdate()],height='4',width='8').grid(row=3,column=2)
        self.r2c2 = tkinter.Button(self.master,textvariable=self.r22,command=lambda:[self.board.playMoveOnBoard(2,1),self.uiUpdate()],height='4',width='8').grid(row=3,column=3)
        self.r2c3 = tkinter.Button(self.master,textvariable=self.r23,command=lambda:[self.board.playMoveOnBoard(2,2),self.uiUpdate()],height='4',width='8').grid(row=3,column=4)
        self.r3c1 = tkinter.Button(self.master,textvariable=self.r31,command=lambda:[self.board.playMoveOnBoard(3,0),self.uiUpdate()],height='4',width='8').grid(row=4,column=2)
        self.r3c2 = tkinter.Button(self.master,textvariable=self.r32,command=lambda:[self.board.playMoveOnBoard(3,1),self.uiUpdate()],height='4',width='8').grid(row=4,column=3)
        self.r3c3 = tkinter.Button(self.master,textvariable=self.r33,command=lambda:[self.board.playMoveOnBoard(3,2),self.uiUpdate()],height='4',width='8').grid(row=4,column=4)
        self.resetButton = tkinter.Button(self.master,text='reset',command=lambda:[self.board.resetGameBoard(),self.uiUpdate()]).grid(row=10,column=5)
        self.quitButton = tkinter.Button(self.master,text='quit',command=quit).grid(row=10,column=6)


    def statLabel(self):
        self.p1NameLabel = tkinter.Label(self.master,textvariable=self.p1Name).grid(row=4,column=5)
        self.p2NameLabel = tkinter.Label(self.master,textvariable=self.p2Name).grid(row=4,column=6)
        self.lastTurnLabel = tkinter.Label(self.master,textvariable=self.lastTurnPlayer).grid(row=2,column=5)
        self.thisTurnLabel = tkinter.Label(self.master,textvariable=self.thisTurnPlayer).grid(row=2,column=6)
        self.numGamesLabel = tkinter.Label(self.master,textvariable=self.totalGames).grid(row=3,column=5)
        self.p1WinsLabel = tkinter.Label(self.master,textvariable=self.p1WinsUI).grid(row=5,column=5)
        self.p2WinsLabel = tkinter.Label(self.master,textvariable=self.p2WinsUI).grid(row=5,column=6)
        self.p1TiesLabel = tkinter.Label(self.master,textvariable=self.p1TiesUI).grid(row=6,column=5)
        self.p2TiesLabel = tkinter.Label(self.master,textvariable=self.p2TiesUI).grid(row=6,column=6)
        self.p1LossesLabel = tkinter.Label(self.master,textvariable=self.p1LossesUI).grid(row=7,column=5)
        self.p2LossesLabel = tkinter.Label(self.master,textvariable=self.p2LossesUI).grid(row=7,column=6)
        self.resetLabel = tkinter.Label(self.master,textvariable=self.resetMessageUI).grid(row=9,column=5)
        
    
    def miscButtons(self):
        pass


    def runUI(self):
      self.master.mainloop()


if __name__ == '__main__':
    test = boardUI()
"""
