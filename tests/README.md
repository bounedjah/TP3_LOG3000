# tests/

## Rôle
Regroupe les tests automatisés du projet. Chaque fichier cible une
unité précise du code : les opérations arithmétiques, le moteur
d'évaluation et les routes Flask.

## Contenu

**Présentement :**
- `test_operators.py` : Tests unitaires des fonctions de
  `operators.py`. 
    - Addition
    - Soustraction
    - Multiplication
    - Division
    - Cas limites comme la division par zéro
- `test_calculate.py` : Tests de la logique d'évaluation d'une
  expression complète. 
  - Priorité des opérateurs
  - Parenthèses
  - Entrées invalides
- `test_app.py` : Tests d'intégration sur l'application Flask.
  - Codes de réponse HTTP
  - Rendu du gabarit
  - Soumission d'une expression via POST
  - Affichage du résultat

## Exécution
Depuis la racine du projet :

```bash
python -m pytest tests/
```

Pour un fichier précis :

```bash
python -m pytest tests/test_operators.py -v
```

## Dépendances et hypothèses
- `pytest` installé (voir le README principal pour l'installation).
- Les tests s'exécutent depuis la racine du dépôt pour que les
  imports (`from app import ...`, `from operators import ...`)
  fonctionnent.
- Les tests Flask utilisent le client de test intégré
  (`app.test_client()`) ; aucune instance du serveur n'a besoin
  d'être lancée en parallèle.
- Convention de nommage : fichiers `test_*.py`, fonctions
  `test_*`, pour la découverte automatique par pytest.