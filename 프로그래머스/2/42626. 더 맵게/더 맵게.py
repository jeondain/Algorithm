import sys
import heapq
input = sys.stdin.readline

def solution(scoville, K):
    count = 0
    q = []
    for i in scoville:
        heapq.heappush(q, i)
    while q[0] < K:
        if(len(q) < 2):        
            return -1
        heapq.heappush(q, (heapq.heappop(q) + heapq.heappop(q)*2))
        count += 1
    return count