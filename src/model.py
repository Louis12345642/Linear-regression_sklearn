import numpy as np
from  sklearn import linear_model
class RegressionModel:
    reg = linear_model.LinearRegression()
   
    def fitData(self,x,y):
        self.reg.fit([x],[y])

    def predictPrice(self,x):
        return self.reg.predict([x])
    
    def exportResults(self,dataset,price):
        #create a new colounn for predicted prices
        dataset['price'] = price
        dataset.to_excel('data/predict_dataset.xlsx')


        




