# 정수를 저장하는 스택을 만들고 명령에 따라 출력을 처리하는 Program
# 1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
# 2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
# 3: 스택에 들어있는 정수의 개수를 출력한다.
# 4: 스택이 비어있으면 1, 아니면 0을 출력한다.
# 5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.
import sys
input = sys.stdin.readline

n = int(input()) # 명령의 수
stack = [] # 정수를 저장하는 Stack을 List로 구현

for i in range(n):
    command = input().strip().split() # 명령어를 입력받는다.
    
    if command[0] == "1":  # 명령어 "1"은 정수 X를 스택에 넣는다.
        x = int(command[1])
        stack.append(x)
    
    elif command[0] == "2": # 명령어 "2"은 스택에 정수가 있다면 맨 위에 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
        if stack:
            print(stack.pop()) # 스택이 비어있지 않으면 맨 위의 정수 출력 후 제거
        else:
            print(-1) # 스택이 비어있다면 -1 출력
            
    elif command[0] == "3": # 명령어 "3"은 스택에 쌓여있는 정수의 개수 출력
        print(len(stack))
        
    elif command[0] == "4": # 명령어 "4"는 스택이 비어있으면 1, 아니면 0을 출력
        if stack:
            print(0)
        else:
            print(1)
    elif command[0] == "5": # 명령어 "5"는 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.
        if stack:
            print(stack[-1])
        else:
            print(-1)

