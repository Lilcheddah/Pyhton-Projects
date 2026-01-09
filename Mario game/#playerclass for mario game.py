#player class for mario game


#future me pls refine this is basically a chatgpt copy make it ur own make it better add a ground stomp or an attack

class Player:
    def __init__(self):
        #basic player stats
        self.health = 3
        self.damage = 1
        self.speed = 3
        #Horizontal position 
        self.x = 0
        #Vertical 
        self.y = 0
        #directional velocity
        self.vx = 0
        self.vy = 0
        #jumping
        self.jump_force = 3
        self.gravity = 15
        self.on_ground = True

    def move_right(self):
        self.vx += self.speed
    
            

    def move_left(self):
        self.vx += -self.speed
    
    def stop(self):
        self.vx = 0

    def jump(self):
        if self.on_ground:
            self.vy = - self.jump_force
            self.on_ground = False
    
    def update(self):
        #gravity
        self.vy += self.gravity

        #applying velocity to position 
        self.x += self.vx
        self.y += self.vy

        #ground at y 0
        if self.y >= 0:
            self.y = 0
            self.vy = 0
            self.on_ground = True

player = Player()
while True:
    cmd = input('a=left,d=right,w=jump,s=stop: ').lower()
    if cmd == "a":
        player.move_left()
    elif cmd == "d":
        player.move_right()
    elif cmd == 'w':
        player.jump()
    elif cmd == 's':
        player.stop()

    player.update()

    print('Position : ', player.x,player.y)
