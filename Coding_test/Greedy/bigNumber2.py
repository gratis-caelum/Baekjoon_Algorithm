# N, M, K 를 공백으로 구분하여 입력
N, M, K = map(int, input().split())

# N개의 배열을 공백으로 구분하여 입력
data = list(map(int, input().split()))
data.sort()

first = data[N - 1] # 가장 큰 수
second = data[N - 2] # 두 번째로 큰 수

count = int(M / (K + 1)) * K 
count += M % (K + 1)

result = (count) * first
result += (M - count) * second

print(result)