import streamlit as st
import pandas as pd

logo = st.sidebar.image('Logo_GHT72.png')
st.sidebar.caption("Thesaurus des interventions pharmaceutiques du GHT72 - Groupe Pharmacie clinique")

data_frame = pd.read_csv('Analyse Pharmacotherapeutique File.csv')
data_frame.set_index('Index', inplace=True)

liste_medoc = [str(medoc) for medoc in set(data_frame.index)]
liste_medoc.sort()
     

option = st.sidebar.selectbox(
     "Choisis un médicament. Petite astuce : Il suffit de cliquer sur la barre de recherche (pas besoin d'effacer) et de taper les première lettres du"
     " médicament (DCI ou Princeps).",
     liste_medoc)

col1, col2 = st.columns(2)

if st.sidebar.button("Ajouter le médicament"):
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
                   txt = st.text_area(f"{data_frame.loc[{option}, 'Situation'][i]}", f"{data_frame.loc[{option}, 'Paragraphe'][i]}")
