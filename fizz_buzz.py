# *
# *
# *
# *
# Prueba 1
# Escribe un programa que muestre por consola (con print) los numeros del 1 al 100 (ambos incluidos y con un salto de linea entre ellos), sustituyendo lo siguientes:
# - Multiplo de 3 por la palabra "fizz"
# - Multiplo de 5 por la palabra "buzz"
# - Multiplos de 3 y 5 a la vez por la pabala "fizzbuzz"
# *
# *
# *  

def fizzbuzz():
  for i in range (1, 101):
    if i%3 == 0 and i%5 == 0:
      print("fizzbuzz")
    elif i%3 == 0:
      print("fizz")
    elif i%5 == 0:
      print("buzz")
    else:
      print(i)
      

fizzbuzz()