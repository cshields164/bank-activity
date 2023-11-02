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
            print(type(row))
            for val in row[1:]:         # for each value starting from index position 1
                if val == " " or val == "":         # if the element in the list is an empty string or a whitespace, continue and skip it. We do not want to add it to the averages list      
                    continue
                else:
                    new_list.append(float(val))     # if the element in the list is not an empty string or whitespace, append it to the new_list list and change the type to a float
                    print(new_list, "<<,")  
            #averages.append(round(sum(new_list)/ len(new_list), 3))
            averages.append(round(stats.mean(new_list), 3))         # append the mean of each row in the new_list list to the averages list and then round it 3 decimal places                 
        return averages
            
            


    def median02(self):
        """pt2
        """
        medians = []
        for row in self.data:
            new_list = []
            print(row)
            for val in row[1:]:         # for each value starting from index position 1
                if val == " " or val == "":               # if the element in the list is an empty string or a whitespace, continue and skip it. We do not want to add it to the medians list 
                    continue
                else:
                    new_list.append(float(val))              # if the element in the list is not an empty string or whitespace, append it to the new_list list and change the type to a float
                    print(new_list, "<<,")  
            medians.append(stats.median(new_list))          # append the median of each row in the new_list list to the medians list
        return medians


    def stddev03(self):
        """pt3
        """
        std_dev = []
        for row in self.data:
            new_list = []
            print(row)
            for val in row[1:]:                   # for each value starting from index position 1
                if val == " " or val == "":      # if the element in the list is an empty string or a whitespace, continue and skip it. We do not want to add it to the std_dev list          
                    continue
                else:
                    new_list.append(float(val))          # if the element in the list is not an empty string or whitespace, append it to the new_list list and change the type to a float
                    print(new_list, "<<,")  
            std_dev.append(round(stats.stdev(new_list), 3))  # append the standard deviation of each row in the new_list list to the std_dev list and then round it 3 decimal places
        return std_dev

