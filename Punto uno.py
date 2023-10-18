# Instrucción: de los retos anteriores selecione 3 funciones y escribalas en forma de lambdas.


#Primera función: Reto 6, punto 1, función para calcular el volumen de la figura (esfera unida a un cono)

#La fórmula para hallar el volumen de una esfera es V=4/3*π*r1^3
#La fórmula para hallar el volumen de un cono es V=1/3*π*h*r2^2
#Por lo tanto, la función matemática para calcular el volumen de la figura es v=1/3*π*(4*r1^3+h*r2^2)

import math #importando math para utilizar el valor de pi
pi:float
PI=math.pi #Declarando el valor de pi como una constante

if __name__=="__main__":
    #Declarando e inicializando variables (se nombran las variables con camelCase, se especifica que son de tipo float y se usa la función input())
    radioUno=float(input("Ingrese el valor correspondiente a r1: "))
    radioDos=float(input("Ingrese el valor correspondiente a r2: "))
    altura=float(input("Ingrese el valor correspondiente a h: "))
    #Se crea la función lambda para calcular el volumen de la figura, teniendo como referencia la fórmula para hallar este volumen
    volumenTotal=(lambda a,b,c:(1/3)*PI*(4*a**3+b**2*c))(radioUno,radioDos,altura)#Los argumentos de la función son radioUno,radioDos y altura y la expresión que se devuelve es el resultado del cálculo del volumen de la figura
    print("Cuando r1 mide "+str(radioUno)+ ", r2 mide "+str(radioDos)+ " y h mide "+str(altura)+ ", el volumen total de la figura es: "+ str(volumenTotal))#Se imprime el resultado del volumen total




#Segunda función: Reto 6, punto 3, función para calcular la cantidad de carne de aves en kilos (si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente. )

if __name__=="__main__":
    #Declarando e inicializando variables (estas son nombradas con camelCase, son de tipo int y se inicializan con la función input())
    cantidadGallinas=int(input("Ingrese la cantidad de gallinas: "))
    cantidadGallos=int(input("Ingrese la cantidad de gallos: "))
    cantidadPollitos=int(input("Ingrese la cantidad de pollitos: "))
    #Se crea la función lambda que calcula la cantidad de carne, considerando que la cantidad total de carne es igual a la suma de la cantidad de los animales multiplicados por su peso.
    carneAves=(lambda a,b,c:(a*6+b*7+c*1))(cantidadGallinas,cantidadGallos,cantidadPollitos)#Los argumentos de la función son cantidadGallos,cantidadPollitos y cantidadGallinas y la expresión que se devuelve es el resultado del cálculo de la cantidad de carne
    print("La cantidad total de carne de aves en kilos es "+str(carneAves)+" cuando hay "+str(cantidadGallinas)+" gallinas, "+str(cantidadGallos)+" gallos y "+str(cantidadPollitos)+" pollitos.")#Se imprime el resultado de la cantidad total de carne de aves en kilos




#Tercera función: Reto 6, punto 4, función para calcular las vueltas de una compra
#Problema planteado: Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

if __name__=="__main__":
    #Declarando e inicializando variables (se nombran con camelCase, son de tipo int y se inicializan con la función input())
    cantidadPan=int(input("Ingrese la cantidad de panes comprados: "))
    cantidadLeche=int(input("Ingrese la cantidad de bolsas de leche compradas: "))
    cantidadHuevo=int(input("Ingrese la cantidad de huevos comprados: "))
    billete=int(input("Ingrese el valor del billete con el que se pagó la compra: "))
    #Se crea la función lambda que calcula las vueltas/lo que se debe, para este cálculo se le resta al valor del billete con el que se pagó el valor de la compra (que se calcula multiplicando la cantidad de cada uno de los productos por su precio)
    vueltas=(lambda a,b,c,d:a-(b*300+c*3300+d*350))(billete,cantidadPan,cantidadLeche,cantidadHuevo)#Los argumentos de la función son billete, cantidadPan, cantidadLeche y cantidadHuevo y la espresión que se devuelve es el resultado del cálculo de las vueltas

    #Se imprime una respuesta distinta dependiendo si hay vueltas, si se debe o si no hay ninguno de los dos casos
    if vueltas>0:#Si hay vueltas
        print("Si compró "+  str(cantidadPan)+ " panes, "+str(cantidadLeche)+ " bolsas de leche y " +str(cantidadHuevo)+ " huevos pagando con un billete de " + str(billete) +",las vueltas son " + str(vueltas)+ " pesos.")
    elif vueltas==0:#Si no hay vueltas
        print("Si compró "+  str(cantidadPan)+ " panes, "+str(cantidadLeche)+ " bolsas de leche y " +str(cantidadHuevo)+ " huevos pagando con un billete de " + str(billete) +", no hay vueltas, ni queda debiendo.")
    else:#Si se debe
        print("Si compró "+  str(cantidadPan)+ " panes, "+str(cantidadLeche)+ " bolsas de leche y " +str(cantidadHuevo)+ " huevos pagando con un billete de " + str(billete) +", usted queda debiendo " + str(-vueltas)+ " pesos.")