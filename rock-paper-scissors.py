#Rock,Paper,Scissors
import random
import os
from tkinter import *

class option():
    def __init__(self,value):
        self.value = value
    def beats(self,other):
        if self.value == 'rock' and other.value == 'scissors':
            return 1
        elif self.value == 'rock' and other.value == 'paper':
            return 2
        elif self.value == 'paper' and other.value == 'scissors':
            return 2
        elif self.value == 'paper' and other.value == 'rock':
            return 1
        elif self.value == 'scissors' and other.value == 'rock':
            return 2
        elif self.value == 'scissors' and other.value == 'paper' :
            return 1
        elif self.value == other.value:
            return 0
    def print(self,a):
        print(str(a)+':'+str(self.value))
    def get(self):
        return str(self.value)
def main():
    highscore = 0
    list=['rock','paper','scissors']
    solution = 0
    playing = 1
    while playing == 1:    
        while solution == 0:
            print('Highscore:'+str(highscore))
            players_move = input('Rock,paper or scissors: ')
            cls()
            computers_move = list[random.randint(0,2)]
            p = option(players_move)
            c = option(computers_move)
            solution = p.beats(c)
            if solution == 0 :
                cls()
                print('Pick again because you both picked:'+c.get())
        if solution == 1:
            cls()
            highscore += 1
            print('Highscore:'+str(highscore))
            print('Player wins!')
            p.print('Player')
            c.print('Computer')
            
        elif solution == 2:
            cls()
            print('Highscore:'+str(highscore))
            print('Computer wins!')
            p.print('Player')
            c.print('Computer')
            highscore = 0
        if int(input('Want to play again(0,1):')) == 1 :
           solution = 0
           cls()
        else:
            playing = 0



def cls():
    os.system('cls' if os.name == 'nt' else 'clear')    

if __name__ == "__main__":
    main()



