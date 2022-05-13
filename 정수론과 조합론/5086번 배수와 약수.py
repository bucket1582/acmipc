x, y = 1, 1
while x * y != 0:
    x, y = input().split()
    x, y = int(x), int(y)

    if x * y == 0:
        break

    # x가 y보다 크다; x가 배수일 가능성
    if x > y:
        # x가 y로 나누어떨어진다; x는 y의 배수
        if x % y == 0:
            print("multiple")
        else:
            print("neither")
    else:
        # x가 약수일 가능성
        if y % x == 0:
            print("factor")
        else:
            print("neither")
