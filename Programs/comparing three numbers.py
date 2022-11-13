#program to compare 3 no.
a=int(input("enter any no."))
b=int(input("enter any no."))
c=int(input("enter any no."))
if a>b:
    if a>c:
        print("a is the greatest")
    else:
        print("c is greatest")
elif a<b:
    if b>c:
        print("b is graetest")
    else:
        print("c is greatest")
else :
    print ("all are equal")