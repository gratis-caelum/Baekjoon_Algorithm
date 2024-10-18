import sys
input = sys.stdin.readline

N, M = map(int, input().split())

S = set()
for i in range(N):
    S.add(input().strip()) # 공백을 제거 후 집합에 추가

count = 0 

for _ in range(M):
    if input().strip() in S:
        count += 1
        
print(count)
