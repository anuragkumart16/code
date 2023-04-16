#telling viwer to choose the value of 'n'
print("for how often you wanna calculate the compund interest?")
print("press 1 to calculate annually")
print("press 2 to compund half yearly")
print("press any digit other than 1 and 2 to calulate quarterly")
a=int(input())

#taking input
Principle=int(input("enter principle"))
Rate=int(input("enter rate"))
Time=int(input("enter time"))


#the arithematics
if a==1:
    #random assigning
    aplha=Rate/100
    beta=0
    aplha=1+aplha
    beta=aplha
    Amount=0
    theta=0

    #aritematics
    for b in range(1,Time):
        aplha=aplha*beta
    Amount=aplha*Principle
    print("Amount =",Amount)
    theta=Amount-Principle
    print("compound interest =",theta)
elif a==2:
        #random assigning
    aplha=Rate/200
    beta=0
    aplha=1+aplha
    beta=aplha
    Amount=0
    theta=0
    Time=Time*2

    #arithematics
    for c in range(1,Time):
        aplha=aplha*beta
    Amount=aplha*Principle
    print("Amount =",Amount)
    theta=Amount-Principle
    print("compound interest =",theta)
else:
        #random assigning
    aplha=Rate/400
    beta=0
    aplha=1+aplha
    beta=aplha
    Amount=0
    theta=0
    Time=Time*4

    #arithematics
    for c in range(1,Time):
        aplha=aplha*beta
    Amount=aplha*Principle
    print("Amount =",Amount)
    theta=Amount-Principle
    print("compound interest =",theta)


