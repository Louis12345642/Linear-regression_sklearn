import pandas as pd
from src import data_injestion,data_processing

class Main:
    def __init__(self):
        # read the dataset 
        dataSet = pd.read_excel('house_price.xlsx')

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
        

# call the main function         
main = Main()





