

f = open("E:/pythonTest/새파일.txt", "r")

lines = f.readlines()

# print(lines)

for line in lines:
    line = line.strip() #줄바꿈  문자 제거
    print(line)

f.close()
