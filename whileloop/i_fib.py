# The Fibonacci sequence is defined as follows:
# ϕ0=0, ϕ1=1, ϕn=ϕn−1+ϕn−2.
# Given an integer a, determine its index among the Fibonacci numbers, that is, print the number n such that ϕn=a. If a is not a Fibonacci number, print -1

A = int(input())
fi1 = 0
fi2 = 1
if A == 1:
    print(1)
else:
    i = 1
    while A > fi2:
        fi2, fi1 = fi1 + fi2, fi2
        i += 1
    if A == fi2:
        print(i)
    else:
        print(-1)
