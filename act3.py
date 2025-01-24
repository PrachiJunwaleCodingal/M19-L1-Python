#calculator

def add(a, b):
   return a+b

def sub(a,b):
  return a-b

def mult(a,b):
  return a*b

def div(a,b):
  return a/b

print("a. Add , b. Subtract, c. Multiply, d. Divide")
ch = input("Please enter ch:")

n1 = int(input("Enter Num1: "))
n2 = int(input("Enter Num2: "))

if ch == 'a':
  print("Sum:", add(n1, n2))
elif ch == 'b':
  print("Sub:", sub(n1, n2))
elif ch == 'c':
  print("product:", mult(n1, n2))
elif ch == 'd':
  print("Division:", div(n1, n2))
else:
  print("INVALID")
