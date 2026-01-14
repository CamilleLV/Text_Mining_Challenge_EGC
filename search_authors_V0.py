import pandas as pd
import gender_guesser.detector as gender

# --- CONFIGURATION ---
INPUT_FILE = './data/authors.csv'
OUTPUT_FILE = './data/resultats_auteurs_genre.csv'

def main():
    print("1. Chargement et préparation des données...")
    
    # Lecture du fichier "jagged" (lignes de longueurs inégales)
    # L'astuce sep='|' force la lecture de la ligne entière dans une seule colonne
    df_raw = pd.read_csv(INPUT_FILE, header=None, names=['raw_line'], sep='|', engine='python')

    # Séparation des auteurs (explode)
    # On crée une série temporaire pour éclater la liste
    authors_series = df_raw['raw_line'].str.split(',').explode()

    # Nettoyage des espaces (strip)
    authors_clean = authors_series.str.strip()

    # On retire les chaînes vides éventuelles
    authors_clean = authors_clean[authors_clean != '']

    # --- COMPTAGE ---
    print("2. Comptage des publications par auteur...")
    
    # Création du DataFrame final avec comptage
    # reset_index() transforme la série en DataFrame
    df_final = authors_clean.value_counts().reset_index()
    df_final.columns = ['auteur_complet', 'nb_articles']

    # --- EXTRACTION PRÉNOM / NOM ---
    print("3. Extraction des prénoms et noms...")

    # On sépare au premier espace uniquement (n=1). 
    # expand=True crée directement 2 colonnes.
    # Cela gère automatiquement les cas où il n'y a pas de nom de famille (met None/NaN).
    split_names = df_final['auteur_complet'].str.split(n=1, expand=True)
    
    df_final['prenom'] = split_names[0]
    # Si pas de nom de famille, on remplace NaN par une chaine vide
    df_final['nom'] = split_names[1].fillna('')

    # --- DÉTECTION DU GENRE ---
    print("4. Détection du genre...")
    
    d = gender.Detector()
    
    # Application de la détection sur la colonne prénom
    df_final['genre_estime'] = df_final['prenom'].apply(d.get_gender)

    # --- STATISTIQUES ---
    print("\n" + "="*30)
    print("RÉSULTATS DE L'ANALYSE")
    print("="*30)

    # Calculs
    counts = df_final['genre_estime'].value_counts()
    percentages = df_final['genre_estime'].value_counts(normalize=True) * 100

    # Création d'un tableau récapitulatif pour l'affichage
    stats_df = pd.DataFrame({
        'Nombre': counts,
        'Pourcentage (%)': percentages.round(2)
    })
    
    print(stats_df)
    print("="*30)

    # --- SAUVEGARDE ---
    print(f"5. Sauvegarde des résultats dans '{OUTPUT_FILE}'...")
    df_final.to_csv(OUTPUT_FILE, index=False)
    print("Terminé !")

if __name__ == "__main__":
    main()