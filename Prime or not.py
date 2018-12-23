# Python program to check if the input number is prime or not

number = 123

if number > 1:
   # check for factors
   for i in range(2,number):
       if (number % i) == 0:
           print(number,"is not a prime number")
           print(i,"times",number//i,"is",number)
           break
   else:
       print(number,"is a prime number")
       

else:
   print(number,"is not a prime number")
