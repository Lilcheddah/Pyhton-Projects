#Choice Game No tutorial
#Choice Game No tutorial
# user info
name = input('whatis your name? ')
age = int(input(name + ' how old are you? '))

# age verification and game start
def ageverify():
    if age < 18:
        print('sorry you cannot play my game')
        exit()

def gamestart():
    ans = input(name + ' Would you Like to play my game?(yes/no)? ').lower()
    if ans == 'no':
        print('cya loser')
        exit()
    return

ageverify()
gamestart()
print('Welcome to The Game')
print('you have 10 health')
print('can you survive?')

health = 10
# starting left choices

leftright = input('Do you want to go left or right (left/right)? ').lower()
if leftright == 'left':
    print('you stumble upon a cemetery')
    ans = input('would you like to follow the path or go in the cemetery(path/cemetery)? ').lower()
    if ans == 'path':
        print('you get mugged by a homeless person causing you to lose 5 health')
        health -= 5
        ans = input('youve made it to the town you see a bar and a hotel where would you like to go(bar/hotel)? ').lower()
        if ans == 'bar':
            print('you got too drunk and started a fight you won the fight but lost 5 health')
            health -= 5
            if health <= 0:
                print('you have died')
                exit()
        elif ans == 'hotel':
            print('you book a room with the shady owner and they give you a free water')
            print('the water turned out to be posioned you lose 5 health')
            health -= 5
            if health <= 0:
                print('you have died')
                exit()
        exit()
    elif ans == 'cemetery':
        print('its spooky but peaceful youve made it thru')
        ans = input('after making thru the cemetery you find a bridge and a forest trail where do you go (bridge/trail)? ').lower()
        if ans == 'bridge':
            print('the bridge has collapsed and you lose 10 health')
            health -= 10
            if health <= 0:
                print('you have died')
                exit()
        elif ans == 'trail':
            print('you find a fairy village and they welcome you')
            print('congrats youve become immortal youve won')
            exit()

# right choices
if leftright == 'right':
    print('you go towards the storm')
    ans = input('do you want to seek shelter at the creepy cabin or keep walking (cabin/walk)? ').lower()
    if ans == 'cabin':
        ans = input('no ones home but you see a pentagram do you light the candles(yes/no)? ').lower()
        if ans == 'yes':
            print('youve started the boss fight good luck')
        elif ans == 'no':
            print('the owner of the creepy cabin comes home while youre sleeping and murders you')
            exit()
    elif ans == 'walk':
        print('you slipped during your walk causing you to lose 5 health')
        health -= 5
        ans = input('you see a tower and castle where do you go (tower/castle)? ').lower()
        if ans == 'tower':
            print('you walk into the tower and a witch casts a spell causing you to lose 5 health')
            health -= 5
            if health <= 0:
                print('you ded')
                exit()
        elif ans == 'castle':
            print('as you cross the bridge to the castle you fall into the mote dying to aligators')
            exit()