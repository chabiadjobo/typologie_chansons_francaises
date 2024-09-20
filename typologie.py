import pandas as pd


# Étape 1 : Préparation des données
data = pd.read_csv('spotify_french_songs.csv')
print(data.info())
print(data.describe())
