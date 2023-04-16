principle=int(input("enter principle"))
rate=int(input("enter rate of interest"))
time=int(input("enter the time (in years)"))
simple_interest=0
simple_interest=principle*rate*time/100
print(simple_interest,"is the the simple interest")
amount=simple_interest+principle
print(amount,"is the amount")
