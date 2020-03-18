from random import randrange
from math import ceil

def roller():
    money = 500
    money = int(money)
    while money > 0:
        print("you got", money,"$")
        amount = input("choisissez le montant que vous misez :")
        amount = int(amount)
        win = amount * 3
        almost = ceil(amount / 2)

        bet = input("choisissez un nombre entre 0 et 49 : ")
        bet = int(bet)
        number = randrange(50)
        if bet == number:
            money += win
            print("you win : ", win)
        elif bet % 2 == number % 2:
            money += almost
            print("presque mais vous gagnez quand même : ", almost)
        else:
            print("you lose : ", amount)
            money -= amount
roller()
print("si vous désirez hypothequer votre maison pour continuer tapez 1 sinon, tapez 2")
choice = input("1 ou 2 : ")
choice = int(choice)
if choice == 1:
    roller()
elif choice == 2:
    print(" aie! tapez moins fort! ..tampis à demain")
else:
    print("are you kidding me?! Fine, i'm out of here")

