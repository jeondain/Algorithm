from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
baseball = list(permutations([1,2,3,4,5,6,7,8,9],3))

for _ in range(n):
    x, s, b = map(int, input().split())
    x = list(str(x)) #인덱스 접근을 위해
    remove_cnt = 0
    
    for i in range(len(baseball)):
        s_cnt = b_cnt = 0
        i -= remove_cnt #삭제된 조합만큼 건너뛰고 탐색
        
        for j in range(3):
            x[j] = int(x[j])
            if x[j] in baseball[i]:
                if j == baseball[i].index(x[j]): #위치와 값이 같은 경우
                    s_cnt += 1
                else: #값이 존재하는 경우
                    b_cnt += 1
                    
        if s_cnt != s or b_cnt != b: #입력 받은 스트라이크, 볼 개수와 다를 경우
            baseball.remove(baseball[i])
            remove_cnt += 1

print(len(baseball))  
