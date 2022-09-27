numlist = [1,2,3,4,5]
numlist.insert(0,0)
print("step0:",numlist)
numlist.append(6)
print("step1:",numlist)
temp=[7,8]
numlist.extend(temp)
print("step2:",numlist)
del numlist[8]
print("step3:",numlist)
del temp
print("step4:报错")
numlist.remove(7)
print("step5:",numlist)
numlist.pop()
print("step6",numlist)
numlist.clear()
print("step7:",numlist)
numlist = [1,2,3,4,5]
numlist[0]=0
print("step8:",numlist)
numlist.sort()
print("step9:",numlist)
numlist.sort(reverse=True)
print("step10:",numlist)
numlist.reverse()
print("step11:",numlist)
print("step12:",len(numlist))
print("step13:",numlist.count(0))