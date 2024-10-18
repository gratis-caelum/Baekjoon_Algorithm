N = int(input())

N_set = set() # set은 중복을 허용하지 않음

for i in range(N + 1):
    n = int(input())
    N_set.add(n)
    
# set을 정렬시키기 위해 리스트로 변환 후 정렬
set_to_list = sorted(N_set, reverse=True)

for i in range(len(set_to_list)):
    print(set_to_list[i])
