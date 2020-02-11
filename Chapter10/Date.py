from __future__ import annotations

class Date:

    def __init__(self, month, day, year):
        """
        Constructor method
        :param month:
        :param day:
        :param year:
        """
        self.month = month
        self.day = day
        self.year = year

    def __str__(self):
        """
        Should return April 15, 1707 when 4, 15, 1707 is passed
        to the constructor
        :return:
        """
        monthList = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        return f"{monthList[self.month - 1]} {self.day}, {self.year}"

    def getDay(self):
        """
        Should return 15 when 4, 15, 1707 is passed to thee constructor
        :return:
        """
        return self.day

    def getMonth(self):
        """
        Should return 4 when 4, 15, 1707 is passed to the constructor
        :return:
        """
        return self.month

    def getYear(self):
        """
        Should return 1707 when 4, 15, 1707 is passed to the constructor
        :return:
        """
        return self.year

    def yearsLaterThanDate(self, otherDate) -> int:
        """
        Determines whole number of years date is later than
        another instance of the Date class called otherDate
        :param otherDate:
        :return:
        """
        gap = self.year - otherDate.getYear()

        return gap

    def isLessThanDate(self, otherDate):
        """
        Returns True if date occurs prior to another instance of
        the Date class called otherDate
        :param otherDate:
        :return:
        """
        pass

    def clone(self) -> Date:
        """
        Returns a new instance of the Date class identical
        to date.
        :return:
        """
        pass

    def nextDay(self):
        """
        Mutates date by finding the next date
        :return:
        """
        pass

    def addNumberOfDays(self, daysToAdd):
        """
        Returns a new instance of the Date class daysToAdd
        after date.
        :param daysToAdd:
        :return:
        """
        pass