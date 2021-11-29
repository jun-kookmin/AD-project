class Cardlist():
    
    def __init__(self):
        shape = [ "♤ ", "🧡", "♧ ", "🔸"]

        number = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "X", "J", "Q", "K"]

        cardShapeandNumber = [x + y for x in shape for y in number]


        self.cardlist = []
        for i in cardShapeandNumber:
            self.cardlist.append(''' 
                 ㅡㅡ
                |''' + i + '''|
                |     |
                 ㅡㅡ ''')
        

