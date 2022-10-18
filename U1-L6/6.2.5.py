def upsidedown(s):
    temp=''
    for char in s:
        if char.isalpha():
            temp += char.lower()
    if temp[::]==temp[::-1]:
        print("是回文串")
    else:
        print("不是回文串")
upsidedown('a121212b21 a')