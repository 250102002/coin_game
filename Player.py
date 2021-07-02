class Player :
    __name = ''
    __guess = ''
    __score = 0
    def set_name(self):
        name = input("Enter your name : ")
        self.__name = name
    def get_name(self):
        return self.__name
    def set_guess(self):
        guess = input(f"Hey {self.get_name()} ,enter your guess from (malik,ketapah) : ").strip()
        if guess not in ['malik','ketapah']:
            print("Enter a valid value from (malik,ketapah)..")
            self.set_guess()
        self.__guess = guess
        
        
    def get_guess(self):
        return self.__guess
    def set_score(self,result):
        if result == True :
            self.__score +=1
    def get_score(self):
        return self.__score
