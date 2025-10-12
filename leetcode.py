# nums = [2,7,11,15]
# target = 9
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if nums[i]+nums[j]==target:
#             print([i,j])
# print([])            





arr = [1,2,3,4,5,6]
target = 8
# for i in range(len(arr)-1):
    # for j in range(len(arr)):
    #     if i+j == target:
    #        arr[i] += 1
    #        print(arr[j],i)

for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if( arr[i]+ arr[j] == target):
           print(arr[i],arr[j]) 