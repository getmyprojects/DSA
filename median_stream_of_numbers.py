"""
    Median in a stream of integers (running integers)
"""

import heapq

# NOTE: Since python doesn't has max heap directly, so we'll multiply numbers
# with -1 to achieve it


class MedianFinder:
    def __init__(self):
        self.small = []     # will be used as max heap
        self.large = []     # will be used as min heap

    def add(self, num):
        heapq.heappush(self.small, -1*num)  # max heap

        # if number in small heap is larger than large heap
        # small[0] => maximum & large[0] => minimum
        if self.small and self.large and (-1*self.small[0] > self.large[0]):
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -1*val)

        # uneven size
        # if difference of length is more than 1
        if len(self.small) > len(self.large)+1:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -1 * val)
        if len(self.large) > len(self.small)+1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def median(self):
        if len(self.small) > len(self.large):
            return -1*self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]

        return (-1*self.small[0] + self.large[0]) / 2


if __name__ == '__main__':
    obj = MedianFinder()
    n = int(input('how many numbers in stream: '))
    for _ in range(n):
        num = int(input('Enter number: '))
        obj.add(num)
        print('Median is: ', obj.median())




