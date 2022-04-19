import switch as switch

from addition import Addition as a
from subtract import Subtraction as s
ch=input("Enter A for addition and S for subtraction")
if ch=='A':
    print(a.add(3,4))
elif ch=='S':
    print(s.subtract(5,1))
else:
  print("wrong input")