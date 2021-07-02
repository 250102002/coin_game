

class GameEngine:
    __play = True
    def gameIsRun(self): 
         return self.__play
    
    def getNumOfPlayers(self):
        num = input("Enter the number of players from (1,2,3) or q for end the game : ").strip()
        if num not in ['1','2','3','q'] :
            print("Enter a valid value form ['1','2','3','q'] ...")
            self.getNumOfPlayers()
        return num


    def compare(self,flip,guess):
        if flip == guess :
            return True
        else :
            return False


    def end_game(self):
        self.__play=False
        return self.__play
        