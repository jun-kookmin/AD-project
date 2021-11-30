
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton
from cardlist import Cardlist
from user import User


class Poker(QWidget):
    def __init__(self):
        super().__init__()
        self.init()
        self.user = User()
        self.cardlist = Cardlist()
        self.callStack = 0
        self.checkStack = 0
        self.level = 0
        
    def init(self):
        self.texasHoldemField = QTextEdit()
        self.texasHoldemField.setReadOnly(True)
        self.texasHoldemField.setAlignment(Qt.AlignCenter)
        
        self.texasHoldemPlayer = QTextEdit()
        self.texasHoldemPlayer.setReadOnly(True)
        self.texasHoldemPlayer.setAlignment(Qt.AlignCenter)
        
        texasHoldemLayout = QGridLayout()
        texasHoldemLayout.addWidget(self.texasHoldemField, 1, 1)
        
        texasHoldemLayout.addWidget(self.texasHoldemPlayer, 2, 1)
        
        buttonLayout = QGridLayout()
        
        self.buttonCheck = QToolButton()
        self.buttonCheck.setText('Check')
        self.buttonCheck.clicked.connect(self.clickedCheck)
        buttonLayout.addWidget(self.buttonCheck, 5, 0)
        
        self.buttonCall = QToolButton()
        self.buttonCall.setText('Call')
        self.buttonCall.clicked.connect(self.clickedCall)
        buttonLayout.addWidget(self.buttonCall, 5, 1)
        
        self.buttonFold = QToolButton()
        self.buttonFold.setText('Fold')
        self.buttonFold.clicked.connect(self.clickedFold)
        buttonLayout.addWidget(self.buttonFold, 5, 2)
        
        self.buttonRaise = QToolButton()
        self.buttonRaise.setText('Raise')
        self.buttonRaise.clicked.connect(self.clickedRaise)
        buttonLayout.addWidget(self.buttonRaise, 5, 3)
        
        self.buttonStart = QToolButton()
        self.buttonStart.setText('startGame')
        self.buttonStart.clicked.connect(self.startGame)
        buttonLayout.addWidget(self.buttonStart, 5, 4)
           
        self.textLayout = QGridLayout()
        #칩 관련
        self.currPlayerMoneyLable = QLabel()
        self.currPlayerMoneyLable.setText("The number of chips the player has : ")
        self.textLayout.addWidget(self.currPlayerMoneyLable, 6, 0)
        
        self.currPlayerMoney = QLineEdit()
        self.currPlayerMoney.setReadOnly(True)
        self.textLayout.addWidget(self.currPlayerMoney,6, 1)
        #플레이어 턴 관련
        self.currPlayerTurnLabel = QLabel()
        self.currPlayerTurnLabel.setText("Now Turn : ")
        self.textLayout.addWidget(self.currPlayerTurnLabel, 7, 0)
        
        self.currPlayerTurn = QLineEdit()
        self.currPlayerTurn.setReadOnly(True)
        self.textLayout.addWidget(self.currPlayerTurn,7, 1)
    
        #배팅 관련
        self.currBettingAmount = QLabel()
        self.currBettingAmount.setText("Enter the betting amount : ")
        self.textLayout.addWidget(self.currBettingAmount, 1, 0)
        
        self.inputCurrBettingAmount = QLineEdit()
        self.textLayout.addWidget(self.inputCurrBettingAmount, 1, 1)
        #현재 누적 칩 관련
        self.AccBettingAmount = QLabel()
        self.AccBettingAmount.setText("Accumulated betting amount : ")
        self.textLayout.addWidget(self.AccBettingAmount, 2, 0)
        
        self.inputAccBettingAmount = QLineEdit()
        self.inputAccBettingAmount.setReadOnly(True)
        self.textLayout.addWidget(self.inputAccBettingAmount, 2, 1)

        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(texasHoldemLayout, 0, 0)
        mainLayout.addLayout(buttonLayout, 7, 0)
        mainLayout.addLayout(self.textLayout, 0, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle('Texas holdem')

        

    def startGame(self):
        self.startGame()
            
    def clickedCheck(self):
        self.level = 0
        if self.user.playerTurn == 0:
            self.currPlayerMoney.setText(str(self.user.player1Chip))
            self.texasHoldemPlayer.setText(self.user.displayCard())
            self.inputCurrBettingAmount.setText('0')
            self.inputAccBettingAmount.setText(str(self.user.fieldMoney))
            self.currPlayerTurn.setText("now player2's turn")
            self.user.playerTurn += 1
            self.checkStack += 1
            
            if self.checkStack == 2 and self.level == 0:
                self.user.flop()
                self.texasHoldemField.setText(self.user.displayField())
                self.callStack = 0
                self.checkStack = 0
                self.level += 1
                
            elif self.checkStack == 2 and self.level == 1:
                self.user.turn()
                self.texasHoldemField.setText(self.user.displayField())
                self.callStack = 0
                self.checkStack = 0
                self.level += 1
                
            elif self.checkStack == 2 and self.level == 2:
                self.user.river()
                self.texasHoldemField.setText(self.user.displayField())
    
        else:
            self.currPlayerMoney.setText(str(self.user.player2Chip))
            self.texasHoldemPlayer.setText(self.user.displayCard())
            self.inputCurrBettingAmount.setText('0')
            self.inputAccBettingAmount.setText(str(self.user.fieldMoney))
            self.currPlayerTurn.setText("now player1's turn")
            self.user.playerTurn -= 1
            self.checkStack += 1
        
            if self.checkStack == 2 and self.level == 0:
                self.user.flop()
                self.texasHoldemField.setText(self.user.displayField())
                self.callStack = 0
                self.checkStack = 0
                self.level += 1
                
            elif self.checkStack == 2 and self.level == 1:
                self.user.turn()
                self.texasHoldemField.setText(self.user.displayField())
                self.callStack = 0
                self.checkStack = 0
                self.level += 1
                
            elif self.checkStack == 2 and self.level == 2:
                self.user.river()
                self.texasHoldemField.setText(self.user.displayField())
                


    def clickedCall(self):
        if self.user.playerTurn == 0:
            self.currPlayerMoney.setText(str(self.user.player1Chip))
            self.texasHoldemPlayer.setText(self.user.displayCard())
            self.betting(int(self.inputCurrBettingAmount.text()))
            self.currPlayerTurn.setText("now player2's turn")
            self.user.playerTurn += 1
            self.callStack += 1
            
            if self.callStack == 2 and self.level == 0:
                self.user.flop()
                self.texasHoldemField.setText(self.user.displayField())
                self.callStack = 0
                self.checkStack = 0
                self.level += 1
            
            elif self.callStack == 2 and self.level == 1:
                self.user.turn()
                self.texasHoldemField.setText(self.user.displayField())
                self.callStack = 0
                self.checkStack = 0
                self.level += 1
            
            elif self.callStack == 2 and self.level == 2:
                self.user.river()
                self.texasHoldemField.setText(self.user.displayField())
            
        else:
            self.currPlayerMoney.setText(str(self.user.player2Chip))
            self.texasHoldemPlayer.setText(self.user.displayCard())
            self.betting(int(self.inputCurrBettingAmount.text()))
            self.currPlayerTurn.setText("now player1's turn")
            self.user.playerTurn -= 1
            self.callStack += 1
            
            
            if self.callStack == 2 and self.level == 0:
                self.user.flop()
                self.texasHoldemField.setText(self.user.displayField())
                self.callStack = 0
                self.checkStack = 0
                self.level += 1
            
            elif self.callStack == 2 and self.level == 1:
                self.user.turn()
                self.texasHoldemField.setText(self.user.displayField())
                self.callStack = 0
                self.checkStack = 0
                self.level += 1
            
            elif self.callStack == 2 and self.level == 2:
                self.user.river()
                self.texasHoldemField.setText(self.user.displayField())
                        
    def clickedFold(self):
        if self.user.playerTurn == 0:
            self.user.playerTurn = 0
            self.currPlayerTurn.setText('player2 win')
            self.user.player2Chip += self.user.fieldMoney
            self.user.fieldMoney = 0
            self.inputAccBettingAmount.setText('0')
        else:
            self.currPlayerTurn.setText('player1 win')
            self.user.playerTurn = 0
            self.user.player1Chip += self.user.fieldMoney
            self.inputAccBettingAmount.setText(self.user.fieldMoney)
            
    def clickedRaise(self):
        if self.user.playerTurn == 0:
            self.texasHoldemPlayer.setText(self.user.displayCard())
            self.currPlayerMoney.setText(str(self.user.player1Chip))
            self.betting(int(self.inputCurrBettingAmount.text()))
            self.currPlayerTurn.setText("now player2's turn")
            self.user.playerTurn += 1
            
        else:
            self.texasHoldemPlayer.setText(self.user.displayCard())
            self.currPlayerMoney.setText(str(self.user.player2Chip))
            self.betting(int(self.inputCurrBettingAmount.text()))
            self.currPlayerTurn.setText("now player1's turn")
            self.user.playerTurn -= 1
            
    def betting(self, chip):
        if self.user.playerTurn == 0:
            self.user.fieldMoney += chip
            self.user.player1Chip -= chip
            self.inputAccBettingAmount.setText(str(self.user.fieldMoney))
        else:
            self.user.fieldMoney += chip
            self.user.player2Chip -= chip

            
    def startGame(self):
        self.user.playerChoice()
        self.user.player1Chip -= 10
        self.user.player2Chip -= 10
        self.user.fieldMoney = 20
        self.inputAccBettingAmount.setText(str(self.user.fieldMoney))
        self.currPlayerMoney.setText(str(self.user.player1Chip))
        self.texasHoldemPlayer.setText(self.user.displayCard())
        self.currPlayerTurn.setText("now player1's turn")
        
if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    game = Poker()
    game.show()
    sys.exit(app.exec_())
