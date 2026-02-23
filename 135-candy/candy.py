class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)

        # Step 1: give 1 candy to each child
        candies = [1] * n

        # Step 2: left to right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Step 3: right to left
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)