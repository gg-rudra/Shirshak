a=int(input('enter first value:'))
b=int(input("enter second value:"))
c=int(input("enter third value:"))
if a>b:
    print("a is the larger number:")
    if a>c:
        print("a is largest:")
    else:
        print("c is largest:")
else:
    if b>c:
        print("b is the larger number:")
    else:
        print("c is largest")
