# A sequence consists of integer numbers and ends with the number 0. Determine how many elements of this sequence are greater than their neighbours above.

c = 0
b = int(input())
a = b
while b != 0:
    if b > a:
       c += 1
    a = b
    b = int(input())
print(c)
