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

Les étapes suivantes doivent être exécutées en ordre dans un terminal (Powershell, Invite de commande Windows ou Terminal Linux/maOS). 

### Étape 1 — S'assurer d'avoir les prérequis

```bash
python --version   # doit afficher Python 3.8 ou plus récent
pip --version
git --version
```

* Sous Linux/macOs, remplacer `python` par `python3` et `pip` par `pip3` si la commande `python` est introuvable.

### Étape 2 — Cloner le dépôt

```bash
git clone https://github.com/bounedjah/TP3_LOG3000.git
cd TP3_LOG3000
```

### Étape 3 — Créer un environnement virtuel

L'environnement virtuel isole les dépendances du projet de celles du système.

```bash
python -m venv venv
```

Un dossier `venv/` est créé à la racine du projet.

### Étape 4 — Activer l'environnement virtuel

| Système | Commande |
|---|---|
| Windows (PowerShell) | `venv\Scripts\Activate.ps1` |
| Windows (Invite de commandes) | `venv\Scripts\activate.bat` |
| Linux/macOS | `source venv/bin/activate` |

Une fois activé, le préfixe `(venv)` apparaît au début de la ligne du terminal.

### Étape 5 — Installer les dépendances

```bash
pip install flask pytest
```

- `flask` : cadriciel de l'application. Nécessaire pour pouvoir l'utiliser.
- `pytest` : cadriciel de test afin de pouvoir exécuter les tests. 


## Utilisation

1. S'assurer que l'environnement virtuel est activé (préfixe `(venv)` dans le terminal).
2. Lancer l'application :
   ```bash
   python app.py
   ```
3. Puis ouvrir un navigateur à l'adresse <http://127.0.0.1:5000>.
4. L'interface de la calculatrice peut être utilisée comme une calculatrice normale simple, en cliquant sur les boutons afin d'effectuer des opérations de la forme : `a <opérateur> b <=>`
4. Pour arrêter le serveur, appuyer sur `Ctrl + C` dans le terminal.

Pour quitter l'environnement virtuel :

```bash
deactivate
```

## Tests

Les tests se trouvent dans le dossier `tests/` et s'exécutent avec `pytest`, installé à l'[Étape 5](#étape-5--installer-les-dépendances).

| Fichier | Contenu |
|---|---|
| `tests/test_operators.py` | Tests unitaires des opérations arithmétiques (`operators.py`) |
| `tests/test_calculate.py` | Tests de l'analyse des expressions (`calculate()` dans `app.py`) |
| `tests/test_app.py` | Tests d'intégration de la route Flask et de l'interface |

Toutes les commandes s'exécutent à la racine du projet, avec l'environnement virtuel activé.

### Exécuter tous les tests

```bash
python -m pytest
```

Le résultat final indique le nombre de tests réussis (`passed`) et les tests échoués (`failed`).

### Exécuter des tests spécifiques

```bash
# Un fichier de tests
python -m pytest tests/test_operators.py

# Une classe de tests
python -m pytest tests/test_operators.py::TestAdd

# Un seul test
python -m pytest tests/test_operators.py::TestAdd::test_add_positive_numbers
```

Ajouter l'option `-v` pour afficher le résultat de chaque test individuellement :

```bash
python -m pytest -v
```

## Flux de contribution

Toute modification passe par une branche et une pull request (PR), avec une issue lorsque c'est pertinent. Aucun changement n'est poussé directement sur `main`.

### 1. Créer une issue (si pertinent)

Les bogues et les tâches à suivre font l'objet d'une issue GitHub qui décrit le problème ou le travail à faire. Le numéro de l'issue sert ensuite à nommer la branche.

Les petites modifications (maintenance, documentation, configuration) peuvent se faire sans issue.

### 2. Créer une branche

Une branche est créée pour chaque tâche, à partir de `main`  :

```bash
git checkout main
git pull
git checkout -b <numéro-issue>/<type>/<tâche>   # avec une issue
git checkout -b <type>/<tâche>                  # sans issue
```

Format du nom de branche :

```
[<numéro-issue>/]<type>/<tâche>
```

- `<numéro-issue>` : numéro de l'issue liée si il y en a une.
- `<type>` : nature du changement.
  - `feat` : nouvelle fonctionnalité
  - `fix` : correction de bogue
  - `test` : ajout ou modification de tests
  - `docs` : documentation
  - `chore` : maintenance 
- `<tâche>` : courte description en minuscules, mots séparés par des tirets.

### 3. Faire des commits

Les messages de commit suivent une convention similaire :

```
<type>(<portée optionnelle>): <description>
```

Exemples : `fix: adjust division to be a real division`, `docs(app): add docstrings and comments`.

### 4. Ouvrir une pull request

```bash
git push -u origin <nom-de-la-branche>
```

Ouvrir ensuite une PR vers `main` sur GitHub, une PR par branche. La description indique ce qui a été changé. Si la branche est liée à une issue, la référencer (par exemple `Closes #4`, ce qui ferme l'issue automatiquement à la fusion).

Avant de fusionner, s'assurer que les tests passent :

```bash
python -m pytest
```


### 5. Revue et fusion

Puisque l'application est plutôt simple,, les PR peuvent être fusionnées sans revue par un autre membre de l'équipe. Une revue est cependant recommandée, surtout pour les changements qui touchent la logique de l'application. 
