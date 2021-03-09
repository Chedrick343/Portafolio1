def numero_inverso(num):
    if isinstance(num,int):
        if num>=0:
            if num<10:
                return num
            else:
                return numero_inverso_aux(num, ContarDigitos(num))
    else:
        print:("Digite un número entero positivo")


def numero_inverso_aux(num, largo):
    if largo==0:
        return 0
    else:
        return (num%10)*10**(largo-1)+ numero_inverso_aux(num//10, largo-1)