import sys
input = sys.stdin.readline

n = int(input()) # 단어의 개수

arr = []

for i in range(n):
    arr.append(input().strip())
        
arr = list(set(arr)) # 중복 제거

arr.sort(key = lambda x : (len(x), x))

for i in arr:
    print(i, sep='\n')
    
