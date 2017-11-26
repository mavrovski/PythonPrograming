nums = list(map(int,input().split(' ')))


while len(nums)>1:
    condensed = [None] * int(len(nums) - 1)
    for i in range (0,len(nums)-1):
        condensed[i]=nums[i]+nums[i+1]
    nums = condensed
print(nums[0])