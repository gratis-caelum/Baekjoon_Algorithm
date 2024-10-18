import sys
input = sys.stdin.readline

# 유클리드 호제법을 이용한 최대공약수 구하기
def gcd(m, n):
    while n != 0:
        t = m % n
        m, n = n, t
    return abs(m)

# 입력 처리
a, b = map(int, input().split())  # b / a 형태의 첫 번째 분수
c, d = map(int, input().split())  # d / c 형태의 두 번째 분수

# 분수 덧셈 처리: 분모의 최소공배수와 분자의 합 계산
high = (d * a) + (b * c)  # 분자 계산
low = b * d  # 분모 계산

# 분자와 분모의 최대공약수 구하기
g = gcd(high, low)

# 기약분수로 변환
reduced_numerator = high // g
reduced_denominator = low // g

# 결과 출력
print(f"{reduced_numerator} {reduced_denominator}")