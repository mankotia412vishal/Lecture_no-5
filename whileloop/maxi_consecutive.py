# Given a sequence of integer numbers ending with the number 0. Determine the length of the widest fragment where all the elements are equal to each other.

chunk = 1
max_chunk = 1
a = int(input())
b = a
while b != 0:
    b, a = int(input()), b
    if b == a:
        chunk += 1
    else:
        if chunk > max_chunk:
            max_chunk = chunk
        chunk = 1
print(max_chunk)
