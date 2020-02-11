#Alex Harris
#CS160 9am

from math import sqrt

class StatSet:
    def __init__(self):
        self.nums = []

    def addNumber(self, x):
        """
        :param x: the number you wish to add
        :return: the list of numbers
        """
        self.nums.append(x)
        return self.nums

    def mean(self):
        total = 0
        for i in self.nums:
            total += i
        self.average = total / len(self.nums)
        return self.average

    def median(self):
        self.nums.sort()
        size = len(self.nums)
        middle = size // 2
        if size % 2 == 0:
            median = (self.nums[middle] + self.nums[middle - 1]) / 2
        else:
            median = self.nums[middle]
        return median

    def stdDev(self):
        sumDevSq = 0
        for num in self.nums:
            dev = num - self.average
            sumDevSq = sumDevSq + dev * dev
        return sqrt(sumDevSq / (len(self.nums) - 1))

    def count(self):
        count = 0
        for num in self.nums:
            count += 1
        return count

    def min(self):
        self.nums.sort()
        return self.nums[0]

    def max(self):
        self.nums.sort()
        return self.nums[-1]