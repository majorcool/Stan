def pref(words,pref):
    long=len(pref)
    count=0
    for items in words:
        if items[:long]==pref:
            count+=1
    print(count)
pref(words = ["coopedu","win","loops","success"], pref = "code")