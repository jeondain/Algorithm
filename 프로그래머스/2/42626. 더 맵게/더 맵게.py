import sys
import heapq
input = sys.stdin.readline

def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if(len(scoville) < 2):        
            return -1
        heapq.heappush(scoville, (heapq.heappop(scoville) + heapq.heappop(scoville)*2))
        count += 1
    return count