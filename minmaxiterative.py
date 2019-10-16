import random

def Randomgen(start,end,num):
    res=[]
    for j in range(num):
        res.append(random.randint(start,end))
    return res

num=10
start=10
end=90
marks = Randomgen(start,end,num)
# max1=marks[0]
# min1=marks[0]
maxi=[]
mini=[]
maxi.append(marks[0])
mini.append(marks[0])

print(marks)
i=1
for i in range(num):
    if marks[i]>maxi[-1]:
        # max1=marks[i]
        maxi.append(marks[i])
    if marks[i]<mini[-1]:
        # min1=marks[i]
        mini.append(marks[i])

print("Maximum Stack:"+str(maxi))
print("Minimum Stack:"+str(mini))
print("Maximum marks: "+str(maxi.pop()))
print("Minimum marks: "+str(mini.pop()))



