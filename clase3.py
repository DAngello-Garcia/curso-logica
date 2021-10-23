def ingresoEstatura(mensaje):
    x = int(input(mensaje))
    return x

def convertirPies(est):
    x = est//30.48
    return x

def convertirPulgadas(est):
    x = est % 30.48
    y = x/2.54
    return y

estatura = ingresoEstatura("Ingrese su estatura en centímetros: ")
pies = convertirPies(estatura)
pulg = convertirPulgadas(estatura)
print("La persona que mide ", estatura," centímetros, mide ", pies," pies y ", pulg," pulgadas.")