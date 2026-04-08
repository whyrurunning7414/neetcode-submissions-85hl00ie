class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums) : # 回傳索引值(i)和數值(a)
            if i > 0 and a == nums[i - 1] : # 如果a跟他前位的數值一樣
                continue # 直接找下一組 (i , a)
                
            l, r = i + 1, len(nums) - 1 # 左右指標
            while l < r : # 左指標小於右指標作為分界，交會就代表找完這組了，跳回上面的for loop
                all = a + nums[l] + nums[r] 
                if all > 0 :
                    r -= 1
                elif all < 0 :
                    l += 1
                else :
                    res.append([a, nums[l], nums[r]])
                    l += 1 # 成功找到一組，找這個a還有沒有其他組可能的答案，所以移動左指標
                    while nums[l] == nums[l -1] and l < r : # 如果移動左指標下個數結果又跟前位一樣
                        l += 1 # 再移
        return res
                
