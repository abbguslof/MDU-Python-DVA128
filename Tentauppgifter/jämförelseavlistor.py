list_a = [4, 1, 9, 4, 7, 9, 3, 8, 5, 8]
list_b = [4, 1, 1, 4, 7, 9, 6, 8, 5, 8]

for x in range(len(list_a)):
    if list_a[x] != list_b[x]:
        print(str(list_a[x]) + ' < - > ' + str(list_b[x]) + ' <- diff')
    else:
        print(str(list_a[x]) + ' < - > ' + str(list_b[x]))