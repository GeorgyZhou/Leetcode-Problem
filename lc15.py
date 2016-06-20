class Solution(object):
    def threeSum(self, nums):
        sum2 = {}
        ret = []
        for i in range(len(nums)-1):
            for j in range(i+1 , len(nums), 1):
                key = nums[i] + nums[j]
                if key in sum2.keys():
                    sum2[key].append([i,j])
                else:
                    sum2[key] = [i,j]

        for i in range(len(nums)):
            if -nums[i] in sum2.keys() and i not in sum2[-nums[i]]:
                triplet = []
                triplet.append([nums[sum2[-nums[i]][1]], nums[sum2[-nums[i]][0]], nums[i]])
                triplet.sort(reverse=False)
                ret.append(triplet)
        return ret
