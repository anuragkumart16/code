import random
A=int(input("eneter"))
while A>=95 and A<100:
    print()
    print()
    print()
    dice=random.randint(1,6)
                
    print("Dice count is",dice)
    A=A+dice
    print("piece position",A)
    
    if A>100:
        print("you gained",A-100,"steps more")
        
        A=A-dice
        print("roll the dice again")
    elif A<100:
        print("roll the dice again")
    elif A==100:
        print("you won!!!")

            
