def float_input(x):
    if type(x)!=float:
        Er=Exception("GetFloatError")
        print("not float")
        raise Er
    return x
print(float_input(2.2))
