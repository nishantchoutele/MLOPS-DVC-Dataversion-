import pandas as pd
import os

 #Create a sample dataframe witg column names
data = {'Name': ['Alice','Bob','Charlie'],
    'Age' : [20 ,30 ,45],
    'City': ['New York','Los Angeles','Chicago']
         }  

df = pd.DataFrame(data)       

#adding new row to df for V2
new_row_loc = {'name': 'V2', 'Age': 20, 'City': 'city1'}
df.loc[len(df.index)] = new_row_loc

#adding new row to df for V3
new_row_loc2 = {'name': 'V3', 'Age': 30, 'City': 'city1'}
df.loc[len(df.index)] = new_row_lo2

#ensure that data dictonary exists  at root level
data_dir ='data'
os.makedirs(data_dir,exists_ok = True)

#define the file path 
file_path =  os.path.join(data_dir,'sample_data.csv ')

#Save the dataframe to csv file, including column names
df.to_csv(file_path,index= False)

print(f"CSV file saved to {file_path}")