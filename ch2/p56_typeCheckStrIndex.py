a = 'Life is too short, You need python'

print(a)

print(a[0])


print(a[19:22])

print(a[19:-1])

print(len(a))

print(a[0:len(a)])

#슬라이스로 문자열을 대체하네 뭐 비슷하지
a = "Pithon"

#print(a[1])
#a[1] = 'y' # TypeError: 'str' object does not support item assignment: python으로 문자열이 변하지 않는다 

#print(a)

a = "20010331Rainy"

print(a[::2])

a = a[0:8]

print(a)
print(a[::2])
print(a[::-2])