# A sequence consists of integer numbers and ends with the number 0. Determine how many elements of this sequence are equal to its largest element.
max = 0
с = 1
a = int(input())
while a != 0:
    if a > max:
        max = a
        с = 1
    elif a == max:
        с += 1
    a = int(input())
print(с)
