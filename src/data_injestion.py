
import matplotlib.pyplot as plt


"""
This class  accepts the data and display  the values the screen
inform of a graph for reading the data properly
"""

class DataIngestion:
    def __init__(self,x,y):
        self.x =x
        self.y =y

    def formatData(self,xlabel,ylabel,title):
        #plot the data on the graph
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.legend
        plt.scatter(self.x,self.y)
        plt.show()



    
