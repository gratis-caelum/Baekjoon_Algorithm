# N, K가 공백으로 구분되어 입력
N, K = map(int, input().split())

count = 0

while True:
    if (N == 1):
        break
    
    if (N % K == 0): # N이 K로 나누어질 경우
        N /= K
        count += 1
    else: # N이 K로 나누어떨어지지 않을 경우
        N -= 1
        count += 1

print(count) # 최종 출력
        