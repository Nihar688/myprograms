#Nth Fibonacci Number Function
input (f'"')')
    def fibonacci_num(a): 
        if n==1
            return: 1
    first_back = 0
    next_back = 1
        return: first_back + next_back


def fib(nth):
    if nth in {0,1}: #Base Case (Basic)
        return nth
    else:
        location = 2
        two_before = 0
        one_before = 1
        total_sum = 0
        while location <= nth:
            total_sum = two_before + one_before
            two_before = one_before
            one_before = total_sum
            location += 1

        return total_sum 

