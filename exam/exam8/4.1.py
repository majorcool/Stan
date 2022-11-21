def small_alpha(sentence):
    alphabet="abcdefghijklmnop"
    for alpha in alphabet:
        if alpha not in sentence:
            return False
    return True
print(small_alpha("coopedu"))