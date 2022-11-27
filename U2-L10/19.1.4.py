def Area(r):
    if r>=0:
        return 3.14*r**2
    else:
        Radiuserror=Exception("RadiusError")
        raise Radiuserror
print(Area(-1))