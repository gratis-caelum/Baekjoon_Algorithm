# 자연수 n에 대하여 n <= x <= 2n 범위에서 소수인 x를 구하는 Program
import sys
input = sys.stdin.readline

test_cases = [] # 입력을 담을 테스트 케이스 List

while True:
    n = int(input())
    if n == 0: # 입력 안에 0이 입력되면 종료
        break
    test_cases.append(n)
    
# 에라토스테네스의 체를 이용해 소수를 판별하는 함수 (n <= x <= 2n)
def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False # 0과 1은 소수가 아님
        
    # 2부터 한계의 제곱근까지의 수를 기준으로 배수 제거
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return sieve
    

# 주어진 테스트 케이스에 대해 소수를 출력하는 함수
def find_primes_in_range(test_cases):
    max_value = max(test_cases) * 2 # 2n 범위까지 소수를 구해야 하므로 가장 큰 n에 대해 2n까지 계산
    sieve = sieve_of_eratosthenes(max_value) # 2n까지의 소수 구하기
    
    for number in test_cases:
        count = 0
        # n <= x <= 2n 범위에서 소수 출력
        for i in range(number + 1, 2 * number + 1):
            if sieve[i]:
                count += 1
        print(count)
 

# 결과 출력
find_primes_in_range(test_cases)       