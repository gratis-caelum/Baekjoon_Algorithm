n = int(input()) # 총 점의 개수
arr = []

for i in range(n):
    [a, b] = map(int, input().split())
    arr.append([a, b])

arr.sort()
for i in arr:
    print(i[0], i[1])