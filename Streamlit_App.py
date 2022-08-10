import streamlit as st
import pandas as pd

st.set_page_config(
   page_title="GHT72",
   page_icon="💊",
   layout="wide"
)
logo = st.sidebar.image('Logo_GHT72.png')
st.sidebar.caption("Thesaurus des interventions pharmaceutiques du GHT72 - Groupe Pharmacie clinique")

data_frame = pd.read_csv('Tableau IP GHT72 - App source.csv')
data_frame.set_index('Index', inplace=True)

liste_medoc = [str(medoc) for medoc in set(data_frame.index)]
liste_medoc.sort()
     

option = st.sidebar.selectbox(
     "Choisis un médicament. Petite astuce : Il suffit de cliquer sur la barre de recherche (pas besoin d'effacer) et de taper les première lettres du"
     " médicament (DCI ou Princeps).",
     liste_medoc)

col1, col2 = st.columns([1, 3])

col1.subheader('Liste des médicaments')
col1.write(option)
with col2 :
    st.subheader('Intervention pharmaceutiques - à adapter selon contexte')
    with st.expander("Interventions"):                                  
         compteur = 0
         for i in data_frame.index: 
             if i == option:
                 compteur += 1

         for i in range(compteur):
             txt = st.text_area(f"{data_frame.loc[{option}, 'Situation'][i]}", f"{data_frame.loc[{option}, 'Paragraphe'][i]}", key = option)
