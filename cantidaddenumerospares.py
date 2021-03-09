def largodeunnumero(num):
    if isinstance(num,int) and num>=0:
        if num==0:
            return 0
        else:
            return 1+largodeunnumero(num//10)
    else:
        return "digite un número entero positivo"


def numeroPar(num):
    if isinstance(num, int) and num>=0:
        if num%2==0:
            print("true")
        else:
            print("false")
    else:
        return "Digite un número entero positivo"

def cantidaddenumerospares(num):
    if isinstance(num,int) and num>=0:
        if num==0:
            return 0
        if num%2==0:
            return 1+cantidaddenumerospares(num//10)
        else:
            return 0+cantidaddenumerospares(num//10)
    else:
        return "Por favor digite un numero entero positivo"
