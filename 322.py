from typing import List
def coinChange( coins: List[int], amount: int) -> int:
    if amount == 0: return 0
    if (len(coins) == 1) and (amount % coins[0] == 0):
        return amount // coins[0]
    elif len(coins) == 1:
        return -1
    n = amount + 1
    T = [float('inf')] * n
    T[0] = 0
    for value in coins:

        if value <= amount:
            T[value] = 1

    for i in range(0 , n):
        for j in coins:
            if i - j >= 0:
                T[i] = min(T[i], T[i-j] + 1)
    if T[n-1] == float('inf'): return -1
    return T[n-1]
coins = [1]
amount = 2
print(coinChange(coins, amount))