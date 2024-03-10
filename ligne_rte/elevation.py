import json
import requests
import pandas as pd
from tqdm import tqdm
import os



df = pd.read_csv(f"{os.getcwd()}/ligne_rte/pylones-rte-elev.csv",delimiter=";")
liste_res = []
time_to_break = False
for i in tqdm(range(0,len(df),200), desc="Récupération de l'altitude pour chaque pylone"):
    
    str_resquest = 'https://api.open-elevation.com/api/v1/lookup?locations='
    
    debut = i
    if i+200 <len(df) :
         fin = i+200
    else :
        fin = len(df)
        time_to_break = True
    for ind, lat, lon, code in df[['Latitude pylône (DD)', 'Longitude pylône (DD)', 'Code ligne']][i:i+200].itertuples():
        str_resquest = str_resquest + f"{lat},{lon}|"
        
    str_resquest=str_resquest[:-1] # On retire juste le carctère | du dernier élement du string

    r = requests.get(str_resquest)
    try :
        json_res = json.loads(r.text)
        liste_res += json_res["results"]
    except:
        r = requests.get(str_resquest)
        json_res = json.loads(r.text)
        liste_res += json_res["results"]

    if time_to_break:
         
         break
        


liste_elev = [l_elev["elevation"] for l_elev in liste_res]

elevation = liste_elev 

df["elevation"]=elevation
df.to_csv(f"{os.getcwd()}/ligne_rte/pylone_avec_elevation.csv",index=False)