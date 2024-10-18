import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M

# 듣도 못한 사람 명단
not_heard = set()
for i in range(N):
    not_heard.add(input().strip()) # 개행문자 제거

# 보도 못한 사람 명단
not_seen = set()
for i in range(M):
    not_seen.add(input().strip()) # 개행문자 제거
    
# 듣도 보도 못한 사람 
not_heard_and_seen = sorted(not_heard & not_seen) # 사전순으로 정렬

# 듣보잡의 수 출력
print(len(not_heard_and_seen))

# 듣보잡 명단 출력
for name in not_heard_and_seen:
    print(name)