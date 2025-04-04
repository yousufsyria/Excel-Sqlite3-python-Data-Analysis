import random
s=random.randint(1,5)
a=int(input("Enter the number: "))
if a==s:
    print("*** you win")
else:
    print("/// you lose ///")
    print(s)