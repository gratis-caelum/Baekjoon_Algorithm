N = int(input())

cnt = 0 # 몇 번째 종말의 수인지 count
num = 666

while True:
    if "666" in str(num): # 666 (종말의 수)가 num에 포함되어있는 경우
        cnt += 1
    
    if cnt == N: # 구하려고 하는 N번째 종말의 수와 같다면 num 반환
        print(num)
        break
    
    num += 1