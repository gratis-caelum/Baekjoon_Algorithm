import sys
input = sys.stdin.readline # 반복문으로 여러 줄 입력받는 상황에서는 input() 사용하면 시간 초과

N = int(input())
N_list = []

for i in range(N):
    N_list.append(int(input()))
    
print(*sorted(N_list), sep='\n')
