from decimal import Decimal, getcontext
import math
def pi(precision: int):
    if precision is None:
        getcontext().prec = 5
    elif precision is not None:
        getcontext().prec = precision

    pi = Decimal('3')
    counter = Decimal('0')
    for i in range(1, precision + 1):
        counter += Decimal('1')
        numero2 = counter * Decimal('2')
        segundo_termo = numero2 + Decimal('1')
        terceiro_termo = numero2 + Decimal('2')
        numero = Decimal('4') / (numero2 * segundo_termo * terceiro_termo)
        oi = numero % Decimal('2')
        if i % 2 != 0:
            pi += numero
        elif i % 2 == 0:
            pi -= numero
        print(f'Carregando... ({counter}/{precision})')
    return pi

def euler(precision: int):
    if precision is None:
        getcontext().prec = 5
    elif precision is not None:
        getcontext().prec = precision

    lista = []
    lista.append(Decimal('1'))
    counter = 0
    for _ in range(1, precision + 1):
        counter += 1
        numero = Decimal('1') / Decimal(math.factorial(counter))
        lista.append(numero)
        print(f'Carregando... ({counter}/{precision})')
    return sum(lista)

def goldenRatio(precision: int):
    if precision is None:
        getcontext().prec = 5
    elif precision is not None:
        getcontext().prec = precision

    raiz_5 = Decimal(5).sqrt()
    phi = (1 + raiz_5) / 2
    return phi

def pythagoras(precision: int = 5):
    if precision is None:
        getcontext().prec = 5
    elif precision is not None:
        getcontext().prec = precision

    return Decimal('2').sqrt()

def speedOfLight(measurementUnit: str):
    if measurementUnit == 'm/s':
        return Decimal('299792458')