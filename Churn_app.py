
import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error

#############################

st.title("Application Iran_still_Call")
st.subheader("Auteur: KHALID")

st.write("Cette application donne la possibilité de voir la distribution des abonnés"
         "  à travers un histogramme "
         "  en définissant leurs valeurs "
         "  entre 5 et  500"
         )

data = pd.read_csv(r'C:/Users/Electro Depot/Desktop/APPRENTISSAGE/Bases de données/Customer Churn.csv')

##
data = pd.read_csv(r'C:/Users/Electro Depot/Desktop/APPRENTISSAGE/Bases de données/Customer Churn.csv')
data = pd.DataFrame(data, columns=["Frequency of use", "Frequency of SMS", "Customer Value", "Seconds of Use"])
st.title("Pairplot des variables")
# Utiliser Seaborn pour créer un pairplot
pairplot = sns.pairplot(data=data)

# Afficher le pairplot dans Streamlit
st.pyplot(pairplot)

##

data_1 = pd.DataFrame(data, columns=["Customer Value"])
data_2 = pd.DataFrame(data, columns=["Frequency of use", "Frequency of SMS", "Customer Value", "Seconds of Use"])
st.title("Matrice de corrélation des variables")

# Calculer la matrice de corrélation
corr_matrix = data_2.corr()
# Créer une figure Matplotlib
fig, ax = plt.subplots(figsize=(10, 8))
# Créer la heatmap et la placer dans l'axe
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
# Afficher la figure dans Streamlit
st.pyplot(fig)

st.write("Bienvenue chez Iran_Still_Call")

st.write(data_1)

#st.dataframe(data.head())

fig, ax = plt.subplots()
n_bins = st.number_input(
    label="Définir la valeur du client",
    min_value = 5,
    value=250,
    max_value=500

)
ax.hist(data_1,bins=n_bins)
st.pyplot(fig)

# ## Representons notre modèle de classiffication de foret aléatoire :
# Charger les données
data = pd.read_csv(r'C:/Users/Electro Depot/Desktop/APPRENTISSAGE/Bases de données/Customer Churn.csv')

# Features
x = data[['Customer Value', 'Frequency of SMS']]# Target
y = data['Churn']

# Train/test split
seed = 111
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=seed)

# Fonction d'évaluation
def evaluate_model(model):
    train_pred = model.predict(x_train)
    test_pred = model.predict(x_test)
    # Erreur quadratique moyenne
    E_train = mean_squared_error(y_train, train_pred, squared=False)
    E_test = mean_squared_error(y_test, test_pred, squared=False)
    return E_train, E_test

# Construction du modèle
rf = RandomForestClassifier(random_state=seed)
rf.fit(x_train, y_train)

# Interface Streamlit
st.title("Application de prédiction de churn")

# Ajouter des widgets pour les hyperparamètres si nécessaire
# ...

# Faire des prédictions sur de nouvelles données (peut être personnalisé en fonction de vos besoins)
new_data = pd.DataFrame({'Customer Value': [250,500,1000], 'Frequency of SMS': [0.5,2,10]})
 # Nouvelles données à prédire
prediction = rf.predict(new_data)

# Afficher les résultats
st.write("Prédiction de churn :", prediction)