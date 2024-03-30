# format 함수 또는 f 문자열 포매팅을 사용해
# !!!python!!! 문자열을 출력해 보자

resultStr = '{str:!^12}'.format(str='python')

print(resultStr)

print(str)
str = 'python'
resultStr = f'{str:!^12}'

print(resultStr)
