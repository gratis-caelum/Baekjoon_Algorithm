import sys
input = sys.stdin.readline

def gcd(m, n):
    while n != 0:
        t = m % n
        (m, n) = (n, t)
        return abs(m)

n = int(input()) # 이미 심어져 있는 가로수의 수
tree_arr = [] # 가로수의 위치를 저장하는 List

for i in range(n):
    tree_arr.append(int(input()))

# 각 가로수의 간격을 저장하는 List
gaps = []

# 각 가로수 간의 간격
for i in range(1, n):
    gaps.append(tree_arr[i] - tree_arr[i - 1])

# 간격들의 최대공약수
gcd_value = gaps[0]
for i in range(1, len(gaps)):
    gcd_value = gcd(gaps[i], gcd_value)

# 필요한 나무의 수 계산
total_trees_needed = 0
for gap in gaps:
    total_trees_needed += (gap // gcd_value) - 1

# 결과 출력
print(total_trees_needed)
    