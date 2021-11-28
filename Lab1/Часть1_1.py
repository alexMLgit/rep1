import pandas as pd
import numpy as np

if __name__ == '__main__':
    counter=0
    data_frame1 = pd.read_json("C:\\Microsoft VS Code\\Prodgect\\Лазаревский\\sales.json")
    data_frame2 = pd.DataFrame(columns=['item', 'country', 'year', 'sales'])

    for item in range(0, len(data_frame1['item'].keys())):
        for country in data_frame1['sales_by_country'][item].keys():
            for year  in data_frame1['sales_by_country'][item].get(f'{country}').keys():
                #print(f"{data_frame1['item'][item]},{country},{year},{data_frame1['sales_by_country'][item].get(f'{country}').get(f'{year}')}")
                data_frame2.loc[counter] = [data_frame1['item'][item],country,year,data_frame1['sales_by_country'][item].get(f'{country}').get(f'{year}')]
                counter+=1      
    data_frame2.to_csv('CSV_data_frame2.csv',sep=',',columns=['item', 'country', 'year', 'sales'])
    print(data_frame2)