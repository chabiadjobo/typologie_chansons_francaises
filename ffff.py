import pandas as pd
data = pd.read_csv('base_excel/songs_with_release_year.csv')
data = data.drop(columns='lyrics', errors='ignore')
data.to_csv('base_excel/data_typologie.csv', index=False)