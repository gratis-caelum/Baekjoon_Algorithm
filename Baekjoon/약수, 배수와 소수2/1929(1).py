# M이상 N이하의 소수를 모두 출력하는 Program
import sys
input = sys.stdin.readline

M, N = map(int, input().split()) # 자연수 M, N 입력

# 소수를 판별하는 함수
def isPrime(number):
    # 숫자가 2보다 작으면 소수가 아님
    if number < 2:
        return False
    # 2부터 제곱근까지 반복
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


# M이상 N이하 소수 출력하는 함수
def print_prime(M, N):
    for i in range(M, N + 1):
        if isPrime(i):
            print(i)
        

print_prime(M, N)