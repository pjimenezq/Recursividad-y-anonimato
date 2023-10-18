# Reto 9: Funciones recursivas, funciones anónimas y argumentos no definidos
**Instrucciones:**

Desarrolle la mayoría de ejercicios en clase. Para cada punto cree un programa individual. Al finalizar suba todo a un repo y subalo al canal reto_9 en slack.

## Punto uno
De los retos anteriores selecione 3 funciones y escribalas en forma de lambdas.

**Primera función**

Reto 6, punto 1, función para calcular el volumen de la figura (esfera unida a un cono)

![image](https://github.com/pjimenezq/Recursividad-y-anonimato/assets/141860508/62396054-f32f-4157-adf3-93eb25c45df4)

**Sin lambdas**
```
#La fórmula para hallar el volumen de una esfera es V=4/3*π*r1^3
#La fórmula para hallar el volumen de un cono es V=1/3*π*h*r2^2
#Por lo tanto, la función matemática para calcular el volumen de la figura es v=1/3*π*(4*r1^3+h*r2*2)

import math #importando math para utilizar el valor de pi
pi:float
PI=math.pi #Declarando el valor de pi como una constante

#Función para calcular el volumen de la figura
def volumenFigura (radioUno:float, radioDos:float, altura:float)->float:
    volumen=(1/3)*PI*(4*radioUno**3+radioDos**2*altura)#Utilizando la función matemática para calcular el volumen que se halló en la primera parte
    return volumen

if __name__=="__main__":
    #Declaración de variables e inicializando variables (nombrándolas con Camelcase y especificando que son de tipo float)

    radioUno=float(input("Ingrese el valor correspondiente a r1: "))
    radioDos=float(input("Ingrese el valor correspondiente a r2: "))
    altura=float(input("Ingrese el valor correspondiente a h: "))

    volumenTotal=volumenFigura(radioUno,radioDos,altura)
    print("Cuando r1 mide "+str(radioUno)+ ", r2 mide "+str(radioDos)+ " y h mide "+str(altura)+ ", el volumen total de la figura es: "+ str(volumenTotal))

```

**Con lambdas**
```
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
```
**Segunda función**

Reto 6, punto 3, función para calcular la cantidad de carne de aves en kilos (si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente. )

**Sin lambdas**
```
#Declarando e inicializando constantes
PESO_GALLINAS:int
PESO_GALLINAS=6
PESO_GALLOS:int
PESO_GALLOS=7
PESO_POLLITOS:int
PESO_POLLITOS=1
#Función para calcular la cantidad de carne
def cantidadCarne(cantidadGallinas:int,cantidadGallos:int,cantidadPollitos:int)->int:
    totalCarne=cantidadGallinas*PESO_GALLINAS+cantidadGallos*PESO_GALLOS+cantidadPollitos*PESO_POLLITOS #La cantidad total de carne es igual a la suma de la cantidad de los animales por su peso.
    return totalCarne
if __name__=="__main__":
    #Declarando e inicializando variables (nombrando con Camelcase y especificando tipo int dado a que el número de animales es siempre entero).
    cantidadGallinas=int(input("Ingrese la cantidad de gallinas: "))
    cantidadGallos=int(input("Ingrese la cantidad de gallos: "))
    cantidadPollitos=int(input("Ingrese la cantidad de pollitos: "))
    carneAves=cantidadCarne(cantidadGallinas,cantidadGallos,cantidadPollitos)
    print("La cantidad total de carne de aves en kilos es "+str(carneAves)+" cuando hay "+str(cantidadGallinas)+" gallinas, "+str(cantidadGallos)+" gallos y "+str(cantidadPollitos)+" pollitos.")
```
**Con lambdas**
```
if __name__=="__main__":
    #Declarando e inicializando variables (estas son nombradas con camelCase, son de tipo int y se inicializan con la función input())
    cantidadGallinas=int(input("Ingrese la cantidad de gallinas: "))
    cantidadGallos=int(input("Ingrese la cantidad de gallos: "))
    cantidadPollitos=int(input("Ingrese la cantidad de pollitos: "))
    #Se crea la función lambda que calcula la cantidad de carne, considerando que la cantidad total de carne es igual a la suma de la cantidad de los animales multiplicados por su peso.
    carneAves=(lambda a,b,c:(a*6+b*7+c*1))(cantidadGallinas,cantidadGallos,cantidadPollitos)#Los argumentos de la función son cantidadGallos,cantidadPollitos y cantidadGallinas y la expresión que se devuelve es el resultado del cálculo de la cantidad de carne
    print("La cantidad total de carne de aves en kilos es "+str(carneAves)+" cuando hay "+str(cantidadGallinas)+" gallinas, "+str(cantidadGallos)+" gallos y "+str(cantidadPollitos)+" pollitos.")#Se imprime el resultado de la cantidad total de carne de aves en kilos
```
**Tercera función**

Reto 6, punto 4, función para calcular las vueltas de una compra
**Sin lambdas**
```
#Declarando constantes
PRECIO_PAN:int
PRECIO_PAN=300
PRECIO_LECHE:int
PRECIO_LECHE=3300
PRECIO_HUEVO:int
PRECIO_HUEVO=350

#Función para calcular las vueltas
def vueltas(cantidadPan:int,cantidadLeche:int,cantidadHuevo:int,billete:int)->int:
    totalVueltas=billete-(PRECIO_PAN*cantidadPan+PRECIO_LECHE*cantidadLeche+PRECIO_HUEVO*cantidadHuevo)
    return totalVueltas

if __name__=="__main__":
    #Declarando e inicializando variables
    cantidadPan=int(input("Ingrese la cantidad de panes comprados: "))
    cantidadLeche=int(input("Ingrese la cantidad de bolsas de lecha compradas: "))
    cantidadHuevo=int(input("Ingrese la cantidad de huevos comprados: "))
    billete=int(input("Ingrese el valor del billete con el que se pagó la compra: "))

    vueltasCompra=vueltas(cantidadPan,cantidadLeche,cantidadHuevo,billete)#Se imprime una respuesta distinta dependiendo si hay vueltas, si se debe o si no hay ninguno de los dos casos.
    if vueltasCompra>0:
        print("Si compró "+  str(cantidadPan)+ " panes, "+str(cantidadLeche)+ " bolsas de leche y " +str(cantidadHuevo)+ " huevos pagando con un billete de " + str(billete) +",las vueltas son " + str(vueltasCompra)+ " pesos.")
    elif vueltasCompra==0:
        print("Si compró "+  str(cantidadPan)+ " panes, "+str(cantidadLeche)+ " bolsas de leche y " +str(cantidadHuevo)+ " huevos pagando con un billete de " + str(billete) +", no hay vueltas, ni queda debiendo.")
    else:
        print("Si compró "+  str(cantidadPan)+ " panes, "+str(cantidadLeche)+ " bolsas de leche y " +str(cantidadHuevo)+ " huevos pagando con un billete de " + str(billete) +", usted queda debiendo " + str(-vueltasCompra)+ " pesos.")
```
**Con lambdas**
```
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
```
## Punto dos
De los retos anteriores selecione 3 funciones y escribalas con argumentos no definidos (*args).

**Primera función**

Reto 6, punto 7, función para calcular el promedio de 5 números reales

**Sin \*args**
```
def promedio(a:float, b:float, c:float, d:float, e:float)->float:
    elPromedio=(a+b+c+d+e)/5
    return elPromedio
if __name__=="__main__":
    #Declarando e inicializando las variables correspondientes a los 5 números reales del problema planteado
    a=float(input("Ingrese el primer número real "))
    b=float(input("Ingrese el segundo número real "))
    c=float(input("Ingrese el tercer número real "))
    d=float(input("Ingrese el cuarto número real "))
    e=float(input("Ingrese el quinto número real "))

    #Aplicando las funciones
    promedioFinal=promedio(a,b,c,d,e)
    print("El promedio de los cinco números reales es "+str(promedioFinal))
```
**Con \*args**
```
def promedio(*args)->float:#Función para calcular el promedio de n argumentos sin nombre
    suma:int=0#Se declara la variable suma que se inicializa en 0
    for num in args:#para cada uno de los elementos (nombrados num) de args...
        suma+=num#...se hace la suma de este elemento a la variable suma
    #De esta manera,se obtiene la sumatoria de todos los números que se deseen
    elPromedio=suma/(len(args))#Para encontrar el promedio se divide la suma de todos los elementos entre la cantidad de elementos que tiene args
    return elPromedio#La función retorna el valor del promedio calculado

if __name__=="__main__":#Función principal
    #Declarando e inicializando las variables correspondientes a los 5 números reales del problema planteado
    a=float(input("Ingrese el primer número real "))
    b=float(input("Ingrese el segundo número real "))
    c=float(input("Ingrese el tercer número real "))
    d=float(input("Ingrese el cuarto número real "))
    e=float(input("Ingrese el quinto número real "))

    print("El promedio de los cinco números reales ingresados es "+str(promedio(a,b,c,d,e)))#Se imprime el resultado del promedio de los cinco números ingresados por el usuario
    print("El promedio de los números reales es "+str(promedio(-10,5,115,-25,-50,15,-20)))#En este caso se imprime el resultado del promedio de la cantidad de números que uno desee, demostrando la funcionalidad de *args
```
**Segunda función**

Reto 6, punto 7, función para calcular el promedio multiplicativo de 5 números reales

**Sin \*args**
```
def promedioMultiplicativo(a:float, b:float, c:float, d:float, e:float)->float:
    elPromedioMultiplicativo=(a*b*c*d*e)**(1/5)
    return elPromedioMultiplicativo
if __name__=="__main__":
    #Declarando e inicializando las variables correspondientes a los 5 números reales del problema planteado
    a=float(input("Ingrese el primer número real "))
    b=float(input("Ingrese el segundo número real "))
    c=float(input("Ingrese el tercer número real "))
    d=float(input("Ingrese el cuarto número real "))
    e=float(input("Ingrese el quinto número real "))
    promedioMultiplicativoFinal=promedioMultiplicativo(a,b,c,d,e)
    print("El promedio multiplicativo es "+ str(promedioMultiplicativoFinal))

```
**Con \*args**
```
def promedioMultiplicativo(*args)->float:#Función para calcular el promedio multiplicativo de n argumentos sin nombre
    multiplicacion:int=1#Se declara la variable multiplicacion que se inicializa en 1
    for num in args:#para cada uno de los elementos (nombrados num) de args...
        multiplicacion*=num#... se lleva a cabo la multiplación de este elemento por el valor de la variable multiplicacion
    #De esta forma, se obtiene la multiplicación de los números ingresados al programa
    elPromedioMultiplicativo=(multiplicacion)**(1/(len(args)))# Para hallar el promedio multiplicativo se calcula la multiplicación de todos los elementos elevado a 1 dividido la cantidad de elementos que tiene args
    return elPromedioMultiplicativo#La función retorna el valor del promedio multiplicativo calculado

if __name__=="__main__":#Función principal
   #Declarando e inicializando las variables correspondientes a los 5 números reales del problema planteado
    a=float(input("Ingrese el primer número real "))
    b=float(input("Ingrese el segundo número real "))
    c=float(input("Ingrese el tercer número real "))
    d=float(input("Ingrese el cuarto número real "))
    e=float(input("Ingrese el quinto número real "))
   
    print("El promedio multiplicativo de los cinco números reales es "+str(promedioMultiplicativo(a,b,c,d,e)))#Se imprime el resultado del promedio multiplicativo de los cinco números ingresados por el usuario
    print("El promedio multiplicativo de los cinco números reales es "+str(promedioMultiplicativo(1,2,3,4,5,6,10,56,9)))#En este caso se imprime el resultado del promedio multiplicativo de la cantidad de números que uno desee, demostrando la funcionalidad de *args
```
**Tercera función**

Reto 6, punto 7, función para calcular la raíz cúbica del menor número

**Sin \*args**
```
def raizCubicaMenorNumero(a:float, b:float, c:float, d:float, e:float)->float:
    primero=a
    segundo=b
    tercero=c
    cuarto=d
    quinto=e

    if primero>segundo:
        segundo=primero
        primero=b

    if primero>tercero:
        tercero=primero
        primero=c

    if primero>cuarto:
        cuarto=primero
        primero=d

    if primero>quinto:
        quinto=primero
        primero=e
   
    raizCubica=primero**(1/3)
    return raizCubica

if __name__=="__main__":
    #Declarando e inicializando las variables correspondientes a los 5 números reales del problema planteado
    a=float(input("Ingrese el primer número real "))
    b=float(input("Ingrese el segundo número real "))
    c=float(input("Ingrese el tercer número real "))
    d=float(input("Ingrese el cuarto número real "))
    e=float(input("Ingrese el quinto número real "))

    raizCubicaMenor=raizCubicaMenorNumero(a,b,c,d,e)
    print("La raíz cúbica del menor número es " + str(raizCubicaMenor))
```
**Con \*args**
```
def raizCubicaMenorNumero(*args)->float:#Función para calcular la raíz cúbica de n argumentos sin nombre
    for num in args:#Para cada uno de los elementos (nombrados num) de args...
        menorNumero=min(args)#... se obtiene el mínimo elemento
    #De esta manera, se obtiene el menor número de los valores ingresados al programa
    raizCubica=menorNumero**(1/3)# Para hallar la raíz cúbica del menor número se calcula el menor número elevado a 1/3 (la raíz cúbica se transforma en potencia)
    return raizCubica#La función retorna el valor calculado de la raíz cúbica

if __name__=="__main__":#Función principal
   #Declarando e inicializando las variables correspondientes a los 5 números reales del problema planteado
    a=float(input("Ingrese el primer número real "))
    b=float(input("Ingrese el segundo número real "))
    c=float(input("Ingrese el tercer número real "))
    d=float(input("Ingrese el cuarto número real "))
    e=float(input("Ingrese el quinto número real "))

    print("La raíz cúbica del menor número es: "+ str(raizCubicaMenorNumero(a,b,c,d,e)))#Se imprime el resultado de la raíz cúbica del menor número de los cinco números ingresados por el usuario
    print("La raíz cúbica del menor número es: "+ str(raizCubicaMenorNumero(81,125,27,100,3500,1000000,99))) #En este caso se imprime el resultado de la raíz cúbica del menor número de la cantidad de números que uno desee, demostrando la funcionalidad de *args

```
