#The big O LESSON

'''Multiple notations when analyzing the complexity of an algorithm - Big omega, theta, and big o
BIG O notation : A mathematical notation that describes the limiting behaviour of a function as its input/parameter/argument approaches infinity
Consider the Big-O to tell us the “Worst case scenario performance” of our algorithm. 

Algorithm Proof
1. To prove that our algorithm A is better than algorithm B, we must have a proof that our Big-O notation is better

2. Measure Performance, Run-time, or Disk Usage
Our algorithms are designed to solve problems; however, reaching the solutions must not be feasible due to time or disk-space constraints

3. Mathematically Formalizing our Algorithms
Different hardware will output different runtimes; therefore, we needed a formal mathematical analysis

- Consider the function: f(x)
To analyze the worst-case scenario / behaviour of f(x) we need to find the Big-O notation for f(x)
→ O(f(x))
Then it can be classified with one of its Big-O Notation

LIST OF COMMON BIG-0 NOTATION
The following is the list from best to worst performance:

1. O(1) → Constant Complexity
    - Constant Time Algorithms: Completes the execution in the same amount of time regardless of its input.
Examples:
Accessing a data point in a list with a known index
Given two numbers, report the sum
Set and Dictionary Membership

2. O(log n) → Logarithmic Complexity
    - Logarithmic Time Algorithm: If N was the size of the input, the algorithm will take log(n) steps to solve a problem.
Most cases will use a log with a base of 2 → log2 
When the input set is continuously divided by two, it is usually a logarithmic complexity algorithm
Example:
Binary Search

3. O(n) → Linear Complexity
    - Linear Time Algorithm: The completion of the algorithm is directly proportional to the size of the input.
Example:
Simple Factor Finder
Search for an item in a list
Searching a queue
Adding two n-bit integers

- O(n log n) → Linearithmic Complexity
- O(n2) → Quadratic Complexity






MERGE SORT

Merge Sort: A comparison-based algorithm that sorts a given dataset. It is classified as a “divide and conquer” algorithm
There are 2 approaches to implementing a merge sort:
-Top-Down Implementation
- Bottom-Up Implementation

Complexity of Merge Sort:
O(n log n) Worst Case Performance'''

def mergeSort(a_list):
    #consider me as the split fing 
    #base case
    if len(a_list) <= 1:
        return a_list

    mid = len(a_list) // 2
    first_half = a_list[:mid]
    seond_half = a_list[mid:]

    first_half = mergeSort(first_half)
    second_half = mergeSort(second_half) 

    return combine(first_half, second_half)

def combine(left, right):
    if len(left) == 0 and len(right) == 0:
        return []
    elif len(left) == 0:
        return right
    elif len(right) == 0:
        return left 
    else:
        #both left and right have values
        i = 0 
        j = 0
        answer = []
        while i < len(left) and j < len(right):
            if len[i] < right[j]:
                answer.append(left[i])
                i += 1
            else:
                answer.append(right[j])
                j += 1
        while i < len(left):
            answer.append(left[i])
            i += 1
        while j < len(right):
            answer.append(right[j])
            j += 1

        return answer


