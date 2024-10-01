import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

def analyser_correlation(df, var1, var2):
    """
    Fonction universelle pour analyser la corrélation entre deux variables dans un DataFrame.
    df : DataFrame contenant les données
    var1 : première variable (colonne du DataFrame)
    var2 : deuxième variable (colonne du DataFrame)
    """

    # 1. Test de normalité sur les deux variables
    def test_normality(column):
        stat, p = stats.shapiro(df[column].dropna())
        return p > 0.05

    normal_var1 = test_normality(var1)
    normal_var2 = test_normality(var2)

    print(f"\nTest de normalité pour '{var1}' : {'Normale' if normal_var1 else 'Non Normale'}")
    print(f"Test de normalité pour '{var2}' : {'Normale' if normal_var2 else 'Non Normale'}")

    # 2. Visualisation de la relation entre var1 et var2
    def visualiser_relation(var1, var2):
        sns.scatterplot(x=df[var1], y=df[var2])
        plt.title(f"Relation entre {var1} et {var2}")
        plt.show()

        print("\nQuel type de relation voyez-vous entre '{}' et '{}' ?".format(var1, var2))
        print("1 : Linéaire")
        print("2 : Quadratique")
        print("3 : Non Linéaire ou Autre")
        relation_type = input("Choisissez une option (1, 2 ou 3) : ")
        return relation_type

    relation_type = visualiser_relation(var1, var2)

    # 3. Choisir la méthode de corrélation en fonction des résultats des tests et du type de relation
    def choisir_correlation(normal_var1, normal_var2, relation_type):
        if normal_var1 and normal_var2 and relation_type == '1':
            return "Pearson"
        elif relation_type == '1':  # Linéaire mais pas normal
            return "Spearman"
        elif relation_type == '2':
            return "Quadratique"
        elif relation_type == '3':
            return "Hoeffding"
        else:
            return "Kendall"

    correlation_method = choisir_correlation(normal_var1, normal_var2, relation_type)
    print(f"\nMéthode de corrélation suggérée : {correlation_method}")

    # 4. Calculer la corrélation en fonction du choix
    def calculer_correlation(method):
        if method == "Pearson":
            return df[var1].corr(df[var2], method='pearson')
        elif method == "Spearman":
            return df[var1].corr(df[var2], method='spearman')
        elif method == "Kendall":
            return df[var1].corr(df[var2], method='kendall')
        elif method == "Quadratique":
            # Exemple simplifié pour quadratique (ajustement d'une régression quadratique)
            df['var1_squared'] = df[var1]**2
            return stats.linregress(df['var1_squared'], df[var2]).rvalue
        elif method == "Hoeffding":
            from scipy.stats import hoeffding
            return hoeffding(df[var1], df[var2])[0]

    # Calculer la corrélation
    correlation_value = calculer_correlation(correlation_method)
    print(f"Valeur de corrélation ({correlation_method}) : {correlation_value}")

    # 5. Visualisation des résultats sous forme de heatmap (automatique)
    def heatmap_corr():
        corr_matrix = df[[var1, var2]].corr(method=correlation_method)
        plt.figure(figsize=(5, 4))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
        plt.title(f"Matrice de corrélation ({correlation_method}) entre {var1} et {var2}")
        plt.show()

    heatmap_corr()

# Exemple d'utilisation
df = pd.read_csv('base_excel/data_scaled_zscore.csv')
analyser_correlation(df, 'energy', 'danceability')
