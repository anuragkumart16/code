import random
Alpha=int(input("press 1 to start"))
if Alpha==1:
    B=-1
    A=-1
    C=0
    while B==-1:
        dice=random.randint(1,6)
        print("Dice Count Is",dice)
        if dice!=6:
            print("Piece position is",A)
            print("Roll the dice Again!")

            
        elif dice==6:
            A=A+1
            print("congo!! your piece is out")
            print("Piece position is",A)
            B=1
            print("#######################################################################")
            print()            
            #After the piece is out
            while A<95:
                dice=random.randint(1,6)
                print("Dice Count Is",dice)
                A=A+dice
                print("Piece position",A)
            #Snakes And Ladders
                if A==2:
                    print("---------------------------------------")
                    print("Congo !!! A leadder")
                    A=23
                    print("position",A)
                    print("---------------------------------------")
                elif A==6:
                    print("---------------------------------------")
                    print("Congo !!! A leadder")
                    A=45
                    print("position",A)
                    print("---------------------------------------")
                elif A==20:
                    print("---------------------------------------")
                    print("Congo !!! A leadder")
                    A=42
                    print("position",A)
                    print("---------------------------------------")
                elif A==43:
                    print(".......................................")
                    print("Bitten By snake")
                    A=30
                    print("position",A)
                    print("........................................")
                elif A==56:
                    print(".......................................")
                    print("Bitten By snake")
                    A=25
                    print("position",A)
                    print("........................................")
                elif A==62:
                    print("---------------------------------------")
                    print("Congo !!! A leadder")
                    A=80
                    print("position",A)
                    print("---------------------------------------")
                elif A==68:
                    print(".......................................")
                    print("Bitten By snake")
                    A=19
                    print("position",A)
                    print("........................................")
                elif A==86:
                    print("---------------------------------------")
                    print("Congo !!! A leadder")
                    A=95
                    print("position",A)
                    print("---------------------------------------")
                
                elif A==100:
                    print("you won")
                else:
                    print("Rolling the dice Again!")
                
            #after the position of piece is greater than 95
                    
                
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
                            
        
        
        
        
        
        
