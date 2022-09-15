ticket=True
knife=21
if ticket==True:
    print("有票可进")
    if knife>20:
        print("🔪>20cm,不能进")
    else:
        print("通过请进")
else:
    print("无票不让进")

if ticket==True and knife<=20:
    print("请进")
elif ticket==False:
    print("无票")
elif knife>20:
    print("🔪>20cm,不能进")