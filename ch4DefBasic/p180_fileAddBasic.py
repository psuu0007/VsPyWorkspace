
f = open("E:/pythonTest/새파일.txt", "a")

for i in range(11, 21):
    data = "%d번째  줄입니다\n" %i
    f.write(data)


