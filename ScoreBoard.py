import csv
from os import write
class ScoreBoard :
    def __init__(self) -> None:
        with open("players.csv",'w+') as file :
            writer = csv.writer(file)
            writer.writerow(['name','score'])


    def save_data(self,player):
        with open("players.csv","a+") as file :
            writer = csv.writer(file)
            writer.writerow([player.get_name(),player.get_score()])
    def print_data(self):
        with open('players.csv') as file :
            reader = csv.DictReader(file)
            for player in reader :
                print(player['name'],"'s score is ",player['score'])
    
