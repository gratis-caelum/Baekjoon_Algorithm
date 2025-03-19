# N, M 을 공백으로 구분하여 입력
N, M = map(int, input().split())

result = 0
# 한 줄씩 입력받아서 확인
for i in range(N):
    data = list(map(int, input().split()))
    # 현재 줄에서 가장 작은 수를 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    # 가장 작은 수들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result) # 최종 답안 출력