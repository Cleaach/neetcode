class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        """
        INEFFICIENT VERSION

        def help(day: int, boughtPrice: int, profit: int, log: str) -> int:
            if day >= n:
                #print(str(profit) + ": " + log)
                return profit
            if boughtPrice != -1: # neetcoin already bought
                sell = help(day + 2, -1, profit + prices[day] - boughtPrice, log + " sell_day_" + str(day))
                notSell = help(day + 1, boughtPrice, profit, log)
                return max(sell, notSell)
            else: # can buy neetcoin
                buy = help(day + 1, prices[day], profit, log + " buy_day_" + str(day))
                notBuy = help(day + 1, -1, profit, log)
                return max(buy, notBuy)
        return help(0, -1, 0, "")
        """

        # EFFICIENT DP
        def help(currDay, holding): # holding = 0 if can buy, 1 if bought already
            if currDay >= n:
                return 0
            if dp[currDay][holding] == -1:
                if holding == 1:
                    sell = prices[currDay] + help(currDay + 2, 0)
                    notSell = help(currDay + 1, 1)
                    dp[currDay][1] = max(sell, notSell)
                else:
                    buy = -prices[currDay] + help(currDay + 1, 1)
                    notBuy = help(currDay + 1, 0)
                    dp[currDay][0] = max(buy, notBuy)
            return dp[currDay][holding]

        # DP
        dp = [[-1, -1] for _ in range(n)]
        
        return help(0, 0)