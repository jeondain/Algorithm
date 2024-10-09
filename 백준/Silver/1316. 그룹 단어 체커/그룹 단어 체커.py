import sys
input = sys.stdin.readline

n = int(input())
cnt = n
for _ in range(n):
    x = input()
    for i in range(len(x)-1):
        if x[i] == x[i+1]:
            continue
        elif x[i] in x[i+1:]:
            cnt -= 1
            break
print(cnt) 