# The Fibonacci sequence is defined as follows:
# ϕ0 = 0, ϕ1 = 1, ϕn = ϕn−1+ϕn−2.
# Given a non-negative integer n, print the nth Fibonacci number ϕn.
# This problem can also be solved with a for loop
n = int(input())
fi1 = 0
fi2 = 1
if n < 1:
    print(0)
elif n == 1:
    print(1)
else:
    i = 2
    while i <= n:
        fi2, fi1 = fi1 + fi2, fi2
        i += 1
    print(fi2)
