import sys
input = sys.stdin.readline

n = int(input())
words = []

for _ in range(n):
    words.append(input().strip())

words = list(set(words)) 

words.sort() # 사전 순으로
words.sort(key = len) # 길이가 짧은 것부터

for word in words:
    print(word)