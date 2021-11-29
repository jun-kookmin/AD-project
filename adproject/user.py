from cardlist import Cardlist
from random import shuffle, randint

class User():
    # 베팅의 최소금액은 10 으로 설정, 베팅은 항상 player1이 먼저한다고 규정
    def __init__(self):
        self.card = Cardlist()
        #플레이어 카드
        self.player1 = []
        self.player2 = []
        #필드 카드
        self.field = []
        #필드 칩, 플레이어의 칩
        self.fieldMoney = 0
        self.player1Chip = 100
        self.player2Chip = 100
        # 순서구분 0은 플레이어 1의 턴, 1은 2의 턴
        self.playerTurn = 0
        self.cnt = -1
        
        
    def playerChoice(self):
        shuffle(self.card.cardlist)
        for i in range(2):
            a = randint(0, len(self.card.cardlist) - 1)
            self.player1.append(self.card.cardlist[a])
            self.card.cardlist.remove(self.card.cardlist[a])
            
            b = randint(0, len(self.card.cardlist) - 1)       
            self.player2.append(self.card.cardlist[b])  
            self.card.cardlist.remove(self.card.cardlist[b])
        return self.player1, self.player2    
        
    def flop(self):
        for i in range(3):
            a = randint(0, len(self.card.cardlist) - 1)
            self.field.append(self.card.cardlist[a])
            self.card.cardlist.remove(self.card.cardlist[a])
        return self.field
            
    def turn(self):
        a = randint(0, len(self.card.cardlist) - 1)
        self.field.append(self.card.cardlist[a])
        self.card.cardlist.remove(self.card.cardlist[a])
        return self.field
        
    def river(self):
        a = randint(0, len(self.card.cardlist) - 1)
        self.field.append(self.card.cardlist[a])
        self.card.cardlist.remove(self.card.cardlist[a])
        return self.field
    
    def displayCard(self):
        if self.playerTurn == 0:
            return self.player1[0] + self.player1[1]
        else:
            return self.player2[0] + self.player2[1]
    
    def displayField(self):
        self.cnt += 1
        if self.cnt == 0:
            return self.field[0] + self.field[1] + self.field[2]
        if self.cnt == 1:
            return self.field[0] + self.field[1] + self.field[2] + self.field[3]
        if self.cnt == 2:
            return self.field[0] + self.field[1] + self.field[2] + self.field[3] + self.field[4]
