n = int(input()) # 입력값 받기

result = 0
for i in range(1, n+1):
    nums = list(map(int, str(i)))
    result = sum(nums) + i
    if result == n:
        print(i)
        break
    if i == n:
        print(0)
