N, k = map(int, input().split())

N_list = list(map(int, input().split()))

new_list = sorted(N_list, reverse=True)

print(new_list[k - 1])  