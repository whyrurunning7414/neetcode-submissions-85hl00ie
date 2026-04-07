class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1 

        while l < r :
            now = numbers[l] + numbers[r]
            if now > target :
                r -= 1
            elif now < target :
                l += 1
            else :
                return [l + 1, r + 1] # 第一個值的index是1，題目規定的