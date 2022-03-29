-analyze number of operations algorithm performs

-space complexity and time complexity

-fast? less error prone?

-runtime is sensitive to specific computer like platform,
concurrent tasks, implementation
but does not anwalys indicate big picture/long term decisions
for that algorithm versus others


#Goal: algorithm goes from input size to number of stepps
-Focus on number of loop iterations "dominating factor"
o(n) vs. o(n^2)

    sum = 0
    for num in numbers:
        sum += num

    vs.

#double nested loop
    sum = 0
    for num in numbers:
        for fun in numbers:
        sum += num

BIG - O:
-Growth functions categorized by dominant fastest
growing term (constants and lower order dropped)
as input size increases lower order becomes irrelevant
10n = O(n)
5n^2+2n+3 = O(n^2)
nlogn +n = O(nlogn)


Big equality equaliy statements analogous to
greater than or equal to sign "upper bound" on the given function
n^2  = O(n^2)
n^2 = O(n^4) "n squared is big O of n to the 4th"
2n^2 = O(n^2) #self note i think 2 coeff is dropped to explain here

--------------
Big Omega ##the function is as bad as and often potentially worse than omega(bla)
-Tighter upped  bound than O(n)
n^4 is omega of n^2
n^4 = omega(n^2)
n! = omega(n^)2


#??????? between lower and upper boudn?
--------
T(n) big t of n describes running time of algorithm
"recurrence relation", "objective function"

Running time: based on number of primitive operations

ex:
factional(n) - input size n
sort(vals) - lenfg of vals ***

Algorithm Analysis:
1. Select a measure of input size and a basic operation
2. Develop a function T(n) that describes the
number of times the basic operation occurs as a function
of input size
3. Describe T(n) using order notation Big-O

-Each lines generates a cost
ie: for a for loop could be
    T(n) = c+2(n-1) -->>>T(n) = 2(n-1)+2 = 2n

##for sort function "worst case" arises
#when data starts out in reverse order

#???slides16 min
#tight bounds, bounds between two functions not asked about

-Using brute force crack n bit password
    -1 character is 8 bits
    -2^8 posible values (bit is 0 or 1)
    -answer O(2^n) n is number of bits?

Binary search
O(logn)

factorial, linear search O(n)

insertion search
O(n^2)

Summary:
Analyze algorithms not runtime
system dependent program
Ask how runnning time changes
as input size changes



####################
"Aalysis 1 Big O Video"
