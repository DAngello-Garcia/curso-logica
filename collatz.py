def collatz(n):
    comparador = n
    contador = 0
    while comparador >= 1:
        if comparador == 1:
            return contador
        elif comparador % 2 == 0:
            comparador = comparador / 2
            contador += 1
        else:
            comparador = comparador*3+1
            contador += 1


print(collatz(5))
