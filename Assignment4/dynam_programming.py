"""
Solving a problem
1) Try recursive soltuion
    2) Cache previous subproblems if possible in dictionary "memoization"

?3) Find Bottom up Dynamming programming solution
Traditional O(n) analysis is different because you dont have recursive call at all!
so its better ie: fib goes to O(2n+1)->O(n) rather than O(2^n) or a slower O(n) if memoized

    ie: in fibonacci you just have an array where you access the previous two values
        and it already starts out with the base case values 0,1,1
    ie: in min coins to return change,
        for r in remainder
            for c in coins
                if r-c>=0:
                    dp[a] = min(dp[a],1+dp[a-c])
        return dp[amount] if dp[amount] != infinite else -1
        #-1 means no solution possible bc remainder is less than coin sizes


#note negative impossible scenario is a great base case!
"""

Lesson from pascal seems to be focus on comparing the ratio
of the input size to the total number of caluclations as input size increases
ie: Total cells: 1,3,6,10,15, for each index row pondered
    which eventually overtakes quadratic. Its arithmetic sum

