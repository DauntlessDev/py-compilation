# Python factorial program

factorial = 1
num = 9

if number < 0:
   print("Negative numbers does not exist in factorial")
elif number == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,number + 1):
       factorial = factorial*i
   print("The factorial of",number,"is",factorial)
