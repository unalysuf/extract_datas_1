import pandas as pd
from pathlib import Path

#in this code base I will try to read all the csv files under same path and display them on terminal window

#create a path object
folder_path = Path(r"C:\Users\TCYUSUNAL\Desktop\Personal\Kariyer\Python\ETL_Projects\1")

#list which will store DataFrames
all_dfs = []

#extract layer
def extract_data(file_path):
    #glob method returns iterator of objects
    for file_path in folder_path.glob("*.csv"):
        df = pd.read_csv(file_path)
        all_dfs.append(df)
    #reset index number after combaning all DataFrames
    final_df = pd.concat(all_dfs, ignore_index = True)
    return final_df
        
print(extract_data(folder_path))




