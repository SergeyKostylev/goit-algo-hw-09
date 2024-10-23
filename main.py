

def find_coins_greedy(coins: list[int], missing_sum):
    coins = sorted(coins)
    current_sum = 0
    result = {}
    current_coin = coins.pop()

    while current_sum != missing_sum:
        if current_coin <= missing_sum - current_sum:
            result[current_coin] = result[current_coin] + 1 if current_coin in result else 1
            current_sum = current_sum + current_coin
        else:
            if len(coins) == 0:
                print("It is not possible to get the amount from the coins provided.")
                return None

            current_coin = coins.pop()

    return result

def find_min_coins(coins: list[int], missing_sum):
    dp = [float('inf')] * (missing_sum + 1)
    dp[0] = 0

    for i in range(1, missing_sum + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[missing_sum] == float('inf'):
        print("It is not possible to get the amount from the coins provided.")
        return None

    result = {}
    remaining_amount = missing_sum
    while remaining_amount > 0:
        for coin in coins:
            if remaining_amount >= coin and dp[remaining_amount] == dp[remaining_amount - coin] + 1:
                result[coin] = result[coin] + 1 if coin in result else 1
                remaining_amount -= coin
                break

    return result

coin_set = [50, 25, 10, 5, 2, 1]
sum = 113

# missing result: {50: 2, 10: 1, 2: 1, 1: 1}
print(f" find_coins_greedy() : {find_coins_greedy(coin_set, sum)}")
print(f" find_min_coins() :    {find_min_coins(coin_set, sum)}")


