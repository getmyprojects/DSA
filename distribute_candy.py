"""
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.
"""


def minimum_cost_candy_distribution(ratings):
    candies = [1]*len(ratings)

    # Left to Right
    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1
    # Right to Left
    for i in range(len(ratings)-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            candies[i] = max(candies[i], candies[i+1]+1)

    return candies, sum(candies)


if __name__ == '__main__':
    ratings = [1,3,2]
    print(minimum_cost_candy_distribution(ratings))
    ratings = [1,2,3]
    print(minimum_cost_candy_distribution(ratings))
    ratings = [12,4,3,11,34,34,1,67]
    print(minimum_cost_candy_distribution(ratings))



