import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()

cnt = 0
i = 0
while i <= len(a) - len(b):
    if a[i:i+len(b)] == b:
        cnt += 1
        i += len(b)  # 찾은 단어의 길이만큼 건너뛰기
    else:
        i += 1

print(cnt)