# 매개변수를 지정하여 호출하기?
# 아 매개변수랑 무조건 일치해야 하네

def sub(a, b):
    return a - b

result = sub(b=1, a=3)
# result = sub(b=1, c=3) #오류가 나네

print(result)

result = sub(1, 3)

print(result)