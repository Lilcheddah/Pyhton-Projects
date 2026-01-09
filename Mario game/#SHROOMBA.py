#SHROOMBA
import time
class Shroomba:
    def __init__(self):
        self.health = 1
        self.damage = 1
        self.speed = 1
        # ai position 
        self.x = 0
        self.y = 0
        #velocity
        self.vx = 0
        self.vy = 0

    def move(self):
        if self.x <= 0:
            
            self.vx = self.speed
        elif self.x >= 10:
            
            self.vx = -self.speed
    
    def update(self):

        self.x += self.vx
        self.y += self.vy


        print("Position: ", self.x)


        pass

enemy=Shroomba()

while True:
    enemy.move()
    enemy.update()
    time.sleep(.3)

