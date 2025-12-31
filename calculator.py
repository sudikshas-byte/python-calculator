num1=float(input("enter first number:"))
num2=float(input("enter second number:"))
print("choose operation")
print("'+',add")
print("'-',sub")
print("'*',product")
print("'/',divide")
operation=input("enter operation:")
if operation=="+":
   print("the sum is:",num1+num2)
elif operation=="-":
   print("the difference is:",num1-num2)
elif operation=="*":
   print("the product is:",num1*num2)
elif operation=="/":
 if num2!=0:
   print("valid",num1/num2)
 else:
   print("invalid not divisible by 0!!")
else:
   print("INVALID OPERATION!!!")
