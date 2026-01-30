import pandas as pd
import gender_guesser.detector as gender

# --- CONFIGURATION ---
INPUT_FILE = '../01.Data/Sources/authors.csv'
OUTPUT_AUTHORS = '../01.Data/Tables/table_auteurs.csv'
OUTPUT_GENDERS = '../01.Data/Tables/table_genres.csv'

def main():
    print("1. Chargement et préparation...")
    
    # Lecture (astuce du séparateur '|')
    df_raw = pd.read_csv(INPUT_FILE, header=None, names=['raw_line'], sep='|', engine='python')

    # Explode pour avoir 1 ligne = 1 auteur
    authors_series = df_raw['raw_line'].str.split(',').explode().str.strip()
    authors_series = authors_series[authors_series != '']

    # --- CRÉATION DE LA TABLE AUTEURS ---
    print("2. Création de la table Auteurs...")
    
    # Comptage des articles
    df_authors = authors_series.value_counts().reset_index()
    df_authors.columns = ['auteur_complet', 'nb_articles']

    # Séparation Prénom / Nom
    split_names = df_authors['auteur_complet'].str.split(n=1, expand=True)
    df_authors['prenom_raw'] = split_names[0]
    df_authors['nom'] = split_names[1].fillna('')

    # Création de la clé de jointure (minuscule, clean)
    df_authors['prenom_cle'] = df_authors['prenom_raw'].str.lower().str.strip()

    # --- CRÉATION DE LA TABLE GENRES ---
    print("3. Création de la table Genres (avec exemple d'auteur)...")

    # Au lieu de juste prendre les uniques, on groupe par prénom et on prend 
    # le PREMIER 'auteur_complet' qui apparait comme exemple.
    # Cela permet d'avoir une table unique sur 'prenom_cle' tout en ayant le contexte.
    df_genders = df_authors.groupby('prenom_cle')['auteur_complet'].first().reset_index()
    
    # On renomme pour que ce soit clair que c'est juste un exemple
    df_genders.rename(columns={'auteur_complet': 'exemple_auteur_complet'}, inplace=True)

    # Initialisation du détecteur
    d = gender.Detector()

    # Détection du genre
    print("4. Détection du genre...")
    # On utilise .capitalize() pour aider le détecteur (jean -> Jean)
    df_genders['genre_estime'] = df_genders['prenom_cle'].apply(lambda x: d.get_gender(x.capitalize()))

    # --- SAUVEGARDE ---
    print(f"5. Sauvegarde des fichiers...")
    
    # Table Auteurs : Garde ses colonnes propres
    df_authors_out = df_authors[['auteur_complet', 'nom', 'prenom_raw', 'prenom_cle', 'nb_articles']]
    df_authors_out.to_csv(OUTPUT_AUTHORS, index=False)
    
    # Table Genres : Clé + Exemple + Genre
    df_genders.to_csv(OUTPUT_GENDERS, index=False)

    print(f"   -> {OUTPUT_AUTHORS} généré ({len(df_authors_out)} auteurs)")
    print(f"   -> {OUTPUT_GENDERS} généré ({len(df_genders)} prénoms uniques)")
    
    print("\n--- Extrait de la table des genres ---")
    print(df_genders.head())

if __name__ == "__main__":
    main()