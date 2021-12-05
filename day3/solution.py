def openFile(path):
    with open(path) as fhand:
        return fhand.readlines()

def binToint(ip):
    ans=0
    p=1
    for i in range(len(ip)-1,-1,-1):
        ans=ans+int(ip[i])*p
        p=p*2

    return ans

def puzzle1(arr):
    one=0
    zero=0
    gamma=""
    epsilon=""
    for i in range(0,len(arr[0])):
        for x in range(0,len(arr)):
            if arr[x][i]=='1':
                one+=1
            else:
                zero+=1
        print(zero,one)
        if zero<one:
            gamma+='1'
            epsilon+='0'
        else:
            gamma+='0'
            epsilon+='1'
        one=0
        zero=0
    print(gamma,epsilon)

    return binToint(gamma)*binToint(epsilon)

def majorityBit(arr,oxygen, pos):
    pos=pos%len(arr[0])
    one=0
    zero=0
    for x in range(0,len(arr)):
        if arr[x][pos]=='1':
            one+=1
        else:
            zero+=1
    if zero<one and oxygen==True:
        return 1
    elif zero>one and oxygen==True:
        return 0
    elif zero==one and oxygen==True:
        return 1
    elif zero==one and oxygen==False:
        return 0
    elif zero<one and oxygen==False:
        return 0
    else:
        return 1
        

def recur(oxygen,carbon,pos):
    if len(oxygen)==1 and len(carbon)==1:
        return ;
    if len(oxygen)!=1:
        oxyBit=majorityBit(oxygen,True,pos)
        temp1=[]
        for x in oxygen:
            if x[pos]==str(oxyBit):
                temp1.append(x)
        oxygen.clear()
        oxygen.extend(temp1)
    if len(carbon)!=1:
        carBit=majorityBit(carbon,False,pos)
        temp2=[]
        for y in carbon:
            if y[pos]==str(carBit):
                temp2.append(y)
        carbon.clear()
        carbon.extend(temp2)
    recur(oxygen,carbon,(pos+1)%len(oxygen[0]))
    

def puzzle2(lst):  
    oxygen=[]
    carbon=[]

    b1=majorityBit(lst,True,0)
    b2=majorityBit(lst,False,0)

    for i in lst:
        if i[0]==str(b1):
            oxygen.append(i)

    for i in lst:
        if i[0]==str(b2):
            carbon.append(i)

    recur(oxygen,carbon,1)
    return binToint(oxygen[0])*binToint(carbon[0])
    
    


ip=openFile('day3/input.txt')
nums=[i.strip() for i in ip]
print(puzzle1(nums))
print(puzzle2(nums))
