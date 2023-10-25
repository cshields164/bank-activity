
import statistics as stats

from code.StockData import StockData


class StockMetrics(StockData):
    def __init__(self, path):
        # call the parent method's constructor
        super(StockMetrics, self).__init__(path)

        # now that we've ran self.load(), we can interact with "self.data" as a
        # list of lists
        self.load()

    def average01(self):
        """pt1
        """
        val = ""
        averages = []
        for row in self.data:
            new_lst = [int(val) for row in val if val != " "]
            new_lst = round(stats.mean(new_lst), 3)
            averages.append(new_lst)


            

        return averages

    def median02(self):
        """pt2
        """
        ...

    def stddev03(self):
        """pt3
        """
        ...

#def calculate_lengths(self):
 #       lengths = []
  #      for row in self.data:
            # TODO: Count the number of non-empty items in each row
            # and append the count to the lengths list
            # also be sure to ignore the date value in this list
 #          new_row = [val for val in row if <cond>]
 #          length = len(row[1:])  # Replace None with appropriate code
 #           lengths.append(length)
  #      return lengths