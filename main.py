import pandas as pd
from src import data_injestion,data_processing


# read the dataset 
dataSet = pd.read_csv('data/house_price_data.csv')

#clean the dataset 
processedData = data_processing.CleanData(dataSet)
processedData.removeUnwanted()
processedData.saveToNewFile()
#return the new cleaned data set
newDataSet =processedData.returnDataset()
 
# visualise the dateset
y = newDataSet['price']
x =newDataSet ['sqft_lot'] 
showData =  data_injestion.DataIngestion(x,y)
showData.formatData('House size','house price','graph show the price of house and there size')
