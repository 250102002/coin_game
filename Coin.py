from numpy.random import randint 


class Coin :
    __value = ''

    def set_value(self):
        random = randint(0,2)
        sample_space = ['malik','ketapah']
        value = sample_space[random]
        self.__value = value
    def get_value(self):
        return self.__value