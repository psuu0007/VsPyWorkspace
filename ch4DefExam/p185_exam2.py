def avgNumbers(*numberTuple):
    result = 0
    for i in numberTuple:
        result = result + i
        
    result = result / len(numberTuple)
    return result


avgNum = avgNumbers(1, 2)
print(avgNum)

avgNum = avgNumbers(1, 2, 3, 4, 5)
print(avgNum)


