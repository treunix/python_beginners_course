# практика по изученному материалу.
# Симуляция игры азартного игрока по стратегии Мартингейла.
# Стратегия Мартингейл - в казике ставишь мин ставку, если победил, то забрал и снова ставишь мин ставочку, а если проебал, то x2 став  ишь

import random

HEADS = "Орёл"
TAILS = "Решка"
COIN_VALUES = [HEADS, TAILS]


def flip_coin():
    return random.choice(COIN_VALUES) # choice возращает случайный элемент из списка.


def play_martingale(*, starting_funds: int, min_bet: int, max_bet: int) -> int:
    steps_to_loose = 0
    current_funds = starting_funds
    current_bet = min_bet

    while current_funds > 0:
        print("=" * 20)
        steps_to_loose += 1
        current_funds -= current_bet
        print(f"Средства после ставки: {current_funds}, Ставка: {current_bet}")
        flipped_coin_value = flip_coin()
        print(f"Выпало: {flipped_coin_value}")
        if flipped_coin_value == HEADS:
            win = current_bet * 2
            print(f'Победа: +{win}')
            print("Всего средств:", current_funds + current_bet + win)
            current_funds += win
            current_bet = min_bet
        else:
            current_bet *= 2
            print(f"Поражение: -{current_bet}")
            print("Всего средств:", (current_funds + current_bet) - current_bet)
            if current_bet > max_bet:
                current_bet = min_bet
            if current_bet > current_funds:
                current_bet = current_funds
    return steps_to_loose

print(play_martingale(starting_funds=1000, min_bet=10, max_bet=100))



def simulate_martingale_for_n_players(*, starting_funds: int, min_bet: int, max_bet: int, n_games: int) -> float:
    total_steps_to_loose = 0
    for i in range(n_games):
        step_to_loose = play_martingale(starting_funds=starting_funds, min_bet=min_bet, max_bet=max_bet)
        total_steps_to_loose += step_to_loose

    return total_steps_to_loose / n_games


# print(
#     simulate_martingale_for_n_players(
#         n_games=10,
#         starting_funds=1000,
#         min_bet=1,
#         max_bet=100,
#     )
# )