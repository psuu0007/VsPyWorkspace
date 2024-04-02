""" 주민등록번호 나누기
881120-1068234 주민번호를 YYYYMMDD부분과 
그 뒤의 숫자 부분으로 나누어 출력하시오 """

pin = '881120-1068234'

# 함수 방식
yyyymmdd = pin.split('-')[0]
num = pin.split('-')[1]
print(yyyymmdd)
print(num)


# 슬라이싱 방식
yyyymmdd = pin[0:6]
num = pin[7:]
print(yyyymmdd)
print(num)

