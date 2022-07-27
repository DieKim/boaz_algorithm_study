#n = int(input())
#nums = [int(input()) for i in range(n)]

import sys
n = int(sys.stdin.readline())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))

mean = round(sum(nums)/n)
median = sorted(nums)[int((n+1)/2)-1]
range_ = max(nums)-min(nums)

dic = {}
for i in sorted(nums):
    try:
        dic[i] += 1
    except:
        dic[i] = 1

dic_sorted = sorted(dic.items(),
                    key=lambda item: item[1],
                    reverse=True)

if len(nums)==1:
    mode = nums[0]
elif dic_sorted[0][1]==dic_sorted[1][1]:
    mode = dic_sorted[1][0]
else:
    mode = dic_sorted[0][0]

print(mean, median, mode, range_, sep='\n')

#input() -> 시간초과 오류
#sys.stdin.readline() -> 성공, 단 스파이더에서 안돌아감