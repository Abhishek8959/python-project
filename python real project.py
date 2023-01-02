import random
a=int(input("a:"))
b=int(input("b:"))
i=int(random.uniform(a,b))
if i>0:
    print("{} is a positive number".format(i))
    if i%2==0:
        print("{} is an even number".format(i))
    elif i%2 !=0:
        print("{} is a odd number".format(i))
    factor=0
    for j in range(1,i+1):
        if i%j==0:
            factor+=1
    if factor>2:
        print ("{} is a composite number".format(i))
    else:
        print("{} is a prime number".format(i))
elif i<0:
    print("{} is a negative number".format(i))
    if i%2==0:
        print("{} is an even number".format(i))
    elif i%2 !=0:
        print("{} is a odd number".format(i))
