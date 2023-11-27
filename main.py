import pandas as pd
from sklearn.linear_model import LinearRegression
from src import data_injestion,data_processing,model
import numpy as np

class Main:
    def __init__(self):
        # read the dataset 
        dataSet = pd.read_excel('data/house_price.xlsx')
        areaDataSet = pd.read_excel('data/areas.xlsx')

        #clean the dataset 
        processedData = data_processing.CleanData(dataSet)

        processedData.saveToNewFile()
        #return the new cleaned data set
        newDataSet =processedData.returnDataset()
        # visualise the dateset
        y =newDataSet['price']
        x =newDataSet ['house_size'] 
        showData =  data_injestion.DataIngestion(x,y)
        showData.formatData('House size','house price','graph show the price of house and there size')

        #run the model
        reg = model.RegressionModel()
        #fit the data 
        reg.fitData(x,y)

        #predicted price
    
        price = reg.predictPrice(areaDataSet['house_size'])
        areaDataSet['price'] = price
        print(areaDataSet)
        # areaDataSet.to_excel('data/predict_dataset.xlsx')


# call the main function         
main = Main()





