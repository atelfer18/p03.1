"""
Problem:

    The function mult_count takes an integer n.
    It should count the number of multiples of 5, 7 and 11 between 1 and n (including n).
    Numbers such as 35 (a multiple of 5 and 7) should only be counted once.

    e.g.
    mult_count(20) = 7  (5, 10, 15, 20; 7, 14; 11)

Tests:

    >>> mult_count(20)
    7
    >>> mult_count(50)
    20
    >>> mult_count(250)
    93

"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code
def mult_count(n):

    count =  0
    
    count5 = 0
    count7 = 0
    count11 = 0

    for i in range(1, n+1, 1):
        ## need to add in for remainders for 5, 7 and 11 so do not get double count

        if i % 5 == 0 or i % 7 == 0 or i % 11 == 0

    for i in range(5, n+1, 5):

        count5 = count5 + 1
        
    for i in range(7, n+1, 7):

        count7 = count7 + 1
        
    for i in range(11, n+1, 11):
                    
            count11 = count11 + 1

    count = count5 + count7 + count11

    print(count)

    
