# 모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
# 모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
# 모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
# 모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
# 짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.
# 입력의 종료 조건으로 온점 하나가 들어오면 Program 종료
# 문자열이 균형을 이루고 있으면 yes, 아니면 no

import sys
input = sys.stdin.readline

while True:
    line = input().rstrip()
    
    # 종료 조건 : 온점(.)이 나오면 종료
    if line == '.':
        break
    
    stack = [] # 괄호를 처리할 Stack
    balanced = True # 균형 여부를 판단한 Flag
    
    for char in line:
        if char == '(' or char == '[': # 열린 괄호는 Stack에 추가
            stack.append(char)
        
        elif char == ')': # 닫힌 소괄호인 경우
            if stack and stack[-1] == '(': # 스택에 문자열이 존재하고, 그 문자열이 열린 소괄호인 경우
                stack.pop() # 짝이 맞으므로 스택에서 제거
            else:
                balanced = False # 균형이 맞지 않음
                break
        elif char == ']': # 닫힌 대괄호인 경우
            if stack and stack[-1] == ']': # 스택에 문자열이 존재하고, 그 문자열이 닫힌 대괄호인 경우
                stack.pop() # 짝이 맞으므로 스택에서 제거
            else:
                balanced = False # 균형이 맞지 않음
                break
    
    if balanced and not stack: # 스택이 비어있고 균형이 맞다면
        print("yes")
    else:
        print("no")
    
