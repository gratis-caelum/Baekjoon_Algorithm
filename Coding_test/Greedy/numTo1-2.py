# N, K를 공백으로 구분하여 입력
N, K = map(int, input().split())

result = 0

while N >= K:
    # N이 K로 나누어 떨어지지 않으면 K의 배수가 되도록 1을 뺀다
    if N % K != 0:
        result += N % K
        N -= N % K # K의 배수로 만듦
        
    # K로 나누기
    result += 1
    N //= K
    
# 마지막으로 남은 수에 대해 1씩 제외
result += (N - 1)
print(result)