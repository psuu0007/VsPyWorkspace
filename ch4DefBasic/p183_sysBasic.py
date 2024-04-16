import sys

# vscode에서 실행 시 인수전달은 launch.json에서 작업함

args = sys.argv[0:]
for i in args:
    print(i)
