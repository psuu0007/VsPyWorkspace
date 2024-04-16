# 파일의 문자열 바꾸기
# 이 문제 정도면 괜찮은 시험문제

# 초기 설정
initTxtStr = "Life is too short\n" + "you need java\n"

with open("E:/pythonTest/test.txt", "w", encoding="utf-8") as f:
    f.write(initTxtStr)




# 여기서 코드 구현
# java라는 문자열을 python으로 바꾸어 저장하기
txtReplace = ""

with open("E:/pythonTest/test.txt", "r", encoding="utf-8") as f:
    txtLines = f.readlines()
    for line in txtLines:
        # line = line.strip()
        
        if line.find("java") != -1:
            line.replace("java", "python")
            # print(line)
        txtReplace = txtReplace + line


with open("E:/pythonTest/test.txt", "w", encoding="utf-8") as f:
    f.write(txtReplace)



