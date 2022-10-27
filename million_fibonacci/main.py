

def fib(n):
    """Calculates the nth Fibonacci number"""
    nums = [0, 1]

    print(f"N: {n}")
    for i in range(1,n):
        last_num = nums[len(nums)-1]
        lsecond_last_num = nums[len(nums)-2]
        nums.append(last_num+lsecond_last_num)
    return nums[len(nums)-1]

def fib(n, computed = {0:0, 1:1}):
    if n < 0:
        return negative_fib(n, computed = {0:0, 1:1})
    if n not in computed:
        computed[n] = fib(n-1, computed) + fib(n-2, computed)
    return computed[n]

def negative_fib(n, computed = {0:0, 1:1}):
    if n not in computed:
        computed[n] = fib(n-1, computed) - fib(n-2, computed)
    return computed[n]

# print(fib(5))

print(fib(8))

# test.assert_equals(fib(0),0)
# test.assert_equals(fib(1),1)
# test.assert_equals(fib(2),1)
# test.assert_equals(fib(3),2)
# test.assert_equals(fib(4),3)
# test.assert_equals(fib(5),5)