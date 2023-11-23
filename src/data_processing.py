import pandas as pd
"""
This class cleans the dataset so that it can be in the regression model 
"""

class CleanData:
    def __init__(self,dataSet):
        self.dataSet = dataSet

    def removeUnwanted(self):
             self.dataSet.drop([
             'date',
            'bedrooms',
            'sqft_living',
            'floors',
            'view',
            'condition',
            'city',
            'street',
            'country',
             'statezip',
            'yr_built',
             'bathrooms',
             'yr_renovated',
             'sqft_basement',
             'sqft_above',
             'waterfront'
             ],axis=1)
            
    def saveToNewFile(self):
          self.dataSet.to_csv('data/cleaned_house_data.csv')

    def returnDataset(self):
          newDataSet = pd.read_csv('data/cleaned_house_data.csv')
          return newDataSet

          
          
         
         

