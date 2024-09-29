def divisorGame(n: int) -> bool:
    T = [False] * (n + 1)
    if n == 1:return False
    for i in range(2, n + 1):
        for x in range(1, i):
            if i % x == 0 and not T[i - x]:
                T[i] = True
                break
    
    return T[n]

print(divisorGame(2))
print(divisorGame(3))
