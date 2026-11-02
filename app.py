import streamlit as st
from utils import decomposition

st.header("Décomposition en facteurs premiers")
st.write("")
#st.divider()

with st.form("saisie"):
    texte = st.text_input("Entier naturel (au moins 2)", value="90")
    valider = st.form_submit_button("Décomposer")

if valider:
    texte = texte.strip()
    if texte.isdigit() and int(texte) >= 2:
        n = int(texte)
        D = decomposition(n)
        st.write("")
        st.write(f"Décomposition de {n} :")
        st.code(str(D), language=None)
    else:
        st.error("Saisis un entier naturel au moins égal à 2.")