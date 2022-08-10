x = int(input("Enter the number: "))
n = 0

while 2**n <= x:
  n += 1

print(n-1)
print(2**(n-1))
