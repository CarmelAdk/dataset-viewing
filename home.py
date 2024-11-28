import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Analyse de Dataset avec Streamlit")

file = st.file_uploader("Importer vos données ici (CSV uniquement)", type=["csv"])

if file is not None:
    df = pd.read_csv(file)

    st.subheader("Aperçu des données")
    st.dataframe(df.head())

    st.subheader("Informations générales")
    st.write(f"**Nombre de lignes :** {df.shape[0]}")
    st.write(f"**Nombre de colonnes :** {df.shape[1]}")
    st.write("**Noms des colonnes :**", list(df.columns))

    st.sidebar.header("Analyse des colonnes")
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    if len(numeric_columns) > 0:
        x_axis = st.sidebar.selectbox("Choisir une colonne pour l'axe X", numeric_columns)
        y_axis = st.sidebar.selectbox("Choisir une colonne pour l'axe Y", numeric_columns)
        color = st.sidebar.selectbox("Choisir une colonne pour la couleur (facultatif)", [None] + list(df.columns))

        st.subheader(f"Graphique interactif : {x_axis} vs {y_axis}")
        fig = px.scatter(df, x=x_axis, y=y_axis, color=color, title=f"{x_axis} vs {y_axis}")
        st.plotly_chart(fig)

    st.subheader("Statistiques descriptives")
    st.write(df.describe())

else:
    st.info("Veuillez importer un fichier CSV pour commencer.")
