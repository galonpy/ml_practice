#  File Dependencies: CS3C_a4Soln.py
#  Topic: Recursion 
#  Application:  Pascal's Triangle 
#  Time Complexity: O(2^n)
#  Space Complexity: Infinite two-dimensional  
#  Development Environment:  Ubuntu 17.0
#  Version: Python 3.7
#  Solution File: CS3C_a4Soln.py
#  Date: 02/01/22

def pascalLine(n):
    print("recursive call")
    '''returns a list of nth line of Pascal's triangle'''
    if n == 0:       # base case
        return [1]

    # induction step: start by generating line n-1
    prev = pascalLine(n-1)

    # use line n-1 to generate line n
    res = [1]
    for index in range(len(prev)-1):
        res.append(prev[index]+prev[index+1]) #you produce a new data point for each pair of points in prior list, make it always longer'
    res.append(1)
    return res

pascalLine

def sum_cells(n):
    count = 1
    for i in range(n):
        count += i+1
    print(count)

#x = 10000000
#sum_cells(x)
#print(x*x, "quadtraic")

#x = 25 *(2+49)
#print(x)