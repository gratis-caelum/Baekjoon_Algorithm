import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # n : A의 원소의 개수, m : B의 원소의 개수

n_set = set(map(int, input().split())) # A 집합
m_set = set(map(int, input().split())) # B 집합

answer = (n_set - m_set) | (m_set - n_set)
print(len(answer))