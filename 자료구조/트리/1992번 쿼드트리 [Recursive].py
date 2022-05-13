def recursive_quad_tree(partial_image, N):
    image_all_true_flag = True
    image_all_false_flag = True

    for row in partial_image:
        for val in row:
            if val == 1:
                image_all_false_flag = False
            else:
                image_all_true_flag = False

    if image_all_true_flag:
        return "1"
    if image_all_false_flag:
        return "0"

    lu = []
    ru = []
    ld = []
    rd = []
    for row in range(N):
        if row < N // 2:
            lu.append(partial_image[row][:N // 2])
            ru.append(partial_image[row][N // 2:])
        else:
            ld.append(partial_image[row][:N // 2])
            rd.append(partial_image[row][N // 2:])

    return "(" + recursive_quad_tree(lu, N // 2) +\
           recursive_quad_tree(ru, N // 2) +\
           recursive_quad_tree(ld, N // 2) +\
           recursive_quad_tree(rd, N // 2) + ")"

    

from sys import stdin

f_input = lambda : stdin.readline().rstrip()

N = int(f_input())
image = []
for _ in range(N):
    image.append([int(t) for t in f_input()])

print(recursive_quad_tree(image, N))
