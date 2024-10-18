import sys
from collections import Counter

input = sys.stdin.readline

N = int(input()) # 상근이가 가지고 있는 숫자 카드의 개수

# 상근이가 가지고 있는 숫자 카드에 적힌 숫자 counting
cards = list(map(int, input().split())) 
card_count = Counter(cards) # 숫자 카드의 개수를 세는 Counter


M = int(input()) # 정수 M의 개수

# M개의 정수 입력
queries = list(map(int, input().split()))

# 각 정수에 대해 상근이가 몇 개 가지고 있는지 출력
result = []
for query in queries:
    result.append(str(card_count[query]))

# 공백으로 구분하여 결과 출력
print(" ".join(result))

