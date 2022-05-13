def euclidean_method(a, b):
    while a % b != 0:
        r = a % b
        a = b
        b = r
    return b

T = int(input())
for _ in range(T):
    raw = input().split()
    a, b = int(raw[0]), int(raw[1])
    if a > b:
        gcd = euclidean_method(a, b)
    else:
        gcd = euclidean_method(b, a)
    lcm = (a * b) // gcd
    print(lcm)
