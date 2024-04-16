# kwargs(keyword arguments): 딕셔너리 타입

def printKwargs(**data):
    print(data)


printKwargs(a = 1)

printKwargs(name="lee", age='3')

def printKwargs(**data):
    return data

a = printKwargs(name="lee", age='3')

print(a['name'])


