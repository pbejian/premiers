import streamlit as st
import streamlit.components.v1 as components
from utils import decomposition


def ecriture_latex(n, D):
    """Construit la formule LaTeX : 90 = 2 \\times 3^{2} \\times 5"""
    termes = []
    for (p, a) in D:
        if a == 1:
            termes.append(str(p))
        else:
            termes.append(f"{p}^{{{a}}}")
    return f"{n} = " + r" \times ".join(termes)


def afficher_mathjax(formule):
    """Affiche une formule LaTeX avec MathJax, chargé depuis un CDN distant."""
    html = rf"""
    <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
    <div style="font-size: 1.5em; overflow-x: auto;">
        \[ {formule} \]
    </div>
    """
    components.html(html, height=100)


st.header("Décomposition en facteurs premiers")
st.write("")

with st.form("saisie"):
    texte = st.text_input("Entier naturel (au moins 2)", value="90")
    valider = st.form_submit_button("Décomposer")

if valider:
    texte = texte.strip()
    if texte.isdigit() and int(texte) >= 2:
        n = int(texte)
        D = decomposition(n)
        afficher_mathjax(ecriture_latex(n, D))
    else:
        st.error("Saisis un entier naturel au moins égal à 2.")
