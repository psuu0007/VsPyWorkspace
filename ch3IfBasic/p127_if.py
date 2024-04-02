"""
 만약 3000원 이상의 돈을 가지고 있으면 
택시를 타고 가고, 그렇지 않으면 걸어가라
 """

money = 2000
if money >= 3000:
    print('택시를 타고 간다')
else:
    print('걸어가라')


"""
 돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 가고,
  그렇지 않으면 걸어가라
 """
# and, or, not 연산자가 있네 단지 not은 논리값 앞에만 쓴다(다른 언어랑 같네)
money = 2000
card = True

if money >= 3000 or card:
    print('택시를 타고 간다')
else:
    print('걸어간다')

if money >= 3000 and card == True:
    print('택시를 타고 간다')
    print('a')
else:
    print('걸어간다')
    print('b')


jkl = 1 in [1, 2, 3]
print(jkl)

jkl = 1 not in [1, 2, 3]
print(jkl)

