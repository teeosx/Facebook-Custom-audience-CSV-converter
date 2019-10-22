import pandas as pd
df_data = pd.read_csv("data.csv") #read csv file from mixpanel export
subset = df_data.loc[:,'$properties.$phone']    
export_csv = subset.to_csv (r'export_dataframe.csv', index = None, header=['mobile']) #save csv file to upload into Facebook ads Manager.