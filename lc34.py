class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        low = 0
        high = len(nums) - 1
        rr = -1
        lr = -1
        while low <= high:
            mid = low + (high - low) / 2
            if nums[mid] == target:
                rr = mid
                lr = mid
                # lh: left high
                # lm: left middle
                # rl: right low
                # rm: right middle
                lh = mid - 1
                rl = mid + 1
                while low <= lh:
                    lm = (lh + low) / 2
                    if nums[lm] == target and ( (lm - 1 > 0 and nums[lm-1] != target) or lm == 0):
                        lr = lm
                        break
                    if nums[lm] == target:
                        lh = lm - 1
                    elif nums[lm] < target:
                        low = lm + 1
                while high >= rl:
                    rm = (rl + high) / 2
                    if nums[rm] == target and ( (rm + 1 < len(nums) and nums[rm+1] != target) or rm == len(nums) - 1):
                        rr = rm
                        break
                    if nums[rm] == target:
                        rl = rm + 1
                    elif nums[rm] > target:
                        high = rm - 1
                return [lr, rr]
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return [-1, -1]

solution = Solution()
print solution.searchRange([0], 0)