import sys
input = sys.stdin.readline

n = int(input()) # 출입 기록의 수

S = set() # log를 저장할 집합

for i in range(n):
    name, log = input().split()
    if log == "enter":
        S.add(name)
    elif log == "leave":
        S.discard(name)


for i in sorted(S, reverse=True):
    print(i)