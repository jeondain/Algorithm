import sys
input = sys.stdin.readline

n = int(input())

# 카드 등장 횟수 저장
hash = {}
for _ in range(n):
    card = int(input())
    if card not in hash:
        hash[card] = 1
    else:
        hash[card] += 1

max_count = max(hash.values())
result = min([key for key, value in hash.items() if value == max_count])   
print(result)   