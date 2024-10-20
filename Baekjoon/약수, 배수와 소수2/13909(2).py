# n번째 사람은 n의 배수 번째 창문을 열려 있으면 닫고 닫혀 있으면 연다. 
# N번째 사람까지 진행한 후 열려 있는 창문의 개수를 구하는 Program (단, 처음에 모든 창문은 닫혀있음)
import math

n = int(input())

# 1부터 n까지의 제곱수의 개수
open_windows_count = int(math.sqrt(n))

print(open_windows_count)