import random
import time


def playerinfo():
    name = input('what is your name ? ').lower()
    yesno = input(name + ' would you like to play a battle game? ').lower()
    if yesno == 'no':
        print('you werent gonna win anyway')
        return
    elif yesno == 'yes':
        print('Lets Get Started!')

# health system
def health():
    player_health = 10
    enemy_health =20


    print('You have 10 health and your oppenant has 20')
    time.sleep(1)
    print('Will you prove worthy?')
    time.sleep(1)

    while player_health > 0 and enemy_health > 0:
        print('your health', player_health)
        print('enemy health', enemy_health)
        time.sleep(1)

        #player turn
        choice = input('attack or heal? ').lower()
        x = random.randint(0,6)
        y = random.randint(1,4)
        if choice == 'attack':
            enemy_health -= x
            print('youve done ', x,'damage')
        elif choice == 'heal':
            player_health += y
            print('youve healed', y,'health')
        time.sleep(1)

        #enemy turn
        if enemy_health > 0:
            damage = random.randint(1,4)
            heal = random.randint(1,3)
            print('your enemy is thinking')
            time.sleep(2)
            enemymove = random.randint(1,2)
            if enemymove == 1:
             print('they attack causing', damage, "damage")
             player_health -= damage
            elif enemymove == 2:
                print('your enemy heals for',heal,'hp')
                enemy_health += heal
    # loop finished when someone reaches 0 HP
    if player_health <= 0:
        time.sleep(1)
        print('You have been defeated.')
    elif enemy_health <= 0:
        time.sleep(1)
        print('You defeated the enemy!')
    return
playerinfo()
health()



        




