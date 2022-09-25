def describe_city(City,Country="China"):
    if City=="ShangHai" and Country=="China":
        return "Yes"
    elif City=="BeiJing" and Country=="China":
        return "Yes"
    elif City=="Sydney" and Country=="Australia":
        return "Yes"
    else:
        return "No"
print(describe_city("ShangHai"))
a=describe_city("Sydney")
print(a)