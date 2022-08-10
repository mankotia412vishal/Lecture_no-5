# The sequence consists of distinct positive integer numbers and ends with the number 0. Determine the value of the second largest element in this sequence. It is guaranteed that the sequence has at least two elements.
max_2 = -1
a = int(input())
max = 0
while a != 0:
    if a > max:
        max_2 = max
        max = a
    elif a > max_2:
        max_2 = a
    a = int(input())
print(max_2)
