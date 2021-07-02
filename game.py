from Player import Player
from GameEngine import GameEngine
from Coin import Coin
from ScoreBoard import ScoreBoard

def game():
    player = Player()
    player.set_name()
    player.set_guess()
    guess = player.get_guess()
    coin = Coin()
    coin.set_value()
    flip= coin.get_value()
    print('the coin is ',flip,' and your guess is ',guess)
    re = engine.compare(flip,guess)
    player.set_score(re)
    Board.save_data(player)
    Board.print_data()







engine = GameEngine()
Board = ScoreBoard()

while engine.gameIsRun() :
    num =engine.getNumOfPlayers()
    
    if num == 'q' :
        engine.end_game()
        
        
    elif num == '1' :
        game()
    elif num == 2 :
        for i in range(2):
            game()
    else :
        for i in range(3):
            game()
        

