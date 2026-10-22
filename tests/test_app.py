"""Tests d'intégration de la route Flask « / » et du template index.html.

Le client de test de Flask simule un navigateur : aucune instance du
serveur n'a besoin d'être lancée.
"""

import os
import re
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app

class TestIndexRoute(unittest.TestCase):
    """Vérifie le cycle requête -> calcul -> page HTML de la route « / »."""

    def setUp(self):
        """Crée un client de test Flask neuf avant chaque test.

        TESTING=True fait remonter les exceptions au lieu de les masquer
        derrière une page d'erreur 500.
        """

        app.config["TESTING"] = True
        self.client = app.test_client()

    def display_value(self, response):
        """Extrait la valeur du champ #display d'une réponse HTML.

        Args:
            response: Réponse retournée par le client de test.

        Returns:
            str: Contenu de l'attribut value de l'écran, ou None s'il est absent.
        """

        match = re.search(r'id="display" value="([^"]*)"', response.get_data(as_text=True))
        return match.group(1) if match else None

    def test_get_returns_page_with_empty_display(self):
        """Entrée : GET /. Sortie attendue : statut 200 et écran vide."""

        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.display_value(response), "")

    def test_post_valid_expression_shows_result(self):
        """Entrée : POST display=7*6. Sortie attendue : écran affichant 42.0."""

        response = self.client.post("/", data={"display": "7*6"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.display_value(response), "42.0")

    def test_post_invalid_expression_shows_error(self):
        """Entrée : POST display=1++2. Sortie attendue : statut 200 et message « Error: »."""

        response = self.client.post("/", data={"display": "1++2"})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(self.display_value(response).startswith("Error:"))

    def test_post_division_by_zero_does_not_crash(self):
        """Entrée : POST display=5/0. Sortie attendue : statut 200 et « Error: », pas un 500."""

        response = self.client.post("/", data={"display": "5/0"})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(self.display_value(response).startswith("Error:"))

class TestCalculatorButtons(unittest.TestCase):
    """Vérifie que chaque bouton affiche le symbole qu'il insère dans l'écran."""

    def test_button_labels_match_inserted_value(self):
        """Entrée : page rendue par GET /. Sortie attendue : étiquette == valeur insérée.

        Pour chaque appendToDisplay('x'), le texte visible du bouton doit
        être exactement « x » (sauf '*' -> « × » et '/' -> « ÷ ») ; sinon
        l'utilisateur ne sait pas ce qu'il tape.
        """

        # La multiplication et la division insèrent '*' et '/' mais affichent × et ÷.
        expected_labels = {"*": "×", "/": "÷"}

        app.config["TESTING"] = True
        html = app.test_client().get("/").get_data(as_text=True)
        buttons = re.findall(r"appendToDisplay\('(.)'\)\">([^<]*)</button>", html)
        self.assertEqual(len(buttons), 14, "14 boutons de saisie attendus (10 chiffres, 4 opérateurs)")
        for value, label in buttons:
            with self.subTest(button=value):
                self.assertEqual(label.strip(), expected_labels.get(value, value))

if __name__ == "__main__":
    unittest.main()
