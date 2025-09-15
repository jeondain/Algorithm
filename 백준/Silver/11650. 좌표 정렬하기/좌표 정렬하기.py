import sys
input = sys.stdin.readline

n = int(input())
points = []

for _ in range(n):
    a, b = map(int, input().split())
    points.append((a, b))

points.sort()

for a, b in points:
    print(a, b)