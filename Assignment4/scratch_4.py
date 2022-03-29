def ok(n):
    if n<10:
        print(n)
    else:
        print(n,"here is n")
        ok(n//10) #gives largest integer cofactor of n. #has applications to dropping last digit
        print(n%10,"here is the remainder", n, "second is n")
ok(3124)
"""
#prints out
3124 here is n
312 here is n
31 here is n
3
1 here is the remainder 31 second is n
2 here is the remainder 312 second is n
4 here is the remainder 3124 second is n

#versus the "stack of the execution" 
line =7
n = 31
line =7
n = 312
line =7
n = 3124
"""

#iterative
def add_numbers(upper):
   total = 0
   for number in range(upper + 1): #so that upper itself is in calculation cause 0 does nothing
      print(number, "number here")
      total += number
   return number
#print(add_numbers(4))

def add_numbers(upper):
   if upper == 0:
      return upper # base case ###immediately triggered if upper input is 0
   else:
      return upper + add_numbers(upper - 1)


   """
   Implement a recursive function reverse() 
   that takes a nonnegative integer as input and 
   prints its digits vertically, starting with the low-order digit.
   """
