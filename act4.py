#act4-peri
def sq(x):
  peri=4*x
  return peri

def rect(l,b):
  peri = 2*(l+b)
  return peri


x=int(input("Enter square side:"))
print(sq(x))

l = int(input("Enter rectangle length:"))
b = int(input("Enter rectangle breadth:"))
print(rect(l,b))