import sys
input = sys.stdin.readline

n = int(input())
points = []

for i in range(n):
    age, name = input().split()
    age = int(age)
    points.append((age, name))

# 나이 순 정렬
points.sort(key=lambda x: x[0])

for age, name in points:
    print(age, name)