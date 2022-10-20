def reverse(n):
    n=str(n)
    if len(n)==1:
        return n
    else:
        return reverse(n[1:])+n[0]
print(reverse(123))