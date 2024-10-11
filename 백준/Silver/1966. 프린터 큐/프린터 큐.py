import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    n, m = map(int, input().split())
    q = list(map(int, input().split()))
    idx_q = list(range(n))
    cnt = 0

    while q:
        if q[0] == max(q):
            cnt += 1 
            if idx_q[0] == m:  
                print(cnt)  
                break
            q.pop(0)  
            idx_q.pop(0)  
        else:
            q.append(q.pop(0))  
            idx_q.append(idx_q.pop(0)) 