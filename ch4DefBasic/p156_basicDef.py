# 155 설명 나쁘지 않은듯
# 1.
def add(a, b):
    return a + b

a = 3
b = 4

c = add(a, b)
print(c)

# 2.
def say():
    return 'hi'

a = say()
print(a)


# 3.
def add(a, b):
    print("%d, %d의 합은 %d입니다." %(a, b, a+b))

a = add(1, 7)

print(a)

# 4.
def say():
    print('Hi')

say()
