import os

a = int(os.environ.get("NUMBER", 0)) 
print("Number entered:", a)
print("select operator= +,-,*,/")
oper=input("pic one operator  :")
b=int(input("enter number: "))
if oper=='+':
      print(a+b)
elif oper=='-':
      print(a-b)
elif oper=='*':
      print(a*b)
elif oper=='/':
      print(a/b)
else:
    print("invalid operator")

