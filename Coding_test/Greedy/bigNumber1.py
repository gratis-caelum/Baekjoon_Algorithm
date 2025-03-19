# N, M, K를 공백으로 구분하여 입력한다.
N, M, K = map(int, input().split())

# N개의 배열을 공백으로 구분하여 입력
data = list(map(int, input().split()))
data.sort() # 작은 수부터 정렬

first = data[N - 1] # 가장 큰 수
second = data[N - 2] # 두 번째로 큰 수

result = 0

while True:
    for i in range(K): # K번 더함
        if M == 0: # M이 0인 경우 멈춤
            break
        result += first
        M -= 1
    
    if M == 0: # M이 0인 경우 멈춤
        break
    result += second 
    M -= 1
    
print(result)