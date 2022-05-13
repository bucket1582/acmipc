num_of_testcases = int(input())

for i in range(num_of_testcases):
    num_of_wearables = int(input())
    fashion_dict = dict()
    for j in range(num_of_wearables):
        cloth, type_of_cloth = input().split()
        if type_of_cloth in fashion_dict:
            fashion_dict[type_of_cloth] += 1
        else:
            fashion_dict[type_of_cloth] = 2

    all_cases = 1
    for value in fashion_dict.values():
        all_cases *= value
    all_cases -= 1

    print(all_cases)
