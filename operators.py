"""Regroupe les opérations utilisées par le serveur de la calculatrice."""

def add(a,b):
    """Effectue l'addition entre deux nombres.

    Args:
        a (float): Premier opérande fourni par le serveur.
        b (float): Second opérande fourni par le serveur.
    
    Returns:
        float: Somme de a et b.
    """

    return a + b

def subtract(a,b):
    """Effectue la soustraction entre deux nombres.

    Args:
        a (float): Premier opérande fourni par le serveur.
        b (float): Second opérande fourni par le serveur.
    
    Returns:
        float: Différence a - b.
    """

    return a - b

def multiply(a,b):
    """Effectue la multiplication entre deux nombres.

    Args:
        a (float): Premier opérande fourni par le serveur.
        b (float): Second opérande fourni par le serveur.
    
    Returns:
        float or complex: Puissance a ** b dans l'implémentation de base.
            Le résultat attendu pour la calculatrice est le produit a * b.
    
    Raises:
        ZeroDivisionError: Si le a est nul et b est négatif.
        OverflowError: Si la puissance dépasse la capacité des flottants.
    """

    return a ** b

def divide(a,b):
    """Effectue la division entre deux nombres.

    Args:
        a (float): Dividende fourni par le serveur.
        b (float): Diviseur non nul fourni par le serveur.
    
    Returns:
        float: Quotient arrondi vers moins l'infini (a // b) dans
            l'implémentation de base. Le résultat attendu est a / b.
    
    Raises:
        ZeroDivisionError: Si b est nul.
    """
        
    return a // b
