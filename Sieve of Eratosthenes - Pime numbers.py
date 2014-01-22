'''This is a prime number sieve based upon the sieve of Eratosthenes.
   Originally I saw this attempted at http://stackoverflow.com/questions/15347174/python-finding-prime-factors
   by the user Ashwini Chaudhary.  It was my oppinion it could be written more efficiently.
   This is my v 1.0.'''

   """This version is on hold, while I build a version of it in LUA for a class"""

def primeSieve(num):
    ## If the input number is less than 2 there are no possible primes.
    if num < 2:
        return []
    ## Generate a list from 2(the first prime) to the input number.
    ## By not adding any even numbers to the list (other than 2), we can save one run of the inner loop during list generation.
    numList = [2] + [i for i in range(3, num+1, 2)]
    ## Start sieve at three, because 2 was taken care of in the list generation.
    currentPrime = 3
    ## Set the end value for the inner loop.
    ## Perform operation here to prevent continuously making the calculation in the inner loop.
    innerMax = num//2+1
    ## As long as the currentPrime^2 is less than or equal to the input number there continues to be a chance to remove more numbers.
    for currentPrime in numList:
        ## The counter for the inner loop only needs to start at the value of the current Prime being evaluated.
        ## All numbers below that point have already been calculated.
        innerCounter = currentPrime
        while innerCounter <= innerMax:
            if currentPrime * innerCounter in numList:
                numList.remove((currentPrime * innerCounter))  ##must redo this so as not to continuously recreate list.
            innerCounter += 1
    return (numList)
    
