#input
print("enter sides")
a=int(input())
b=int(input())
c=int(input())
#arithemaics
if a+b>c:
    print(" tringle possible 1")
elif b+c>a:
    print("triangle posible 2")
elif c+a>b:
    print("trangle is possible 3")
else:
    print("triangle not possible")
