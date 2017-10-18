import math


def energia(m: float, c: float) -> float:
    """Esta funcion calcula la energia"""
    """Luis Angel Vealazquez Jimenez"""
    """GITI7092e"""
    opera = float
    opera = m * (c * c)
    return opera


def formula(b: float, a: float, c: float) -> float:
    """Esta funcion calcula el resultado de la formula general"""
    """Luis Angel Velazquez Jimenez"""
    """GITI7092e"""
    ope1 = b * b
    ope2 = 4 * a * c
    ope3 = ope1 - ope2
    ope4 = 2 * a
    raiz = math.sqrt(ope2)
    x1 = -b + raiz / (2 * a)
    x2 = -b - raiz / (2 * a)
    return x1, x2
