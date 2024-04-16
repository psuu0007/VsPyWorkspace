for i in range(2, 10):
    for k in range(1, 10):
        print('{0} * {1} = {result}'.format(i, k, result=(i*k)), end="\t")
    print()


print()
print()
for i in range(1, 10):
    for k in range(2, 10):
        print('{0} * {1} = {result}'.format(k, i, result=(i*k)), end="\t")
    print()




print()
print()
for i in range(2, 10):
    for k in range(1, 10):
        print(f'{i} * {k} = {i * k}', end="\t")
    print()