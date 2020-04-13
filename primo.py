def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero + 1):
        if numero % i == 0 and i != numero:
            return False
    return True

def primo(numero):
    if es_primo(numero):
        print("El numero %s es primo" % numero)
    else:
        print("El numero %s NO es primo" % numero)

numero = int(input("inserta un numero :  "))
primo(numero)
