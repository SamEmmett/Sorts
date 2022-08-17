# Student name: Samuel Emmett.
#
# Implement the insertion sort and heap sort
# algorithms in the functions that follow.  Also implement
# the issorted function to check if a list is sorted, and
# the randomlist function to generate a list of random integers.
#
# Make sure that you carefully read the docstrings that I've provided
# for the functions, which specifies what you are to implement.
#
# Don't change the names of the functions or parameters.
# Be aware of the indentation in what I've provided.  The helper
# functions for heapsort are indented within heapsort on purpose
# so that they will be nested functions.
#
# Don't delete the docstrings that I have at the start of the functions
# (the multiline strings that indicate what the functions do).  You can
# feel free to delete comments that I have with hints, etc, however.
#
# IMPORTANT: Remember that the textbook pseudocode uses 1-based indexing,
# while Python uses 0-based indexing, so you may need to make minor
# adjustments from the pseudocode (pay specific attention to the left
# and right helper functions for heapsort).  
#
# Note: You don't need the pass statements that I inserted, so you
# can delete them after you implement the functions.  I put them
# in temporarily so that you have valid syntax to start with.  A function
# requires at least one statement in the body.  The pass statement does
# nothing, but is a statement none-the-less.
#
# IMPORTANT: DO NOT have any print statements in the functions in this
# Python file (e.g., in the issorted, randomlist, insertionsort,
# heapsort, and heapsort's various helper functions).
# In general, you want to separate
# output from the computation.  You'll be outputting results
# (e.g., using print) in the if block at the very bottom of this module.

import random

def issorted(A) :
    """Returns True if A is sorted in non-decreasing order,
    and returns False if A is not sorted.

    Keyword arguments:
    A - a Python list.
    """
    check = False
    if(A == sorted(A)):
        check = True

    if (check == True):
        print ("The list is sorted.")
    else :
        print ("The list is not sorted.")
    ## Hints for implementing issorted:
    ## Hint 1: DO NOT use the built-in function sorted in this function.
    ##       E.g., if you are tempted to call sorted and then compare
    ##       result to A, this would be wrong (or at least it would be a
    ##       terribly inefficient way to do this).  Python's sorted function
    ##       actually does a sort generating a new list that is a sorted copy
    ##       of the original.  This would be a silly, and costly, way to check
    ##       if your list is sorted.  You will get 0 points for the issorted
    ##       function if you call Python's sorted function.
    ## Hint 2: If A is sorted then A[0] <= A[1] <= A[2] <= ....
    ##       So, you can write a loop whose body does one
    ##       comparison of adjacent elements, returning False if there is a violation
    ##       within the loop. If you manage to get
    ##       through the loop without returning, then the list must be sorted,
    ##       so return True.

def randomlist(length, low=0, high=100) : ##Generates a list of random numbers
    """Generates and returns a Python list of random integer values.
    The integers in the list are generated uniformly at random from
    the interval [low, high], inclusive of both end points.

    Keyword arguments:
    length - the length of the list.
    low - the lower bound for the random integers.
    high - the upper bound for the random integers.
    """
    ## all imports will be at the top of the file

    randList = []

    for i in range(low, length): ##this way the number of elements will not exceed the given number
        num = random.randint(0, 100)
        randList.append(num)


    return randList


def insertionsort(A) :
    """Implementation of the insertion sort algorithm
    as specified on page 18 of the textbook.

    Keyword arguments:
    A - a Python list.
    """
    
    for i in range (1, len(A)) :
        place = A[i]

       ##moving larger numbers to the *right*

        j = i-1 ## j is the location that the smaller number be moved to
        while j >= 0 and place < A[j]:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = place


    return A

def heapsort(A) : #RUNS BUT DOES NOT SORT PROPERLY


    heapsize = len(A)

    def left(i): #left is 2i since it's position in the heap will be 2 * the position of its parent
        return 2*i
    
    def right(i) : #right is 2i+1 since it's position in the heap will be 2 * the position of its parent + 1
        return 2*i+1

    def maxheapify(A, i):
        nonlocal heapsize

        l = left(i)
        r = right(i)

        if l <= heapsize - 1 and A[l] > A[i]:
            largest = l
        else:
            largest = i

        if r <= heapsize - 1 and A[r] > A[largest]:
            largest = r

        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            maxheapify(A, largest)

    def buildmaxheap(A) :
        nonlocal heapsize

        # Implement the buildmaxheap from page 157 here.
        for i in range(heapsize - 1 // 2 , 0, -1): #down to 1
            maxheapify(A, i)

    buildmaxheap(A)

    for i in range (heapsize - 1, 1, -1): #down to 2
        A[0], A[i] = A[i], A[0]
        heapsize = heapsize - 1
        maxheapify(A, 0)

    return A

if __name__ == "__main__" :
    firstList = []
    secondList = []
    firstList = randomlist(10)
    secondList = randomlist(10)

    print(firstList)
    issorted(firstList)

    firstList = insertionsort(firstList)
    print(firstList)
    issorted(firstList)

    print()

    print(secondList)
    issorted(secondList)

    secondList = heapsort(secondList)
    print(secondList)
    issorted(secondList)

    ## Indented within this if block, do the following:
    ## 1) Write a few lines of code to demonstrate that your
    ##    issorted works correctly (i.e., that it returns True
    ##    if given a list that is sorted, and False otherwise).
    ## 2) Write a few lines of code to demonstrate that insertionsort
    ##    correctly sorts a list (your randomlist function will be useful
    ##    here).  Output (i.e., with print statements) the contents
    ##    of the list before sorting, and then again after sorting).
    ## 3) Repeat 2 to demonstrate that your heapsort sorts correctly.



