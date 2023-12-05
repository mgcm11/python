n1 = [30,60,20,3,5]
n2 = [60,43,21,5,8]
n3 = []
n4 = []


# for i in n1:
    # for j in n2:
        # if i == j:
            # print(i)
            # n3.append(j)
# print(n3)
for i in n1:
    for j in n2:
        if i % j == 0:
            n4.append(i)
            print(n4)
        