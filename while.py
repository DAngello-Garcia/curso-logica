# Función que multiplique dos números con sumas
#n1 > n2

def multiplicarConSumas(n1, n2):
    resultado = 0
    i = 0
    while i < n2:
        resultado += n2
        i += 1
    return resultado

# Función que divida dos números con restas
# n1>n2


def dividirConRestas(n1, n2, resultado):
    resta = n1
    i = 0
    while resta >= n2:
        resta -= n2
        i += 1
    if resultado == 'c':
        return resta
    else:
        return i  # residuo
