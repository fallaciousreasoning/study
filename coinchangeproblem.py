# https://www.hackerrank.com/challenges/coin-change/problem

def getWays(goal, coins):
    table = [[1 for i in range(len(coins))] for i in range(goal + 1)]
    
    for i in range(1, goal + 1):
        for j in range(len(coins)):
            coin = coins[j]

            x = 0 if i - coin < 0 else table[i - coin][j]
            y = table[i][j - 1] if j >= 1 else 0
            table[i][j] = x + y


    return table[goal][len(coins) - 1]


print(getWays(4, [1,2,3]))
print(getWays(10, [2, 5, 3, 6]))