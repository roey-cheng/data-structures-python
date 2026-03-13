class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        best, seq = 0, 0 
        for num in nums:
            if num == 1:
                seq += 1
                best = seq if seq > best else best
            else:
                seq = 0
        return best

print(Solution().findMaxConsecutiveOnes([1,1,0,1,1,1]))