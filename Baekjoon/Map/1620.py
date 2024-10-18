import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())  # N: 도감에 수록된 포켓몬의 개수, M: 문제의 개수

by_id = {}  # 포켓몬 번호 -> 이름 dictionary
by_name = {}  # 포켓몬 이름 -> 번호 dictionary

# 포켓몬 도감에 포켓몬을 수록
for i in range(1, N + 1):
    pokemon = input().strip()  # 개행 문자 제거 후 입력
    by_id[i] = pokemon  # 번호에 따른 포켓몬 이름 저장
    by_name[pokemon] = i  # 포켓몬 이름에 따른 번호 저장

# 문제 처리
for i in range(M):
    x = input().strip()  # 개행 문자 제거 후 입력
    if x.isdigit():  # 입력이 숫자인 경우
        print(by_id[int(x)])  # 숫자로 변환한 후 포켓몬 이름 출력
    else:  # 입력이 이름인 경우
        print(by_name[x])  # 포켓몬 번호 출력