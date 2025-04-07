# Реалізувати функцію яка приймає список і число і видає пари чисел які в сумі дають це число
from copy import deepcopy

# def find_pairs(nums: list[int], target: int) -> list[tuple[int, int]]:
#     seen = set()
#     res = set()    
#     nums.sort()
#     for elem in nums:
#         second = target - elem
        
#         if second in seen:
            
#             res.add(tuple(sorted((elem, second))))
#         seen.add(elem)
            
#         if second + elem > target:
#             return list(res)
#     return list(res)

def find_pairs(nums1: list[int], target: int) -> list[tuple[int, int]]:
    nums = deepcopy(nums1)
    seen = set()
    res = set()
    
    for num in nums:
        complement = target - num
        if complement in seen:
            # Сортуємо пару для унікальності: (менше, більше)
            res.add(tuple(sorted((num, complement))))
        seen.add(num)
        
    return list(res)

# def find_pairs1(nums: list[int], target: int) -> list[tuple[int, int]]:
#     #seen = set()
#     res = set()
#     nums.sort()
    
#     right_edge = len(nums) -1 
#     left_index =0
#     while (right_edge>left_index):
        
#     #for num in nums:
#         notFind = True
#         while notFind:
#             if right_edge>0:
#                 if nums[right_edge] + nums[left_index] == target:
#                     res.add(tuple(sorted((nums[right_edge], nums[left_index]))))
#                     left_index+=1
#                     notFind=False
#                 right_edge -= 1
#             else:
#                 return []
        
#     return list(res)

def find_pairs1(nums: list[int], target: int) -> list[tuple[int, int]]:
    nums.sort()
    res = set()
    
    left = 0
    right = len(nums) - 1

    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            res.add((nums[left], nums[right]))
            left += 1
            right -= 1
        elif s < target:
            left += 1
        else:
            right -= 1
    
    return list(res)


        
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    target = 5
    print(find_pairs(nums, target))
    print(find_pairs1(nums, target))
    
    nums = [1, 2, 2, 3, 4]
    target = 5   
    
    print(find_pairs(nums, target))
    print(find_pairs1(nums, target))
    nums = [-3, -1, 0, 1, 2, 4]
    target = 1

    
    print(find_pairs(nums, target))
    print(find_pairs1(nums, target))
    nums = [2, 2, 2, 2]
    target = 4

    
    
    print(find_pairs(nums, target))
    print(find_pairs1(nums, target))
    #nums = [1, 3, 5]
    nums = [1,2,4, 6, 7, 9, 11, 15]
    #target = 10
    target = 5
    
    
    print(find_pairs(nums, target))
    print(find_pairs1(nums, target))
            
            
        
            
