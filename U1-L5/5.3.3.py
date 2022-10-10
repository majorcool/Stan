dic={
    'python':95,
    'java':99,
    'c':100
}
#1
print(len(dic))
#2
dic["java"]=98
print(dic)
#3
dic.pop("c")
print(dic)
#4
dic["php"]=90
#5
temp=[]
for k in dic:
    temp.append(k)
print(temp)
#6
temp2=[]
for k in dic:
    temp2.append(dic[k])
print(temp2)
#7
if "javascript" in dic:
    print("Javascript in dic")
else:
    print("Javascript not in dic")
#8
sum=0
for k in dic:
    sum=sum+dic[k]
print(sum)
#9
temp2.sort()
print(temp2[len(temp2)-1])
#10
print(temp2[0])
#11
dic1={
    'php':97
}
dic.update(dic1)
print(dic)
