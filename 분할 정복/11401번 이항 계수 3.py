def choose():
    global p, n_fact, k_fact, n_k_fact
    if k == 0 or k == n:
        return 1
    
    return n_fact % p * \
           recursive_pow(k_fact % p * n_k_fact % p % p, p - 2, p)

''' Pythonic
def choose_2():
    global p, n_fact, k_fact, n_k_fact
    return n_fact % p * \
           pow(k_fact % p * n_k_fact % p, p - 2, p)
'''

def recursive_pow(x, a, p):
    if x == 1:
        return 1
    if a == 0:
        return 1
    if a == 1:  
        return x % p

    if a % 2 == 0:
        ans = recursive_pow(x % p, a // 2, p)
        return ans % p * ans % p % p

    ans = recursive_pow(x % p, (a - 1) // 2, p)
    return ans % p * ans % p * x % p % p


from sys import stdin

f_input = lambda : stdin.readline().rstrip()

n, k = map(int, f_input().split())
p = 1000000007

l_factorial = 1
n_fact = 1
k_fact = 1
n_k_fact = 1
for i in range(1, n + 1):
    l_factorial *= i
    l_factorial %= p
    if i == k:
        k_fact = l_factorial
    if i == n:
        n_fact = l_factorial
    if i == n - k:
        n_k_fact = l_factorial

print(choose() % p)
