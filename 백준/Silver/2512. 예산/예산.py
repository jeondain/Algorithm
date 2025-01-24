import sys
input = sys.stdin.readline

N = int(input())
cities = list(map(int, input().split()))
budgets = int(input()) 
start, end = 0, max(cities) 

# 이분 탐색
while start <= end:
    mid = (start+end) // 2
    total = 0 
    for i in cities:
        if i > mid:
            total += mid
        else:
            total += i
    if total <= budgets: # 지출이 예산 보다 작으면
        start = mid + 1
    else: # 지출이 예산 보다 크면
        end = mid - 1
print(end)