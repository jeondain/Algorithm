import sys
input = sys.stdin.readline

n = int(input())
card = []
for _ in range(n):
    card.append(int(input()))

# 카드 등장 횟수 저장
hash = {}
for num in card:
    if num not in hash:
        hash[num] = 1
    else:
        hash[num] += 1

max_count = max(hash.values())
result = min([key for key, value in hash.items() if value == max_count])   
print(result)        