# 들여쓰기 오류 예제
money = True

if money:
    print('택시를')
    print('타고')
    print('가라')

# if money:
#     print('택시를')
# print('타고')
#     print('가라')


# if money:
#     print('택시를')
#     print('타고')
#         print('가라')
    
money = False
if money:
    print('택시를')
    print('타고')
print('간다')

# 공백으로도 가능한데 첫라인의 들여쓰기로 들여쓰기 레벨이 결정된다
if 1:
 print('aa')
 print('bb')

