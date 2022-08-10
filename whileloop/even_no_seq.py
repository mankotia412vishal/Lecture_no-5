"""


The number of even elements of the sequence
"""
x = int(input())
count = 0

while x != 0:
  if x % 2 == 0:
    count += 1
  x = int(input())

print(count)


