# 모든 수를 받아적은 후 그 수의 합을 알아내는 Program
# 잘못된 수를 받아적을 때마다 0을 외쳐 가장 최근에 쓴 수를 지우게 함.

import sys
input = sys.stdin.readline

K = int(input()) # 정수 K개가 입력됨

stack = [] # Stack을 List로 구현

for i in range(K):
    num = int(input())
    
    if num == 0: # 만일 0을 입력받으면
        if stack:
            stack.pop() # 가장 최근에 쓴 수를 지운다.
    else:
        stack.append(num)
    
   

total_sum = sum(stack)

print(total_sum)