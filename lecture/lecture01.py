# RECURSION
# process that calls on itself


# fn which prints even numbers from N to 0
# def print_numbers(n):
#     for i in range(n, 0, -1):
#         print(i)

# O(n) function gets called N times
def print_num(n):
    print(n)
    # base case (i.e. the code that tells us to stop running function)
    if n == 0:
        return
    # recursive case (i.e. the case which takes us to next subproblem)
    print_num(n-1)


# print_num(10)
# O(2^n) the two comes from calling the recursion twice.
def double_print_num(n):
    print(n)
    if n == 0:
        return

    double_print_num(n-1)
    double_print_num(n-1)
    return


# double_print_num(3)

# Fibonaaci Sequence
# 0 1 1 2 3 5 8 13 21 34 55

# Fib(n) = Fib(n-1) + Fib(n-2)
# Base case: at n =0,  Fib(0) == 0
# at n=1, Fib(1) == 1
######RUNTIME IMPORTANT###########
# RUNTIME 2^n
##################################
# Every recursive function MUST HAVE BASE CASE which is some code that DOES NOT INVOKE ITSELF (the function it's in)
def fib(n):
    # Base case
    if n == 0:
        return 0
    if n == 1:
        return 1

    # recursive case
    result = fib(n-1) + fib(n-2)
    return result


# print(fib(10))

# divide and conquer
