# Python Fibonacci sequence program (Recursion)

def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))

nterms = 15

if nterms <= 0:
   print("Plese only enter positive numbers.")
else:
   print("Fibonacci Sequence:")
   for i in range(nterms):
       print(fibonacci(i))
