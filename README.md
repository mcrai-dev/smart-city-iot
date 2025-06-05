# Smart City IoT

**Smart City IoT** est une plateforme moderne de visualisation et d’analyse des données environnementales urbaines (CO₂, température, humidité, AQI, etc.) pour Madagascar. Elle s’appuie sur des capteurs IoT et propose une interface cartographique interactive, des filtres dynamiques, des alertes, et des modules d’intelligence artificielle pour la prédiction en temps réel.

---

##  Fonctionnalités

- **Carte interactive Leaflet** : Visualisation des points de mesure sur la carte de Madagascar.
- **Sidebar dynamique** : Filtres par zone et niveau d’alerte, détails enrichis sur chaque point.
- **Changement de fond de carte** : Vue sombre, claire et satellite.
- **Légende moderne** : Explications visuelles des codes couleurs et symboles.
- **Loader animé & gestion des erreurs**.
- **Responsive** : Adapté desktop/mobile, sidebar rétractable.
- **Backend Python/Flask** : Sert les données depuis un CSV, prêt pour l’extension IA.
- **Prédiction IA (optionnel)** : Intégration possible de modèles pour la détection d’anomalies et la prédiction d’alertes.

---

##  Structure du projet

```
smart-city-iot/
├── backend/
│   └── app.py           # API Flask pour servir les données et les prédictions
├── data/
│   └── co2.csv          # Fichier de données environnementales (modifiable)
├── frontend/
│   └── index.html       # Interface utilisateur moderne (Leaflet, JS, CSS)
├── db/
│   └── init.sql         # (Optionnel) Script SQL pour usage futur en base
└── README.md
```

---

## ⚡ Installation & Lancement

### 1. Prérequis

- Python 3.x
- pip (`pip install flask pandas flask-cors`)
- (Optionnel pour IA : `scikit-learn`, `joblib`, etc.)

### 2. Lancer le backend Flask

```bash
cd backend
python3 app.py
```

Le backend lit automatiquement `../data/co2.csv` et expose les données sur `/api/points`.

### 3. Lancer le frontend

Ouvre `frontend/index.html` dans ton navigateur.
- La carte s’affiche avec tous les points et filtres dynamiques.
- Les données sont chargées en direct depuis le backend.

---

##  Personnalisation des données

Modifie le fichier `data/co2.csv` pour ajouter ou éditer des points (quartiers, villes, types de zones, valeurs de CO₂, etc.).
- Recharge la page pour voir les changements en temps réel.

---

##  Intelligence Artificielle (optionnel)

Le projet est prêt à accueillir des modules IA pour :
- Prédiction d’alertes en temps réel
- Détection d’anomalies
- Prévisions de pollution

Voir le dossier `backend/` pour intégrer un modèle (ex : RandomForest, IsolationForest, Prophet…).

---

## Aperçu

![screenshot](/screenshoot.png) 
---

##  Licence

Projet open-source sous licence MIT.

---

## 👤 Auteur

Mcrai LAYDAM  
Contact : [laydamcrai@gmail.com](mailto:laydamcrai@gmail.com)

---

## 🌍  Madagascar et l’innovation urbaine!
# smart-city-iot
