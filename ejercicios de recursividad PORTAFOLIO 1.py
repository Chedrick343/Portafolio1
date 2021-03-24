"""
Nombre de la función: divisores
entradas: Un número
salidas: Los números que dividen al número ingresado
restricciones:el número debe ser entero y positivo
"""



def divisores(num):
    if isinstance(num,int)and num>0:
        return divisoresAux(num,num)
    else:
        print("Digite un número entero y positivo")


def divisoresAux(num,contador):
    if contador==1:
        return 1
    if num%contador==0:
        print(contador)
        return divisoresAux(num,contador-1)
    else:
        return divisoresAux(num,contador-1)




"""
Nombre de la función: multiplicarRecursivo
entradas: un número y su factor
salidas: la multiplicacion del número y su factor
restricciones: ambas entradas deben ser números enteros y positivos

"""
def multiplicarRecursivo(num,factor):
    if isinstance(num,int):
        if isinstance(factor,int):
            if factor<=0:
                return 0
            else:
                return num+multiplicarRecursivo(num,factor-1)
        else:
            print("El factor debe de ser entero")
    else:
        print("El número debe de ser entero")


"""
Nombre de la función: divisionRecursivo
entradas: Un número a dividir y un divisor
salida: el resultado de la división
restricciones: Las entradas deben de ser números enteros y mayores que 0
"""
def divisionRecursivo(divisor,dividendo):
    if isinstance(divisor,int) and isinstance(dividendo,int):
        if dividendo>0 and divisor>0:
            return divisionRecursivoAux(divisor,dividendo,1,0)
        else:
            print("Los valores deben de ser positivos")
    else:
        print("Los valores deben ser números enteros")


def divisionRecursivoAux(divisor,dividendo,multi,potencia):
    if divisor<dividendo:
        return 0
    elif multi*dividendo<divisor:
        return divisionRecursivoAux(divisor,dividendo,multi+1,potencia)
    elif multi*dividendo==divisor:
        return multi*10**potencia
    elif multi*dividendo>divisor:
        return multi*10**potencia+divisionRecursivoAux(divisor-(dividendo*multi),dividendo,multi-(multi+1),potencia+1)
        



"""
Nombre de la función:indiceNumero
entradas:un número y su indice
salidas: el número que está en el respectivo indice
restricciones: un número entero positivo.
"""
def ContarDigitos(num):
    if isinstance(num,int)and num>=0:
        if num==0:
            return 0
        else:
            return 1 + ContarDigitos(num//10)
    else:
        return "El número debe de ser entero y positivo"




def indiceNumero(num,indice):
    if isinstance (num,int) and isinstance(indice,int):
        if num>0 and indice>0:
            return indiceNumeroAux(numero_inverso(num),indice)
        else:
            print("El número y el indice deben de ser numeros positivos")
    else:
        print("El número y el indice deben ser números enteros")
    
def indiceNumeroAux(num,indice):
    if indice==0:
        return num%10
    else:
        return (num//10**(indice))%10



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



"""
Nombre de la función: cortarNumero
Entradas: un número y sus indices
salida: los números que están dentro del rango de los indices, incluidos los números que están en los indices indicados
restricciones, un número entero positivo y los indices enteros y positivos también
"""
def cortarNumero(num,indice1,indice2):
    if isinstance(num,int) and isinstance(indice1,int)and isinstance(indice2,int):
        if num>0 and indice1>=0 and indice2>=0:
            if indice1==0 and indice2==0:
                return numero_inverso(num)%10
            if indice1==0 and indice2>0:
                return cortarNumeroAux3(numero_inverso(num)%(10**(indice2+1)))
            if indice1>0 and indice2==0:
                return cortarNumeroAux3(numero_inverso(num)%10**(indice1+1))
            else:
                return cortarNumeroAux(numero_inverso(num),indice1,indice2)#invierto el número para poder evaluarlo
        else:
            print("Los valores deben de ser positivos")
    else:
        print("los valores deben de ser números enteros")


def cortarNumeroAux(num,indice1,indice2):
    return cortarNumeroAux2(num,mayor(indice1,indice2),menor(indice1,indice2))#busco cuál indice es mayor para poder obtener mi rango


def cortarNumeroAux2(num,distancia1,distancia2):
    return (cortarNumeroAux3((num%10**(distancia1+1))//10**distancia2))#obtengo mi rango
def cortarNumeroAux3(num):
    return numero_inverso(num)#vuelvo a invertir el número para devolver el rango original
            
        

def mayor(indice1,indice2):
    if indice1>indice2:
        return indice1
    else:
        return indice2

def menor(indice1,indice2):
    if indice1>indice2:
        return indice2
    else:
        return indice1
