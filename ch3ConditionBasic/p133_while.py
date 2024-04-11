treeHit = 0

while treeHit < 10:
    treeHit = treeHit + 1
    print('나무를 %d번 찍었다' % treeHit)
    if treeHit == 10:
        print('나무 넘어간다')



# treeHit = treeHit + 1
# print('나무를 %d번 찍었다' % treeHit)
# treeHit = treeHit + 1
# print('나무를 %d번 찍었다' % treeHit)
# treeHit = treeHit + 1
# print('나무를 %d번 찍었다' % treeHit)
# treeHit = treeHit + 1
# print('나무를 %d번 찍었다' % treeHit)
# treeHit = treeHit + 1
# print('나무를 %d번 찍었다' % treeHit)

# print('나무 넘어간다')
        

""" 
1. Add
2. Del
3. List
4. Quit
Enter number: '' 
ex:
(숫자에 맞는 글자가 출력된다)
1
Add
2
Del
3
List
5
잘못된 입력입니다
1
Add
4
Quit
(프로그램 종료됨)
"""

prompt = "''"

print('1. Add')
print('2. Del')
print('3. List')
print('4. Quit')

print("Enter number: ''")

myNumber = 0
while myNumber != 4:
    myNumber = int(input())
    if myNumber == 1:
        prompt = 'Add'
    elif myNumber == 2:
        prompt = 'Del'
    elif myNumber == 3:
        prompt = 'List'
    elif myNumber == 4:
        prompt = 'Quit'
    else:
        prompt = '잘못된 입력입니다'
    print(prompt)

    
