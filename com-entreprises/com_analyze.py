import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Définir un style pour les graphiques
sns.set_theme(style="whitegrid")

def plot_entreprises_par_province(df):
    plt.figure(figsize=(16, 8))
    provinces = df['SiegeSocial'].str.title().value_counts().head(10)
    sns.barplot(x=provinces.values, y=provinces.index, palette="coolwarm_r")
    plt.title("Distribution des entreprises par siège social (Top 10)", fontsize=18, fontweight="bold", pad=20)
    plt.xlabel("Nombre d'entreprises", fontsize=14)
    plt.ylabel("Siège Social", fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.annotate("Source : Youssouf SAGAF", xy=(provinces.values.max() / 2, len(provinces.index) / 2), 
                 fontsize=10, ha="center", rotation=30, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_capital_social_per_secteur(df):
    plt.figure(figsize=(16, 8))
    sns.boxplot(x='Capital social (KMF)', y='Secteur d\'activités', data=df, showfliers=False, 
            order=df.groupby('Secteur d\'activités')['Capital social (KMF)'].median().sort_values(ascending=False).index[:2], 
            palette='coolwarm_r', width=0.6+len(max(df['Secteur d\'activités'], key=len))/100)

    plt.title("Distribution du capital social par secteur d'activité (Top 10)", fontsize=16, fontweight="bold", pad=10)
    plt.xlabel("Capital social (KMF)", fontsize=12)
    plt.ylabel("Secteur d'activités", fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.annotate("Source : Youssouf SAGAF", xy=(df['Capital social (KMF)'].max() / 2, len(df.groupby('Secteur d\'activités').count().index) / 2), 
                 fontsize=12, ha="center", rotation=30, alpha=0.3)
    plt.tight_layout()
    plt.show()

def plot_secteurs_activites(df):
    plt.figure(figsize=(16, 8))
    secteurs = df['Secteur d\'activités'].value_counts().head(10)
    sns.barplot(x=secteurs.values, y=secteurs.index, palette="coolwarm_r")
    plt.title("Top 10 des secteurs d'activités", fontsize=18, fontweight="bold", pad=20)
    plt.xlabel("Nombre d'entreprises", fontsize=14)
    plt.ylabel("Secteur d'activités", fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.annotate("Source : Youssouf SAGAF", xy=(secteurs.values.max() / 2, len(secteurs.index) / 2), 
                 fontsize=10, ha="center", rotation=30, alpha=0.3)
    plt.tight_layout()
    plt.show()

def plot_forme_juridique(df):
    plt.figure(figsize=(16, 8))
    formes_juridiques = df['Forme Juridique'].value_counts()
    sns.barplot(x=formes_juridiques.values, y=formes_juridiques.index, palette="Spectral")
    plt.title("Nombre d'entreprises par forme juridique", fontsize=18, fontweight="bold", pad=20)
    plt.xlabel("Nombre d'entreprises", fontsize=14)
    plt.ylabel("Forme juridique", fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.annotate("Source : Youssouf SAGAF", xy=(formes_juridiques.values.max() / 2, len(formes_juridiques.index) / 2), 
                 fontsize=10, ha="center", rotation=30, alpha=0.3)
    plt.tight_layout()
    plt.show()

def plot_capital_social_distribution(df):
    plt.figure(figsize=(16, 8))
    sns.histplot(data=df, x='Capital social (KMF)', kde=True, bins=20, color='purple', edgecolor='white')
    plt.title("Distribution du capital social", fontsize=18, fontweight="bold", pad=20)
    plt.xlabel("Capital social (KMF)", fontsize=14)
    plt.ylabel("Fréquence", fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.annotate("Source : Youssouf SAGAF", xy=(df['Capital social (KMF)'].max() / 2, plt.gca().get_ylim()[1] / 2), 
                 fontsize=10, ha="center", rotation=30, alpha=0.3)
    plt.tight_layout()
    plt.show()

def plot_capital_social_per_secteur(df):
    plt.figure(figsize=(12, 8))
    sns.boxplot(x='Capital social (KMF)', y='Secteur d\'activités', data=df, showfliers=False, order=df.groupby('Secteur d\'activités')['Capital social (KMF)'].median().sort_values(ascending=False).index[:10], palette='coolwarm_r')
    plt.title("Distribution du capital social par secteur d'activité (Top 10)", fontsize=18, fontweight="bold", pad=15)
    plt.xlabel("Capital social (KMF)", fontsize=14)
    plt.ylabel("Secteur d'activités", fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.annotate("Source : Youssouf SAGAF", xy=(df['Capital social (KMF)'].max() / 2, len(df.groupby('Secteur d\'activités').count().index) / 2), 
                 fontsize=10, ha="center", rotation=30, alpha=0.3)
    plt.tight_layout()
    plt.show()



def replace_forme_juridique(df):
    formes_juridiques_map = {
        'SARLU': 'SARL',
        'SARLu': 'SARL',
        'Sarl': 'SARL',
        ' SARL': 'SARL',
        'PP': 'PP',
        'pp': 'PP',
        'SCOOPS': 'SCOOPS',
        'SCOOP-CA': 'SCOOP-CA',
        'SA': 'SA',
        'SAS': 'SAS'
    }
    df['Forme Juridique'] = df['Forme Juridique'].replace(formes_juridiques_map)
    return df

def remove_unnamed_columns(df):
    colonnes_inutiles = ['Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14']
    df.drop(columns=colonnes_inutiles, inplace=True)
    return df

def drop_missing_values(df):
    df.dropna(subset=['Forme Juridique', 'Secteur d\'activités', 'Gerant', 'CHR-NRCCM'], inplace=True)
    return df

def clean_capital_social(df):
    df['Capital social (KMF)'].fillna(0, inplace=True)
    df['Capital social (KMF)'] = pd.to_numeric(df['Capital social (KMF)'], errors='coerce')
    df['Capital social (KMF)'].fillna(0, inplace=True)
    return df

def unify_text_case(df):
    df['Forme Juridique'] = df['Forme Juridique'].str.upper().str.strip()
    df['Secteur d\'activités'] = df['Secteur d\'activités'].str.capitalize().str.strip()
    return df

def identify_outliers(df):
    Q1 = df['Capital social (KMF)'].quantile(0.25)
    Q3 = df['Capital social (KMF)'].quantile(0.75)
    IQR = Q3 - Q1
    seuil_bas = Q1 - 1.5 * IQR
    seuil_haut = Q3 + 1.5 * IQR
    outliers = df[(df['Capital social (KMF)'] < seuil_bas) | (df['Capital social (KMF)'] > seuil_haut)]
    return outliers

def nettoyage(df):
    df = replace_forme_juridique(df)
    df = remove_unnamed_columns(df)
    df = drop_missing_values(df)
    df = clean_capital_social(df)
    df = unify_text_case(df)
    outliers = identify_outliers(df)
    print("Outliers dans la colonne 'Capital social (KMF)':")
    print(outliers)
    return df

def read_excel_file(fichier_excel):
    df = pd.read_excel(fichier_excel, engine='openpyxl')
    return df

def display_general_information(df):
    print("\nInformations générales après nettoyage:")
    print(df.info())
    print("\nStatistiques descriptives:")
    print(df.describe())
    print("\nNombre d'entreprises par secteur d'activité:")
    print(df['Secteur d\'activités'].value_counts())
    print("\nNombre d'entreprises par forme juridique:")
    print(df['Forme Juridique'].value_counts())
    return

def main():
    # Remplacez 'chemin_du_fichier.xlsx' par le chemin réel de votre fichier Excel
    fichier_excel = 'entreprises-2022.xlsx'
    df = read_excel_file(fichier_excel)
    
    print("Noms de colonnes dans le DataFrame:")
    print(df.columns)
    print("Les 5 premières lignes du fichier:")
    print(df.head())
    
    df = nettoyage(df)
    display_general_information(df)

    # Appeler les fonctions de tracé pour visualiser les informations importantes
    plot_secteurs_activites(df)
    plot_forme_juridique(df)
    plot_capital_social_distribution(df)
    #plot_capital_social_per_secteur(df)
    plot_entreprises_par_province(df)
    

if __name__ == '__main__':
    main()
