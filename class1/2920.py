nums = [int(i) for i in input().split()]
if nums == sorted(nums):
    print('ascending')
elif nums == sorted(nums, reverse=True):
    print('descending')
else:
    print('mixed')