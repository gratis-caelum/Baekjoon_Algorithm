# 골드바흐 파티션의 개수 구하기
import sys
input = sys.stdin.readline

T = int(input()) # 테스트 케이스의 개수

test_cases = [] # 골드바흐 파티션의 수를 넣어놓을 List

for i in range(T):
    test_cases.append(int(input()))
    
# 에라토스테네스의 체를 이용하여 소수를 구하는 함수
def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    
    sieve[0] = sieve[1] = False # 0과 1은 소수가 아님
    
    # 2부터 주어진 숫자의 제곱근까지 배수를 제거하는 것을 반복
    for i in range(2, int(limit ** 0.5) + 1):    
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False

    return sieve
    
# 골드바흐 파티션의 개수를 구하는 함수
def count_goldbach_partititons(n, primes):
    count = 0
    for i in range(2, (n // 2) + 1): # 두 소수의 쌍을 구하는데 중복을 피하기 위해 절반만 확인
        if primes[i] and primes[n - i]:
            count += 1
    return count

# 가장 큰 테스트 케이스를 기준으로 소수 리스트 생성
max_value = max(test_cases)
primes = sieve_of_eratosthenes(max_value)

# 각 테스트 케이스에 대해 결과 출력
for n in test_cases:
    result = count_goldbach_partititons(n, primes)
    print(result)
    
    