# M 이상 N 이하의 소수를 찾는 Program(에라토스테네스의 체 방법 사용)
import sys
input = sys.stdin.readline

M, N = map(int, input().split()) # M, N 자연수 입력

# 에라토스테네스의 체를 이용하여 M 이상 N 이하의 소수를 구하는 함수
def sieve_of_eratosthenes(M, N):
    # N까지의 범위에서 소수를 찾기 위한 List
    sieve = [True] * (N + 1)
    sieve[0] = sieve[1] = False # 0과 1은 소수가 아님
    
    # 2부터 N의 제곱근까지의 수를 기준으로 배수 제거
    for i in range(2, int(N ** 0.5) + 1):
        if sieve[i]: # i가 소수라면
            for j in range(i * i, N + 1, i): # i의 배수들은 소수가 아니다.
                sieve[j] = False
    
    
    # M 이상 N 이하의 소수를 출력
    for i in range(M, N + 1):
        if sieve[i]:
            print(i)

# 결과 출력
sieve_of_eratosthenes(M, N)