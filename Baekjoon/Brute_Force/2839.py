n = int(input())

count = 0 # 봉지 개수를 세는 변수

while n >= 0: # n이 0 이상일때만 반복
    if n % 5 == 0: # 5의 배수일 때
        count += int(n // 5) # 5kg 봉지 추가
        print(count)
        n -= 5
    
    count += 1 # 3kg 봉지 추가 (5의 배수가 될 때까지)
    n -= 3
    
    
else:
    print(-1)
    