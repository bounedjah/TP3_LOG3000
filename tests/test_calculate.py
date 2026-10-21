"""Tests de la fonction calculate() du module app (analyse des expressions).

Ces tests vérifient le contrat du parseur : format « a op b », gestion des
espaces et messages d'erreur. Ils passent par calculate(), donc un bogue
dans operators.py peut aussi les faire échouer.
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import calculate  # noqa: E402

class TestCalculateValidExpressions(unittest.TestCase):
    """Expressions bien formées : le résultat numérique doit être correct."""

    def test_each_operator(self):
        """Entrées : une expression par opérateur. Sorties : 9, 3, 18, 2.

        subTest permet de voir dans le rapport chaque opérateur en échec
        au lieu de s'arrêter au premier.
        """

        cases = {"6+3": 9, "6-3": 3, "6*3": 18, "6/3": 2}
        for expr, expected in cases.items():
            with self.subTest(expr=expr):
                self.assertAlmostEqual(calculate(expr), expected)

    def test_spaces_are_ignored(self):
        """Entrée : « 12 + 30 ». Sortie attendue : 42."""

        self.assertAlmostEqual(calculate(" 12 + 30 "), 42)

    def test_decimal_operands(self):
        """Entrée : « 1.5+2.25 ». Sortie attendue : 3.75."""

        self.assertAlmostEqual(calculate("1.5+2.25"), 3.75)

    def test_returns_float(self):
        """Entrée : « 2+3 ». Sortie attendue : un float (les opérandes sont convertis)."""

        self.assertIsInstance(calculate("2+3"), float)

    def test_negative_first_operand(self):
        """Entrée : « -5+3 ». Sortie attendue : -2.

        Cas réel dans l'interface : après 3-5=, l'écran affiche -2.0 et
        l'utilisateur doit pouvoir continuer le calcul à partir de ce résultat.
        """

        self.assertAlmostEqual(calculate("-5+3"), -2)

class TestCalculateInvalidExpressions(unittest.TestCase):
    """Expressions mal formées : une ValueError avec un message clair est attendue."""

    def test_empty_expression(self):
        """Entrée : chaîne vide. Sortie attendue : ValueError « empty expression »."""

        with self.assertRaisesRegex(ValueError, "empty expression"):
            calculate("")

    def test_non_string_input(self):
        """Entrée : 42 (int). Sortie attendue : ValueError."""

        with self.assertRaises(ValueError):
            calculate(42)

    def test_no_operator(self):
        """Entrée : « 123 ». Sortie attendue : ValueError « invalid expression format »."""

        with self.assertRaisesRegex(ValueError, "invalid expression format"):
            calculate("123")

    def test_missing_operand(self):
        """Entrées : opérateur au début ou à la fin. Sortie attendue : ValueError."""

        for expr in ("+3", "3+"):
            with self.subTest(expr=expr):
                with self.assertRaisesRegex(ValueError, "invalid expression format"):
                    calculate(expr)

    def test_two_operators(self):
        """Entrée : « 1+2+3 ». Sortie attendue : ValueError « only one operator is allowed »."""

        with self.assertRaisesRegex(ValueError, "only one operator"):
            calculate("1+2+3")

    def test_non_numeric_operand(self):
        """Entrée : « a+2 ». Sortie attendue : ValueError « operands must be numbers »."""

        with self.assertRaisesRegex(ValueError, "operands must be numbers"):
            calculate("a+2")

    def test_division_by_zero(self):
        """Entrée : « 5/0 ». Sortie attendue : ZeroDivisionError (affichée par la route)."""
        
        with self.assertRaises(ZeroDivisionError):
            calculate("5/0")

if __name__ == "__main__":
    unittest.main()
