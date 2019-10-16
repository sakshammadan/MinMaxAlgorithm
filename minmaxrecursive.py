import random
minimum=[100]
maximum=[0]
k=1

def Randomgen(start,end,num):
    res=[]
    for j in range(num):
        res.append(random.randint(start,end))
    return res

def MinMax(i,j,marks):
    global k
    if j-i<=1:
        maxi=(max(marks[i],marks[j]))
        if(maxi>maximum[-1]):
            if k==1:
                maximum.pop()
            maximum.append(maxi)
        mini=(min(marks[i],marks[j]))
        if(mini<minimum[-1]):
            if k==1:
                minimum.pop()
            minimum.append(mini)
        k=k+1
    else:
        mid=(i+j)//2
        MinMax(i,mid,marks)
        MinMax((mid+1),j,marks)


num=10
start=10
end=90
marks = Randomgen(start,end,num)
print(marks)


MinMax(0,(num-1),marks)
print("Stack maximum:"+str(maximum))
print("Stack minimum:"+str(minimum))

print("Maximum marks: "+str(maximum[-1]))
print("Minimum marks: "+str(minimum[-1]))
