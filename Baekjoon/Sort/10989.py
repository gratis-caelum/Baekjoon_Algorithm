import sys
input = sys.stdin.readline 

N = int(input())

arr = [0] * (10000 + 1) # 자연수 10,000까지 주어지니 10,001 까지 배열 선언

for i in range(N):
    arr[int(input())] += 1 # 각 입력값에 해당하는 index value 증가

# arr에 기록된 정보 check
for i in range(len(arr)):
    if arr[i] != 0: # 입력받은 데이터들을 출력
        for j in range(arr[i]):
            print(i)