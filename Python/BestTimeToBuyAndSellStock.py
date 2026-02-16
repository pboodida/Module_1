#BestTimeToBuyAndSellStock
def maxProfit(self, prices: List[int]) -> int: #Predefined function
    min_price=float('inf') #determining the min value for min price
    max_profit=0
    for price in prices: #Checking for the min value in the prices list
        if price<min_price:
            min_price=price
        else:
            profit=price-min_price #Checking for the max profit 
            max_profit=max(max_profit,profit)
    return max_profit