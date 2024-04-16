# import math
""" 
9명의 학생 중간고사 점수의 평균을 구하시오
70, 60, 55, 75, 95, 90, 80, 85, 100
"""

studentScoreList = [70, 60, 55, 75, 95, 90, 80, 85, 100]
sum = 0



for score in studentScoreList:
   sum = sum + score
   print(f'더한 값: {sum}')
   
   
aver = sum / len(studentScoreList)   
# aver = math.floor(aver * 100) / 100
aver = int(aver * 100)#소수점 셋째자리 내림처리
aver = aver / 100
print('%0.2f' %aver)    
