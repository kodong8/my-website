import random
from tkinter import messagebox


# 로또 번호 생성
def generate_lotto_numbers():
    return sorted(random.sample(range(1, 46), 6))

# 당첨 결과 계산
def check_winning(lottos, winning_numbers, bonus_number):
    results = []
    prize_money = [0, 0, 5000, 50000, 1500000, 45000000, 2000000000]  # 등수별 당첨금
    for lotto in lottos:
        match_count = len(set(lotto) & set(winning_numbers))
        is_bonus = bonus_number in lotto

        if match_count == 6:
            results.append((1, prize_money[6], lotto))
        elif match_count == 5 and is_bonus:
            results.append((2, prize_money[5], lotto))
        elif match_count == 5:
            results.append((3, prize_money[4], lotto))
        elif match_count == 4:
            results.append((4, prize_money[3], lotto))
        elif match_count == 3:
            results.append((5, prize_money[2], lotto))
        else:
            results.append((0, 0, lotto))
    return sorted(results, key=lambda x: (x[0] if x[0] > 0 else float('inf')))

# 초기화 함수
def reset_totals():
    global total_cost_accumulated, total_prize_accumulated
    total_cost_accumulated = 0
    total_prize_accumulated = 0
    messagebox.showinfo("초기화 완료", "누적 금액과 결과가 초기화되었습니다.")