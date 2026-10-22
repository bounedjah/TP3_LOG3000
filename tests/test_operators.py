"""Tests unitaires des opérations arithmétiques du module operators.

Chaque fonction est testée isolément, sans passer par Flask ni par le
parseur, afin qu'un échec pointe directement vers l'opération fautive.
"""

import os
import sys
import unittest

# Rend la racine du projet importable quand les tests sont lancés depuis
# n'importe quel dossier (operators.py n'est pas un paquet installé).
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from operators import add, subtract, multiply, divide  # noqa: E402

class TestAdd(unittest.TestCase):
    """Vérifie que add(a, b) retourne a + b."""

    def test_add_positive_numbers(self):
        """Entrées : 2 et 3. Sortie attendue : 5."""

        self.assertEqual(add(2, 3), 5)

    def test_add_with_negative_and_decimal(self):
        """Entrées : -1.5 et 4. Sortie attendue : 2.5 (couvre signes et décimales)."""

        self.assertAlmostEqual(add(-1.5, 4), 2.5)

class TestSubtract(unittest.TestCase):
    """Vérifie que subtract(a, b) retourne a - b, dans cet ordre."""

    def test_subtract_order_matters(self):
        """Entrées : 10 et 4. Sortie attendue : 6.

        L'ordre des opérandes est volontairement asymétrique : un résultat
        de -6 indiquerait que les opérandes sont inversés.
        """

        self.assertEqual(subtract(10, 4), 6)

    def test_subtract_to_negative(self):
        """Entrées : 3 et 5. Sortie attendue : -2."""

        self.assertEqual(subtract(3, 5), -2)

class TestMultiply(unittest.TestCase):
    """Vérifie que multiply(a, b) retourne le produit a * b."""

    def test_multiply_basic(self):
        """Entrées : 3 et 4. Sortie attendue : 12.

        Valeurs choisies pour distinguer le produit (12) de la puissance (81).
        Éviter 2 * 2, qui donne 4 dans les deux cas.
        """

        self.assertEqual(multiply(3, 4), 12)

    def test_multiply_by_zero(self):
        """Entrées : 5 et 0. Sortie attendue : 0 (une puissance donnerait 1)."""

        self.assertEqual(multiply(5, 0), 0)

class TestDivide(unittest.TestCase):
    """Vérifie que divide(a, b) retourne le quotient réel a / b."""

    def test_divide_exact(self):
        """Entrées : 8 et 2. Sortie attendue : 4."""

        self.assertEqual(divide(8, 2), 4)

    def test_divide_non_integer_result(self):
        """Entrées : 7 et 2. Sortie attendue : 3.5.

        Un résultat de 3 indiquerait une division entière (//) au lieu
        d'une division réelle.
        """

        self.assertAlmostEqual(divide(7, 2), 3.5)

    def test_divide_by_zero_raises(self):
        """Entrées : 5 et 0. Sortie attendue : ZeroDivisionError levée."""

        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

if __name__ == "__main__":
    unittest.main()
