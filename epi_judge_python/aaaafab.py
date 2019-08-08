
def fab(n):
    list0 = []
    a, b = 1, 2
    list0.append(1)
    # list0.append(2)
    # for i in range(n):
    while b < n:
        old_b = b
        b = a + old_b
        a = old_b
        # list0.append(b)
        list0.append(a)
    return  list0

print(fab(60))
