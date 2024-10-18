import sys
input = sys.stdin.readline

# 유클리드 호제법을 이용한 최대공약수(GCD) 함수
def gcd(m, n):
    while n != 0:
        t = m % n
        m, n = n, t
    return abs(m)

# 최소공배수(LCM) 함수
def lcd(m, n):
    return m * n // gcd(m, n)

n, m = map(int, input().split())  # 정수 A, B 입력

# 결과 출력
result = lcd(n, m)
print(result)