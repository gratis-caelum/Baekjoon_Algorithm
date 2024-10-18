# 연립 방정식 풀이, 행렬, 브루트포스 방법이 보이나 브루트포스 방법으로 시작
a, b, c, d, e, f = map(int, input().split())

for i in range(-999, 1000):
    for j in range(-999, 1000):
        if (a * i) + (b * j) == c and (d * i) + (e * j) == f:
            print(i, j)
            