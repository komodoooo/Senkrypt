import sys

def key(key) -> str:
    if key != None:
        numberz = []
        for i in list(key):
            a:str = bin(ord(i)).split("0b")[1]
            numberz.extend(a)
        final = int()
        for i in numberz:
            final += int(i)
        return final
    else: 
        return 0

try:
    KEY = key(sys.argv[3])
except IndexError:
    KEY = 0

def encrypt(text):
    if "-" in text:
        text.replace("-", "")
    ewe = ""
    for sex in list(text):
        e = ord(sex) * len(text) + KEY
        ewe += hex(e)
        ok = ewe.split("0x")
    assert ok, "The text isn't valid."
    print("".join(ok[::-1]))

def decrypt(text):
    first_step = [text[i:i+3] for i in range(0, len(text), 3)]
    second_step = []
    for i in first_step:
        second_step.append(int(i, 16))
    second_step = second_step[::-1]
    third_step = []
    for i in second_step:
        keyformat = int(i-KEY)
        third_step.append(int(keyformat/len(second_step)))
    final_step = []
    for i in third_step:
        final_step.append(chr(i))
    gohan = "".join([i for i in final_step])
    if "-" in gohan:
        print(gohan.replace("-", " "))
    else:
        print(gohan)

try:
    if sys.argv[1].startswith("-e"):
        encrypt(sys.argv[2])
    elif sys.argv[1].startswith("-d"):
        decrypt(sys.argv[2])
except Exception as not_sex:
    print(f"Error:\n{not_sex}")
