def CFB(lieshu):
    HangShu = lieshu
    for i in range(1, HangShu + 1):
        print("%d*%d=%d" % (1, i, i), end=" ")
        if i >= 2:
            print("%d*%d=%d" % (2, i, 2 * i), end=" ")
        if i >= 3:
            print("%d*%d=%d" % (3, i, 3 * i), end=" ")
        if i >= 4:
            print("%d*%d=%d" % (4, i, 4 * i), end=" ")
        if i >= 5:
            print("%d*%d=%d" % (5, i, 5 * i), end=" ")
        if i >= 6:
            print("%d*%d=%d" % (6, i, 6 * i), end=" ")
        if i >= 7:
            print("%d*%d=%d" % (7, i, 7 * i), end=" ")
        if i >= 8:
            print("%d*%d=%d" % (8, i, 8 * i), end=" ")
        if i >= 9:
            print("%d*%d=%d" % (9, i, 9 * i), end=" ")
        print("")
CFB(9)