# 다양한 파일내용 불러오기

f = open("E:/pythonTest/새파일.txt", "r")

lines = f.readlines()

# print(lines)

for line in lines:
    line = line.strip() #줄바꿈  문자 제거
    print(line)

f.close()


# f = open("E:/pythonTest/새파일.txt", "r")

# data = f.read()
# print(data)
# f.close()




f = open("E:/pythonTest/새파일.txt", "r")

# print(lines)

for line in f:
    print(line)

f.close()