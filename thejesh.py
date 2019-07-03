def findpair(list1, k):
    for i in range(0, len(list1)):
        for j in range(0, len(list1)):
            if k == list1[i] + list1[j]:
                return True    
    return False       
nums = [10, 5, 6, 7, 3]
k = 100
print(findpair(nums, k))
