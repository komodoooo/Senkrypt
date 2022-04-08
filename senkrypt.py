import sys

def crypt(text):
    if "-" in text:
        text.replace("-", "")
    ewe = ""
    for sex in list(text):
        e = ord(sex) * len(text)
        ewe += hex(e)
        ok = ewe.split("0x")
    assert ok, "The text isn't valid."
    print("".join(ok[::-1]))


def decrypt(text):
    #assert len(text)%3==0, "Invalid text"
    first_step =  [text[i:i+3] for i in range(0, len(text), 3)]; second_step = []
    for i in first_step:
        second_step.append(int(i, 16))
    second_step = second_step[::-1]; third_step = []
    for i in second_step:
        third_step.append(int(i/len(second_step)))
    final_step = []
    for i in third_step:
        final_step.append(chr(i))
    gohan = "".join([i for i in final_step])
    if "-" in gohan:
      print(gohan.replace("-", " "))
    else:
      print(gohan)


try:
    if sys.argv[1].startswith("-c"):
        crypt(sys.argv[2])
    elif sys.argv[1].startswith("-d"):
            decrypt(sys.argv[2])
except Exception as not_sex:
    print(f"Error:\n{not_sex}")
        

