from itertools import combinations

card_num, target_num = map(int, input().split())
card_list = list(map(int, input().split()))

# 카드의 개수가 잘못되었을 경우 확인
if len(card_list) != card_num:
    print("error : 카드 개수와 입력된 리스트의 개수 불일치")
else:
    biggest_num = 0
    for cards in combinations(card_list, 3):
        temp_num = sum(cards)
        if biggest_num < temp_num <= target_num:
            biggest_num = temp_num
    print(biggest_num)