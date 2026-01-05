import random

playagain = True
class warship:
    def __init__(self):
        self.position = random.randint(1,5)
        self.health = 3


    def move(self):
        self.position = random.randint(1,5)
    def check_hit(self,guess):
        if guess == self.position:
            self.health -= 1
            return True
        return False
        

       
            
class player:
    def __init__(self):
        self.positon = (1,5)


while playagain:
    ship = warship()
    guessesleft = 10

    while ship.health > 0 and guessesleft > 0 :
   
        ship.move()
        guess = int(input('Guess a Number 1-5: '))
        guessesleft -= 1
        x = guessesleft
        print('guesses remaining', x )
        if ship.check_hit(guess):
            print('Hit!')
        else:
            print('Miss!')     
    
    if ship.health <= 0:
      print('You sunk the Battleship!')
    if guessesleft <= 0 :
      print('You have run out of guesses')
            
    choice = input('Play again? (y/n): ').lower()
    if choice != 'y':
        playagain = False