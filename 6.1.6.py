def reverse(str_):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    Alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    temp=[]
    for i in str_:
        if i in alphabet:
            temp.append(alphabet[-(alphabet.find(i)+1)])
        if i in Alphabet:
            temp.append(Alphabet[-(Alphabet.find(i)+1)])
    print(temp)
reverse("abc")
