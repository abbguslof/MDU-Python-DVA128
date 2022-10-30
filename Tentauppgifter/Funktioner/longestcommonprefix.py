def longest_common_prefix(a, b):
    prefix = ''
    if a == b:
        return a
    if a < b:
        a, b = b, a
    for x in range(len(b)):
        if a[x] == b[x]:
            prefix += a[x]
        else:
            return prefix

a = input('a = ')
b = input('b = ')
print('-----')
c = longest_common_prefix(a, b)
print('LCP:', c)