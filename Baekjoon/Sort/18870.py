import sys
input = sys.stdin.readline

n = int(input())  # 좌표의 개수

numbers = list(map(int, input().split()))

unique_numbers = sorted(set(numbers))  # 중복 제거 후 정렬

print(unique_numbers)

# 각 숫자의 압축된 좌표를 딕셔너리에 저장
numDict = {num: i for i, num in enumerate(unique_numbers)}

print(numDict)

# 입력된 numbers 리스트의 순서를 그대로 유지하며 압축 좌표 출력
for i in numbers:
    print(numDict[i], end=" ")