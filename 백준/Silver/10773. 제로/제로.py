import sys
input = sys.stdin.readline

k = int(input().strip())
arr = []

for _ in range(k):
    n = int(input().strip())
    if n == 0:
        arr.pop()
    else:
        arr.append(n)

print(sum(arr))