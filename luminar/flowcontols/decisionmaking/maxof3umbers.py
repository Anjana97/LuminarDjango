num1=int(input("enter a number 1\n"))
num2=int(input("enter a number 2\n"))
num3=int(input("enter a number 3\n"))

if((num1>num2)&(num1>num3)):
    print("num1 is greater",num1)
elif((num2>num1)&(num2>num3)):
    print("num2 is greater",num2)
elif((num3>num2)&(num1<num3)):
    print("num3 is greater",num3)
else:
     print("numbers are equal",num1)
