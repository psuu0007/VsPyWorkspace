# 176페이지의 파일 경로와 슬래시(/) 내용은 볼 만함
# 둘 다 실행될 줄이야

f = open("E:/pythonTest/새파일.txt", "w")
# f = open("E:\\pythonTest\\새파일.txt", "w")


for i in range(1, 11):
    data = "%d번째  줄입니다\n" %i
    f.write(data)

f.close()
