def update_dict(dict_sample):
    key=str(input("输入key:"))
    value=int(input("输入value:"))
    if key in dict_sample:
        if value>dict_sample[key]:
            dict_sample[key]=value
    else:
        dict_sample[key]=value
    return dict_sample
dic={
    '1':5,
    '2':6,
    '3':7
}
print(update_dict(dic))