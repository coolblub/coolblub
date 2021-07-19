import socket, tkinter, gameboard, threading
from tkinter import ttk

class boardUI():
    mainSocket = None
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
    p1NameTemplate = ''
    p2NameTemplate = ''
    lastTurnPlayer = ''
    thisTurnPlayer= ''
    totalGames = ''
    p1WinsUI = ''
    p2WinsUI = ''
    p1TiesUI = ''
    p2TiesUi = ''
    p1LossesUI = ''
    p2LossesUI = ''
    resetMessageUI = ''
    serverAddress = ''
    serverPort = ''
    clientSocket = ''
    clientAddress = ''
    clientQuit = ''


    def __init__(self):
        self.mainSocket = None
        self.clientSocket = None
        self.clientAddress = None
        self.clientQuit = False
        self.board = gameboard.BoardClass()
        self.canvasSetup()
        self.uiVar()
        self.createButtons()
        self.statLabel()
        self.serverInfo()
        self.miscButtons()
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
        self.continueVar = tkinter.StringVar()
        self.p1NameTemplate = tkinter.StringVar()
        self.p2NameTemplate = tkinter.StringVar()
        self.lastTurnPlayer = tkinter.StringVar()
        self.thisTurnPlayer = tkinter.StringVar()
        self.totalGames = tkinter.StringVar()
        self.p1WinsUI = tkinter.StringVar()
        self.p2WinsUI = tkinter.StringVar()
        self.p1TiesUI = tkinter.StringVar()
        self.p2TiesUI = tkinter.StringVar()
        self.p1LossesUI = tkinter.StringVar()
        self.p2LossesUI = tkinter.StringVar()
        self.serverAddress = tkinter.StringVar()
        self.serverPort = tkinter.IntVar()
        #self.resetMessageUI = tkinter.StringVar() #for player 2 to see


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
        self.p1NameTemplate.set('P1: ' + self.p1Name.get())
        self.p2NameTemplate.set('P2: ' + self.p2Name.get())
        self.lastTurnPlayer.set('Last Turn: ' + statTuple[1])
        self.thisTurnPlayer.set('This Turn: ' + self.board.turnPlayer)
        if self.board.gameProgress == False or self.clientQuit == True:
            self.totalGames.set('Total Games: ' + str(statTuple[2]))
            self.p1WinsUI.set('P1 Wins: ' + str(statTuple[3][0]))
            self.p2WinsUI.set('P2 Wins: ' + str(statTuple[3][1]))
            self.p1TiesUI.set('P1 Ties: ' + str(statTuple[4][0]))
            self.p2TiesUI.set('P2 Ties: ' + str(statTuple[4][1]))
            self.p1LossesUI.set('P1 Losses: ' + str(statTuple[5][0]))
            self.p2LossesUI.set('P2 Losses: ' + str(statTuple[5][1]))
            #self.resetMessageUI.set('Do you want to play again?') #for player2
        else:
            self.totalGames.set('')
            self.p1WinsUI.set('')
            self.p2WinsUI.set('')
            self.p1TiesUI.set('')
            self.p2TiesUI.set('')
            self.p1LossesUI.set('')
            self.p2LossesUI.set('')
        

    def canvasSetup(self):
        self.master = tkinter.Tk()
        self.master.title('Tic-Tac-Toe: Edward Chang. Name/ I.P./ Port')
        self.master.geometry('700x500')


    def createButtons(self):
        self.r1c1 = tkinter.Button(self.master,textvariable=self.r11,command=lambda:[self.board.playMoveOnBoard(1,0),self.uiUpdate(),self.sendMove(1,0)],height='4',width='8').grid(row=2,column=1)
        self.r1c2 = tkinter.Button(self.master,textvariable=self.r12,command=lambda:[self.board.playMoveOnBoard(1,1),self.uiUpdate(),self.sendMove(1,1)],height='4',width='8').grid(row=2,column=2)
        self.r1c3 = tkinter.Button(self.master,textvariable=self.r13,command=lambda:[self.board.playMoveOnBoard(1,2),self.uiUpdate(),self.sendMove(1,2)],height='4',width='8').grid(row=2,column=3)
        self.r2c1 = tkinter.Button(self.master,textvariable=self.r21,command=lambda:[self.board.playMoveOnBoard(2,0),self.uiUpdate(),self.sendMove(2,0)],height='4',width='8').grid(row=3,column=1)
        self.r2c2 = tkinter.Button(self.master,textvariable=self.r22,command=lambda:[self.board.playMoveOnBoard(2,1),self.uiUpdate(),self.sendMove(2,1)],height='4',width='8').grid(row=3,column=2)
        self.r2c3 = tkinter.Button(self.master,textvariable=self.r23,command=lambda:[self.board.playMoveOnBoard(2,2),self.uiUpdate(),self.sendMove(2,2)],height='4',width='8').grid(row=3,column=3)
        self.r3c1 = tkinter.Button(self.master,textvariable=self.r31,command=lambda:[self.board.playMoveOnBoard(3,0),self.uiUpdate(),self.sendMove(3,0)],height='4',width='8').grid(row=4,column=1)
        self.r3c2 = tkinter.Button(self.master,textvariable=self.r32,command=lambda:[self.board.playMoveOnBoard(3,1),self.uiUpdate(),self.sendMove(3,1)],height='4',width='8').grid(row=4,column=2)
        self.r3c3 = tkinter.Button(self.master,textvariable=self.r33,command=lambda:[self.board.playMoveOnBoard(3,2),self.uiUpdate(),self.sendMove(3,2)],height='4',width='8').grid(row=4,column=3)


    def statLabel(self):
        self.p1NameLabel = tkinter.Label(self.master,textvariable=self.p1NameTemplate).grid(row=4,column=5)
        self.p2NameLabel = tkinter.Label(self.master,textvariable=self.p2NameTemplate).grid(row=4,column=6)
        self.lastTurnLabel = tkinter.Label(self.master,textvariable=self.lastTurnPlayer).grid(row=2,column=6)
        self.thisTurnLabel = tkinter.Label(self.master,textvariable=self.thisTurnPlayer).grid(row=2,column=5)
        self.numGamesLabel = tkinter.Label(self.master,textvariable=self.totalGames).grid(row=3,column=5)
        self.p1WinsLabel = tkinter.Label(self.master,textvariable=self.p1WinsUI).grid(row=5,column=5)
        self.p2WinsLabel = tkinter.Label(self.master,textvariable=self.p2WinsUI).grid(row=5,column=6)
        self.p1TiesLabel = tkinter.Label(self.master,textvariable=self.p1TiesUI).grid(row=6,column=5)
        self.p2TiesLabel = tkinter.Label(self.master,textvariable=self.p2TiesUI).grid(row=6,column=6)
        self.p1LossesLabel = tkinter.Label(self.master,textvariable=self.p1LossesUI).grid(row=7,column=5)
        self.p2LossesLabel = tkinter.Label(self.master,textvariable=self.p2LossesUI).grid(row=7,column=6)
        self.resetLabel = tkinter.Label(self.master,textvariable=self.resetMessageUI).grid(row=9,column=5)
        self.continueMessageLabel = tkinter.Label(self.master,textvariable=self.continueVar).grid(row=10,column=5)



        
    
    def miscButtons(self):
        #self.resetButton = tkinter.Button(self.master,text='reset',command=lambda:[self.board.resetGameBoard(),self.uiUpdate()]).grid(row=10,column=5)
        self.quitButton = tkinter.Button(self.master,text='quit',command=self.onlineQuit).grid(row=10,column=6)
        self.serverButton = tkinter.Button(self.master,text='start server',command=self.serverSetup).grid(row=1,column=7)

    def serverInfo(self):
        self.p1NameInput = tkinter.Entry(self.master,textvariable=self.p1Name).grid(row=1,column=4)
        self.serverAddressInput = tkinter.Entry(self.master,textvariable=self.serverAddress).grid(row=1,column=5)
        self.serverPortInput = tkinter.Entry(self.master,textvariable=self.serverPort).grid(row=1,column=6)


    def serverSetup(self):
        serverAddress = self.serverAddress.get()
        Port = self.serverPort.get()
        self.mainSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.mainSocket.bind((serverAddress, Port))
        self.mainSocket.listen(1)
        self.acceptInputsThread()


    def acceptInputsThread(self):
        self.clientSocket, self.clientAddress = self.mainSocket.accept()
        print(self.clientSocket, self.clientAddress)
        self.p2Name.set(self.clientSocket.recv(1024).decode('utf-8'))
        self.clientSocket.send(self.p1Name.get().encode('utf-8'))
        thread1 = threading.Thread(target=self.acceptInputs, args=(self.clientSocket,))
        thread1.start()


    def acceptInputs(self, clientSocket):
        while True:
            someInput = clientSocket.recv(256).decode('utf-8')
            self.opponentMoves(someInput)


    def opponentMoves(self, someInput):
        if len(someInput) == 2:
            listForm = list(someInput)
            self.board.playMoveOnBoard(int(listForm[0]),int(listForm[1]))
            self.uiUpdate()
        if someInput == 'quit':
            print('player 2 quit')
            self.clientQuit = True
            self.uiUpdate()
        if someInput == 'yes':
            self.continueVar.set('Play Again')
            self.board.resetGameBoard()
            self.uiUpdate()
        if someInput == 'noplay':
            self.continueVar.set('Fun Times')
            self.uiUpdate()
            
            
    def sendMove(self, rowMove, colMove):
        moveString = str(rowMove)+str(colMove)
        self.clientSocket.send(moveString.encode('utf-8'))
            

    def onlineQuit(self):
        self.clientSocket.send(b'quit')
        self.master.destroy()

            
    def runUI(self):
        self.master.mainloop()

        
if __name__ == '__main__':
    game = boardUI()
    
    


