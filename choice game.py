print('this is my first game')

'''
this is another way to make a comment
str "hello" 'hi' "69"
int 8, 9 ,-100,6900
float 6.0, 7.5, -.05, 10000.0
bool true, false
'''
health = 10



name = input("what is your name?")
age = int(input('how old are you '+ name + '? ' ))
 
print('hello',name,"you are",age,'years old')

is_older = age >= 18




#elif also works as else if
if age >= 18:
    print('youre old enough to play')

    want_to_play = input('do you want to play? ').lower()
    if want_to_play == "yes":
        print('lets play')
        print('youre starting with', health,"health")
        left_or_right = input('first choice... left or right (left/right)? ')
        if left_or_right == "left":
            ans = input("you follow the path. do you cross the bridge or go through the woods (bridge/woods)? ")
            if ans == "bridge":
                 print('you won')
            if ans == "woods":
                print('you lost 5 health because a snake bit you')
                health -=5
            ans = input('you see a house or a tower what do you pick(tower/house)? ')
            if ans == "house":
                print('you goto the house and get shot by the owner losing 5 health')
                health -= 5
                if health <=0:
                    print('you now have 0 health and died')
            elif ans == "tower":
                print('you get turned into a frog by a wizard')

           

        elif left_or_right == "right":
            print("you fell through the trapdoor and died")
    else:
        print('bye loser')
if age < 18: 
    print('youre too young for me')











