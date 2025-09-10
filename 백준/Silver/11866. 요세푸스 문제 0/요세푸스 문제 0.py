import sys
input = sys.stdin.readline 

n, k = map(int, input().split())

idx = 0
queue = [i for i in range(1, n+1)]
res = []
while queue:
    idx += k - 1  # k-1번째 인덱스까지 건너뛰기
    if idx >= len(queue):  # 인덱스가 범위를 넘어갈 경우
        idx %= len(queue)  
    res.append(str(queue.pop(idx)))  

print("<", ", ".join(res), ">", sep="")