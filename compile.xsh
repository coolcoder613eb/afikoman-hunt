import sys

def compile(exename):
    @(sys.executable) -m nuitka main.py -o @(exename) --standalone --onefile --disable-console --enable-plugin=tk-inter --include-data-dir=./customtkinter=./customtkinter


i = input("(D)emo, (R)elease, or (C)lean?")
if i == 'd':
    compile('Afikoman Hunt Demo')
elif i == 'r':
    compile('Afikoman Hunt')
elif i == "c":
    rm -rf main.build main.dist main.onefile-build