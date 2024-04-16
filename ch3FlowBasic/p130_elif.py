""" 주머니에 돈이 있으면 택시를 타고 가고,
주머니에 돈은 없지만 카드가 있으면 택시를 타고 가고,
돈도 없고 카드도 없으면 걸어가라 """


pocket = ['money', 'phone']

if 'money' in pocket:
    jkl = '돈을 이용해서 택시를 타고 간다'
elif 'card' in pocket:
    jkl = '카드를 이용해서 택시를 타고 간다'
else:
    jkl = '걸어간다'

print(jkl)


# 중첩 if문
pocket = ['card', 'phone']

if 'money' in pocket:
    jkl = '돈을 이용해서 택시를 타고 간다'
else:
    if 'card' in pocket:
        jkl = '카드를 이용해서 택시를 타고 간다'
    else:
        jkl = '걸어간다'

print(jkl)


