#idle game
import time
import random

gold = 0
gold_per_second = 1
running = True
last_time = time.time()
miners = 0
superminer = 0
miner_cost = 10
smcost = 50

while running:
    current_time = time.time()
    delta = current_time - last_time
    last_time = current_time
    gold += gold_per_second * delta
     
    
    
    
    
    if gold > miner_cost:
        gold -= miner_cost
        miners += 1
        gold_per_second += 1
        miner_cost = int(miner_cost * 1.5)
        
        if miners >= 20:
            miner_cost = int(miner_cost * 3)

    
    if gold > smcost:
        command = input('would you like to buy a super miner? ').lower()
        if command == "yes":
            gold -= smcost
            superminer += 1
            gold_per_second += 2.5
            smcost = int(smcost * 10)

        elif command == "no":
            print('okay ill ask later')
            time.sleep(15)

    if gold >= 10000:
        print("youve won")
        break
    
        
    print(f"Gold: {int(gold)},GPS: {int(gold_per_second)},Miners: {miners}, Superminers: {superminer}")
    time.sleep(1)

   
   

       

   