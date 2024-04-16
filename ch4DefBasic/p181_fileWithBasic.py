# with는 꽤 쓸만하네

with open("E:/pythonTest/foo.txt", "w") as f:
    for i in range(11, 21):
        data = "%d번째  줄입니다\n" %i
        f.write(data)

