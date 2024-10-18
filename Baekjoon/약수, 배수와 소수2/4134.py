# n보다 크거나 같은 소수 중 가장 작은 소수를 찾는 Program
import sys
input = sys.stdin.readline

n = int(input()) # 테스트 케이스의 개수

test_cases = [] # 테스트 케이스들을 모아놓는 List

# 테스트 케이스 개수만큼 List 추가
for i in range(n):
    test_cases.append(int(input()))

print(test_cases)

# 소수 판별 함수
def isPrime(number):
    # 숫자가 2보다 작으면 소수가 아님
    if number < 2:
        return False
    # 2부터 숫자의 제곱근까지 반복해서 소수인지 확인해보기
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# 숫자보다 크거나 같은 가장 작은 소수를 찾는 함수
def find_next_prime(number):
    while True:
        if isPrime(number):
            return number
        # 소수가 아니라면 그 다음 수로 증가시킴
        number += 1

# 테스트 케이스마다 결과를 출력하는 함수
def prime_list(test_cases):
    for number in test_cases:
        next_prime = find_next_prime(number)
        print(next_prime)

# 결과 출력
prime_list(test_cases)