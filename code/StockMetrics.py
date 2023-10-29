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
        averages = []
        for row in self.data:
            new_list = []
            print(row)
            for val in row[1:]:
                if val == " " or val == "":               
                    continue
                else:
                    new_list.append(float(val))
                    print(new_list, "<<,")  
            #averages.append(round(sum(new_list)/ len(new_list), 3))
            averages.append(round(stats.mean(new_list), 3))                          
        return averages
            
            


    def median02(self):
        """pt2
        """
        medians = []
        for row in self.data:
            new_list = []
            print(row)
            for val in row[1:]:
                if val == " " or val == "":               
                    continue
                else:
                    new_list.append(float(val))
                    print(new_list, "<<,")  
            medians.append(stats.median(new_list))
        return medians


    def stddev03(self):
        """pt3
        """
        std_dev = []
        for row in self.data:
            new_list = []
            print(row)
            for val in row[1:]:
                if val == " " or val == "":               
                    continue
                else:
                    new_list.append(float(val))
                    print(new_list, "<<,")  
            std_dev.append(round(stats.stdev(new_list), 3))
        return std_dev

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