import folium
import pandas as pd
from tqdm import tqdm
import os


df = pd.read_csv(f"{os.getcwd()}/Bac_a_sable/pylones-rte.csv",delimiter=";")




dict_ligne = {}
for ind, lat, lon, code in tqdm(df[['Latitude pylône (DD)', 'Longitude pylône (DD)', 'Code ligne']].itertuples(), desc = 'Création des cartes'):
    if code in dict_ligne:
        dict_ligne[code].add_child(folium.RegularPolygonMarker(location=[lat,lon], fill_color='#132b5e', radius=5))
    else :
        dict_ligne[code] =  folium.Map(location=[48.85, 2.34])
        dict_ligne[code].add_child(folium.RegularPolygonMarker(location=[lat,lon], fill_color='#132b5e', radius=5))

 

for cle, val in tqdm(dict_ligne.items(), desc="Sauvegarde des cartes pour chaque ligne"):
    val.save(f"{os.getcwd()}/Bac_a_sable/carte_html/{cle}.html")
    
