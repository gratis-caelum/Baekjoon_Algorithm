# n번째 사람은 n의 배수 번째 창문을 열려 있으면 닫고 닫혀 있으면 연다. 
# N번째 사람까지 진행한 후 열려 있는 창문의 개수를 구하는 Program (단, 처음에 모든 창문은 닫혀있음)
import sys
input = sys.stdin.readline

n = int(input()) # 창문의 개수와 사람의 수

# 창문을 열려 있는지 여부를 나타내는 List (처음엔 모두 닫혀있음)
windows = [False] * (n + 1) # 1번부터 n번까지의 창문

# 각 사람의 순서대로 창문을 열거나 닫는 작업
for person in range(1, n+1):
    for window in range(person, n + 1, person):
        windows[window] = not windows[window] # 창문을 열거나 닫음
    
# 열려 있는 창문의 개수 카운트
open_windows_count = sum(windows)

print(open_windows_count)
    
# 메모리 초과