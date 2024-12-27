import sys
input = sys.stdin.readline

n, m = map(int, input().split())
words = dict()

for _ in range(n):
    w = input().strip()
    if len(w) >= m: 
        if w in words:
            words[w] += 1
        else:
            words[w] = 1

# -x[1] 자주 나오는 단어 앞에 배치
# -len(x[0]) = 단어 길이 길수록 앞에 배치
# x[0] = 사전 순 정렬
words = sorted(words.items(), key = lambda x: (-x[1], -len(x[0]), x[0]))

for i in words:
    print(i[0])