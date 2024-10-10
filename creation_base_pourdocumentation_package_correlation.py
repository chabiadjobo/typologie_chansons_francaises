import pandas as pd
import numpy as np

# Charger la base de données dans un DataFrame pandas (adapte le chemin si nécessaire)
df = pd.read_csv('base_excel/data_scaled_zscore.csv')

# Liste des variables (exclut 'ID' qui est déjà inclus)
variables = ['danceability', 'energy', 'mode', 'acousticness', 'valence', 'tempo', 
             'release_year', 'key_sin', 'key_cos', 'loudness_winsorized',
             'speechiness_log', 'instrumentalness_log', 'liveness_log', 'duration_log']

# Sélectionner aléatoirement 5 variables
selected_variables = np.random.choice(variables, size=5, replace=False)

# Ajouter 'ID' à la liste des variables sélectionnées
selected_variables = ['id'] + list(selected_variables)

# Sélectionner aléatoirement 400 individus
sampled_df = df[selected_variables].sample(n=400, random_state=42)

sampled_df.reset_index(drop=True, inplace=True)
sampled_df.to_csv('example.csv', index=False)
