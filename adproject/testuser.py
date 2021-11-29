import unittest

from cardlist import Cardlist

from user import User


class TestUser(unittest.TestCase):
    
    def setUp(self):
        self.g1 = User()
    def tearDown(self):
        pass
    
    def test__init__(self):
        self.assertEqual(self.g1.player1, [])
        self.assertEqual(self.g1.player2, [])
        self.assertEqual(self.g1.field, [])
    #리스트형성    
    def testcardExtraction(self):
        self.assertEqual(len(self.g1.playerChoice()), 2)
        self.assertEqual(len(self.g1.flop()), 3)
        self.assertEqual(len(self.g1.turn()), 4)
        self.assertEqual(len(self.g1.river()), 5)
    
if __name__ == '__main__':
    unittest.main()