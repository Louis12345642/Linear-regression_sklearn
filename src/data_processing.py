import pandas as pd
"""
This class cleans the dataset so that it can be in the regression model 
"""

class CleanData:
    def __init__(self,dataSet):
        self.dataSet = dataSet


    def saveToNewFile(self):
          self.dataSet.to_excel('data/cleaned_house_data.xlsx')

    def returnDataset(self):
          newDataSet = pd.read_excel('data/cleaned_house_data.xlsx')
          return newDataSet

          
          
         
         

