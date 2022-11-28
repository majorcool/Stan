def Cap(title):
    title=title.split()
    Title=''
    for item in title:
        if len(item)<=2:
            for char in item:
                Title+=(char.lower())
        else:
            Title+=item[0].upper()
            for i in range(1,len(item)):
                Title+=item[i].lower()
        Title+=' '
    return Title
print(Cap("First leTTeR of EACH WoRD"))





