# Escriba una función recursiva para calcular la operación de la potencia.

def potenciaRecursivo(a:int,b:int)-> int:

  # Caso base 
  if b == 1: 
    return a
  else:
    # Condicion de la funcion recursiva
    return a*potenciaRecursivo(a,b-1)#Se le resta una unidad a b

if __name__ == "__main__":#Función principal
  base= int(input("Ingrese la base de la potencia: "))
  exponente=int(input("Ingrese el exponente de la potencia: "))
  resultadoPotencia = potenciaRecursivo(base,exponente)
  print("El resultado de la operación de la potencia de  " + str(base) + " elevado a la " + str(exponente)+ " es " +str(resultadoPotencia))