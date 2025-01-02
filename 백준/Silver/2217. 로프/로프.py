import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))
arr.sort()

result = []
for x in arr:
    result.append(x*n)
    n -= 1

print(max(result))