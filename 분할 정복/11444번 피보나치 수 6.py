R = 1000000007
MEMOI = {0: 0, 1: 1, 2: 1}
def quick_fib(n):
    # d'Ocagne's identity & Memoization
    global R, MEMOI
    if n in MEMOI.keys():
        return MEMOI[n]
    if n % 2 == 0:
        left_fib = quick_fib(n - 1) % R
        right_fib = quick_fib(n + 1) % R
        ans = right_fib - left_fib
        ans %= R
        MEMOI[n] = ans
        return ans
    k = (n + 1) // 2
    left_fib = quick_fib(k - 1) % R
    right_fib = quick_fib(k) % R
    ans = left_fib * left_fib % R + right_fib * right_fib % R
    ans %= R
    MEMOI[n] = ans
    return ans
    


from sys import stdin

f_input = lambda : stdin.readline().rstrip()

n = int(f_input())
f_n = quick_fib(n)
print(f_n)
