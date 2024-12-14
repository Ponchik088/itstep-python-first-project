import tkinter as tk

hp = 100
level = 1

click_pwr = 10
coins = 0
upgrade_cost = 100

auto_click = 0
auto_click_cost = 100
check_ac = False

def autoclick_upgrade():
    global coins
    global auto_click
    global auto_click_cost
    global check_ac
    if coins >= auto_click_cost:
        coins -= round(auto_click_cost)
        auto_click += 1
        auto_click_cost = round(auto_click_cost * 1.6)
        if check_ac == False:
            check_ac = True
            autoclick()
        coins_label.config(text=f"Coins: {coins}", font=("Arial", 15))
        auto_click_up.config(text = f"AutoCkick: {auto_click}, Upgrade cost: {auto_click_cost}")

def autoclick():
    global hp
    global auto_click
    hp -= auto_click
    hp_label.config(text=f"HP: {hp}")
    autoclick()

def upgrade_click():
    global coins
    global click_pwr
    global upgrade_cost
    if coins >= upgrade_cost:
        coins -= round(upgrade_cost)
        click_pwr += 1
        upgrade_cost = round(upgrade_cost * 1.5)
        coins_label.config(text=f"Coins: {coins}", font=("Arial", 15))
        upgrade_click_pwr.config(text = f"Click POWER: {click_pwr}, Upgrade cost: {upgrade_cost}")

def attack():
    global hp
    global level
    global coins
    hp -= click_pwr
    hp_label.config(text = f"HP: {hp}")
    if hp <= 0:
        coins += level * 50
        level += 1
        hp = level * 100
        hp_label.config(text=f"HP: {hp}")
        level_label.config(text=f"Level: {level}")
        coins_label.config(text=f"Coins: {coins}", font=("Arial", 15))

window = tk.Tk()
window.geometry("500x700")
window.resizable(False, False)
window.title("MegaClicker")

monster1 = tk.PhotoImage(file =r".\img\Monster1.png")
monster2 = tk.PhotoImage(file =r".\img\Monster2.png")
monster3 = tk.PhotoImage(file =r".\img\Monster3.png")
monster4 = tk.PhotoImage(file =r".\img\Monster4.png")
monster5 = tk.PhotoImage(file =r".\img\Monster5.png")

level_label = tk.Label(text=f"Level: {level}", fg="#000000", font=("Arial", 15))
level_label.pack()

monster = tk.Button(image = monster1, command=attack)
monster.pack()

if level == 2:
    monster.config(image = monster2)
elif level == 3:
    monster.config(image=monster3)

hp_label = tk.Label(text = f"HP: {hp}", font=("Arial", 15))
hp_label.pack()

coins_label = tk.Label(text = f"Coins: {coins}", font=("Arial", 15))
coins_label.pack()

upgrade_click_pwr = tk.Button(text = f"Click POWER: {click_pwr}, Upgrade cost: {upgrade_cost}", command=upgrade_click)
upgrade_click_pwr.pack()

auto_click_up = tk.Button(text = f"AutoCkick: {auto_click}, Upgrade cost: {auto_click_cost}", command=autoclick_upgrade)
auto_click_up.pack()

window.mainloop()