class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0 , 1 # 不是從兩側往內，而是隔壁
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else: # 算出來是負的 或 找到更好的買入點
                l = r # 直接換到右指標，會比一個一個找的效率更好
            r += 1 # 反正不管如何，右指標都會繼續走
        return maxP
