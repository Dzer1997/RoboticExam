import pandas as pd
import glob
import os
import re

folder_path = "C:\\temp\\"  
csv_files = glob.glob(os.path.join(folder_path, "*.csv"))  

combined_df = []  

for file in csv_files:
    df = pd.read_csv(file, delimiter=';')  
    df.columns = df.columns.str.strip()  

    
    df['Winner_Initials'] = df['Winner'].apply(lambda x: re.search(r'[A-Z]+$', x).group(0) if re.search(r'[A-Z]+$', x) else '')

    
    df['Winner_Name'] = df['Winner'].apply(lambda x: re.sub(r'[A-Z]+$', '', x).strip())

    
    df['Laps'] = pd.to_numeric(df['Laps'], errors='coerce', downcast='integer')  

    
    def convert_time_format(time_str):
       
        if ':' in time_str:
            time_parts = time_str.split(':')
            
            if len(time_parts) == 2:
                time_str = '00:' + time_str  
        try:
            
            time_obj = pd.to_datetime(time_str, format='%H:%M:%S.%f')
            return time_obj.strftime('%H:%M:%S')  
        except Exception as e:
            return None  

    df['Time'] = df['Time'].apply(convert_time_format) 

    
    df.drop(columns=['Winner'], inplace=True)

    
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce', dayfirst=True)  
    df['Year'] = df['Date'].dt.year 

    
    combined_df.append(df)


final_df = pd.concat(combined_df, ignore_index=True)

final_df= final_df.rename(columns={"Grand Prix":'Grand_prix', "Date" : "Race_date", "Time":"Race_time"
                                
})

final_df.to_csv("C:\\temp\\F1Cleaned.csv", index=False)

print("All data saved to 'F1.Cleaned.csv'.")
