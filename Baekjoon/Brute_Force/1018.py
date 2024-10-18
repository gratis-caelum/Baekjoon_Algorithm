N, M = map(int, input().split()) # N x M 정사각형 생성

board = [] # 보드판을 저장하는 리스트
result = [] # 결과값을 저장하는 리스트

for _ in range(N):
    board.append(input())

for i in range(N - 7): # 보드판을 넘어서지 않기 위해 시작점을 N-8까지 제한 (8x8 체스판 생성)
    for j in range(M - 7):
        b_index = 0 # black으로 칠할 변수
        w_index = 0 # white로 칠할 변수

        for a in range(i, i + 8): # i부터 i + 7까지 
            for b in range(j, j + 8): # j부터 j + 7까지
                if (a + b) % 2 == 0: # 행과 열의 index 합이 짝수인 경우
                    if board[a][b] != 'B': # 그 인덱스가 검은색이 아닌 경우
                       b_index +=1 # 검은색으로 색칠
                    if board[a][b] != 'W': # 인덱스가 하얀색이 아닌 경우 
                        w_index +=1 # 하얀색으로 색칠
                        
                else : # 행과 열의 index 합이 홀수인 경우
                    if board[a][b] != 'B': # 인덱스가 검은색이 아닌 경우
                        w_index += 1 # 하얀색으로 색칠
                    
                    if board[a][b] != 'W': # 인덱스가 하얀색이 아닌 경우
                        b_index += 1 # 검은색으로 색칠
                    
        result.append(b_index)
        result.append(w_index)

print(min(result))
                        
                       