class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = candies[0]
        length = len(candies)

        for i in range(1, length):
            if candies[i] > max_candies:
                max_candies = candies[i]

        result = []

        for i in range(length):
            if candies[i]+extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)

        return result        