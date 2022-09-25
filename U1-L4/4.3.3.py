def make_shirt(Size,Name='I love python'):
    return("Size=%s\nName=%s" % (Size,Name))
print(make_shirt("Big"))
a=make_shirt("Medium")
print(a)
print(make_shirt("Small","Hello World"))