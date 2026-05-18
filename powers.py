# Replace the "ANSWER HERE" for your answer

def power(base, exp):
    """
    Retorna base elevado a exp usando un bucle for.
    exp es siempre >= 0.

    Ejemplo: power(2, 3) -> 8  (2*2*2)
    """
    if exp < 0:
        return f"Error"
    pot = 1
    for i in range(exp):
        pot *= base
    return pot


def sum_of_powers(base, max_exp):
    """
    Retorna la suma de base^0 + base^1 + ... + base^max_exp.
    Debe USAR la funcion power.

    Ejemplo: sum_of_powers(2, 3) -> 15  (1+2+4+8)
    """
    resultado = 0
    for i in range(max_exp + 1):  
        resultado += power(base, i)  
    return resultado
