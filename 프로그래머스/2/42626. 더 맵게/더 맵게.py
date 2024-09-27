import sys
import heapq
input = sys.stdin.readline

def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        try:
            heapq.heappush(scoville, (heapq.heappop(scoville) + heapq.heappop(scoville)*2))
            count += 1
        except:
            return -1
    return count