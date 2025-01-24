#n conversion- Decimal To Binary

def convert(n):
    if n >= 1:
        convert(n // 2)
    print(n % 2, end='')


print("Binary value:", end=' ')
convert(3)
print() 
