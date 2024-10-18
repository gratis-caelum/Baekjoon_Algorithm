import sys
input = sys.stdin.readline

S = input().strip() # 문자열 입력

count = set()

for i in range(len(S)):
    for j in range(i + 1, len(S) + 1):
        count.add(S[i:j]) 

print(len(count))       