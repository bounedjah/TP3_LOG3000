"""Application Flask qui affiche la calculatrice, valide les expressions envoyées et retourne leur résultat."""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

# Regroupe les opérations utilisées pour valider l'expression et effectuer le calcul.
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """Évalue une expression à un seul opérateur et retourne son résultat.

    Args: 
        expr (str): Expression de la forme « a op b », op parmi +, -, *, /. 
            Les espaces sont ignorés. Chaque nombre peut être négatif
            (ex. « -5+3 », « 3*-2 »).

    Returns:
        float: Résultat du calcul effectué par la fonction correspondant à 
            l'opérateur dans OPS.
    
    Raises:
        ValueError: Si l'expression est vide, n'est pas une chaîne de caractères
            ou ne respecte pas le format de deux nombres séparés par un seul opérateur.
        ZeroDivisionError: Si le calcul tente une division par zéro.
        OverflowError: Si le résultat dépasse la valeur maximale représentable
            par un nombre flottant.
    """

    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # Une seule opération est autorisée, car les priorités de calcul ne sont pas gérées.
    for i, ch in enumerate(s):
        if ch in OPS:
            # Un - en début d'expression ou juste après l'opérateur est le signe d'un nombre négatif.
            if ch == '-' and (i == 0 or s[i-1] in OPS):
                continue
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # L'opérateur doit être placé entre deux nombres.
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    # Les opérandes doivent être numériques pour permettre le calcul.
    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """Affiche la calculatrice et calcule l'expression envoyée par le formulaire.

    Entrées:
        Aucun paramètre. Utilise la méthode de la requête Flask et, pour une
        requête POST, la valuer du champ « display » (vide si le champ est absent).
    
    Returns:
        str: Page HTML affichant la calculatrice vide en GET, ou le résultat du 
            calcul ou un message d'erreur en POST.
    """

    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            # Affiche l'erreur dans la calculatrice pour que l'utilisateur puisse réessayer.
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)