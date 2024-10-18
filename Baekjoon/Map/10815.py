import sys
input = sys.stdin.readline

N = int(input())
N_set = set(map(int, input().split()))
            
M = int(input())
M_list = list(map(int, input().split()))

for i in M_list:
    if i in N_set:
        print("1", end= " ")
    else:
        print("0", end= " ")
