def openFile(filename):
    with open(filename) as fhand:
        lines=fhand.readlines()
    return lines

def puzzle1(nums):
    cnt=0
    n=len(nums)
    for i in range(0,n-1):
        #check adjcent values whether increasing or not
        if(nums[i+1]>nums[i]):
            cnt+=1
    return cnt

def puzzle2(nums):
    #here window size is 3
    ans=0
    i=0
    j=0
    n=len(nums)
    sum=0
    prev=-1
    while j<n:
        sum+=nums[j]
        print(j-i+1)
        if j-i+1==3:
            if prev==-1:
                prev=sum
            else:
                if sum>prev:
                    ans+=1
                prev=sum
            sum-=nums[i]
            i+=1
        j+=1

    return ans
        

lines=openFile("day1/input1.txt")
nums=[int(line.strip()) for line in lines]

print(puzzle1(nums))
print(puzzle2(nums))


