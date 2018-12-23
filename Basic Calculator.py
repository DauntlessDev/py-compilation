def compute_sum(x, y):
   return x + y

def compute_difference(x, y):
   return x - y

def compute_product(x, y):
   return x * y

def compute_quotient(x, y):
   return x / y

print("Select what to find : ")
print("1.Find Sum")
print("2.Find Difference")
print("3.Find Product")
print("4.Find Quotient")

# Take input from the user 
choice = input("Enter choice(1/2/3/4):")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if choice == '1':
   print(num1,"+",num2,"=", compute_sum(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", compute_difference(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", compute_product(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", compute_quotient(num1,num2))
else:
   print("Invalid input")
