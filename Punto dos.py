# Instrucción: de los retos anteriores selecione 3 funciones y escribalas con argumentos no definidos (*args).



#Primera función: reto 6, punto 7, función para calcular el promedio de 5 números reales

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




#Segunda función: reto 6, punto 7, función para calcular el promedio multiplicativo de 5 números reales

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




#Tecera función: reto 6, punto 7, función para calcular la raíz cúbica del menor número

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
