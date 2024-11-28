import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Analyse de Dataset avec Streamlit")

file = st.file_uploader("Importer vos données ici (CSV uniquement)", type=["csv"])

if file is not None:
    df = pd.read_csv(file)

    st.subheader("Aperçu des données")
    selected_value = st.slider("Sélectionnez le nombre de lignes à afficher", min_value=5, max_value=100, value=5, step=1)
    st.dataframe(df.head(selected_value))

    st.subheader("Informations générales")
    st.write(f"**Nombre de lignes :** {df.shape[0]}")
    st.write(f"**Nombre de colonnes :** {df.shape[1]}")
    st.write("**Noms des colonnes :**", list(df.columns))

    st.sidebar.header("Analyse des colonnes")
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    if len(numeric_columns) > 1:
        x_axis = st.sidebar.selectbox("Choisir une colonne pour l'axe X", numeric_columns)
        remaining_columns = [col for col in numeric_columns if col != x_axis]
        y_axis = st.sidebar.selectbox("Choisir une colonne pour l'axe Y", remaining_columns, key="y_axis")
        color = st.sidebar.selectbox("Choisir une colonne pour la couleur (facultatif)", [None] + list(df.columns))

        st.subheader(f"Histogramme de la colonne {x_axis}")
        fig_hist = px.histogram(df, x=x_axis, title=f"Histogramme de {x_axis}")
        st.plotly_chart(fig_hist)

        st.subheader(f"Graphique interactif : {x_axis} vs {y_axis}")
        fig = px.scatter(df, x=x_axis, y=y_axis, color=color, title=f"{x_axis} vs {y_axis}")
        st.plotly_chart(fig)
    
    correlation_matrix = df.select_dtypes(include=['float64', 'int64']).corr()

    st.subheader("Matrice de Corrélation")
    fig = px.imshow(correlation_matrix, text_auto=True, color_continuous_scale='Blues', title="Matrice de Corrélation")
    st.plotly_chart(fig)

    st.subheader("Statistiques descriptives")
    st.write(df.describe())

else:
    st.info("Veuillez importer un fichier CSV pour commencer.")
