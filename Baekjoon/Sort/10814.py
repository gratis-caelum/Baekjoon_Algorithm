import sys
input = sys.stdin.readline

n = int(input()) # 온라인 저지 회원의 수

arr = []

for i in range(n):
    [age, name] = input().split()
    arr.append([int(age), name, i]) # 나이, 이름 배열
    
arr.sort(key = lambda x : (x[0], x[2])) # 나이가 증가하는 순인데, 같으면 먼저 가입한 순서

for i in arr:
    print(i[0], i[1])


