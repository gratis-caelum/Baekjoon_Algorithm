# () : 기본 VPS 라고 하는데, 열린 괄호가 있다면 닫힌 괄호가 존재하는 것이 기본인 문자열.
# 기본인 문자열을 Yes, 아닌 문자열을 No 라고 판단하는 Program

import sys
input = sys.stdin.readline

T = int(input()) # 입력 데이터의 수 


for i in range(T):
    stack = [] # 괄호 기호를 넣을 Stack을 구현할 List
    is_vps = True # 올바른 VPS 인지 판단하는 변수
    
    parentheses = input().strip() # 괄호 문자열을 입력받음
    
    for char in parentheses: 
        if char in '(': # 열린 괄호는 스택에 추가함
            stack.append(char)
        elif char in ')': # 닫힌 괄호일 때
            if stack: # 스택에 문자가 존재하는 경우
                stack.pop() # 짝을 맞추고 제거
            else: # 문자가 존재하지 않는 경우
                is_vps = False #  잘못된 문자열
                break
    
    # 스택이 비어 있으면 VPS
    if is_vps and not stack:
        print("YES")
    else:
        print("NO")
 
       

