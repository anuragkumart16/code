Number=int(input("Enter Three Digit no."))
for a in range(1,3):
    b=Number%100
    c=Number//100
    print(c)
    print(b)
    Number=b    
print(Number)