import tkinter as tk
import random
import time



last_time = time.time()
gold = 0
miner_cost = 10
miner = 0
gpc = 1
iuc = 1000
idlerunning = False

def on_click():
    global gold,gpc
    gold += gpc
    label.config(text=f"Gold: {gold}")

def upgrade():
    global gold,gpc,miner,miner_cost
    if gold >= miner_cost:
        gold -= miner_cost
        miner_cost = int(miner_cost*1.5)
        miner += 1
        gpc += 1

        label.config(text=f"Gold: {gold}")
        upgrade_button.config(text=f"buy miner ({miner_cost} gold)")

def idleincome():
    global gold
    gold += 1
    label.config(text=f"Gold: {gold}")
    window.after(1000,idleincome)
                 

    
def idle():
    global gold, iuc, idlerunning

    if gold >= iuc and not idlerunning:
        gold -= iuc
        iuc = int(iuc * 5)
        idlerunning = True

        idleincome()

        label.config(text=f"Gold: {gold}")
        idlebutton.config(text=f"Buy Idle Upgrade ({iuc} gold)")

  


window = tk.Tk()
window.title("1st visual python game")
window.geometry('400x300')
label = tk.Label(window,text="Gold: 0")
label.pack()
button = tk.Button(window,text="mine gold", command=on_click)
button.pack()
upgrade_button = tk.Button(window,text="buy miner (10 gold)", command=upgrade)
upgrade_button.pack()
idlebutton = tk.Button(window,text='buy idle upgrade (1000 gold)',command=idle)
idlebutton.pack()
window.mainloop()
