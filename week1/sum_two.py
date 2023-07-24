# def twoSum(nums, target):
#     for index, num1 in enumerate(nums):
#         j_index = index + 1
#         for j_index, num2 in enumerate(nums):
#             if num1 + num2 == target:
#                 print("result", index, j_index)

def twoSum(nums, target):

    for index, num1 in enumerate(nums):
        j_index = index + 1
        for j_index, num2 in enumerate(nums[index+1:],start=index + 1):
            if num1 + num2 == target:
                print("result", index, j_index)



nums = [2, 7, 11, 15]
target = 17

twoSum(nums,target)