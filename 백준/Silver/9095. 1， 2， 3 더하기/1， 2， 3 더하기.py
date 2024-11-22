import sys
input = sys.stdin.readline

n = int(input())  

for _ in range(n):  
    x = int(input())  
    d = [0] * (x+1)  

    if x >= 1:
        d[1] = 1
    if x >= 2:
        d[2] = 2
    if x >= 3:
        d[3] = 4

    for i in range(4, x+1):
        d[i] = d[i-1] + d[i-2] + d[i-3]

    print(d[x])