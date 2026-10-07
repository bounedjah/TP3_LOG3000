# Calculatrice Flask

**Équipe :** 01
**Cours :** LOG3000

## Objectif

Ce projet est une application web qui consiste en une calculatrice simple développée avec Flask. Elle permet les opérations suivantes :  
`+`, `-`, `*`, `/`

L'objectif de ce TP est de tester l'application afin de découvrir et de corriger les bogues à l'aide d'un pipeline entièrement documenté. 

## Structure du projet

```
.
├── app.py              # Application Flask et logique de calcul
├── operators.py        # Fonctions des opérations arithmétiques
├── static/style.css    # Feuille de style
└── templates/index.html # Interface de la calculatrice
```

## Prérequis

- Python 3.8 ou plus récent
- pip
- Git

## Installation

1. Cloner le dépôt :
   ```bash
   git clone <url-du-depot>
   cd TP3_LOG3000
   ```

2. (Optionnel) Créer et activer un environnement virtuel :
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```

3. Installer les dépendances :
   ```bash
   pip install flask
   ```

## Utilisation

Lancer l'application :

```bash
python app.py
```

Puis ouvrir un navigateur à l'adresse <http://127.0.0.1:5000>.
