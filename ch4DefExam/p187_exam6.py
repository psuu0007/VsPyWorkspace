# 이거 인코딩은 가르치기 쉽겠다

userInputStr = input("저장할 내용을 입력하세요:")

f = open("E:/pythonTest/test.txt", "a", encoding="utf-8")
f.write(userInputStr)
f.write("\n")
f.close()

