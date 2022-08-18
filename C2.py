#                     C2 (12-ago)
# ------------------ OPERADORES LÓGICOS-------------
resultado = 10 < 20
print (resultado)
a = 10
b = 16
c = 21

resultado = (a>b)and (b<c)

print (resultado)
# ------------------ OPERADORES ARITMÉTICOS-------------

a = 0
a = a+5 #Forma tradicional de sumar
a+=5 #Suma en python
a-=5 #Resta en python
a*=3 #Multiplicación en python
a/=2 #División en python
a**=2 #Potencia en python
print (a)

# ------------------ SALIDAS EN PYTHON -------------
nombre = "Azul"
edad = 21

print (f"Hola mi nombre es {nombre} y tengo {edad}")

# ------------------ FUNCIONES INTEGRADAS-------------

n = int("8") #De v. cadena a entero
n = float ("5")  #De v. cadena a float
n = str (16) #De v. entero a cadena

h = bin (0)  #binario
print (h)

# Para valor absoluto abs ()
# Para redondear round ()

# ------------------ RESOLVIENDO ECUACIONES -------------
a = float (input("a-> "))
b = float (input("b-> "))
c = float (input("c-> "))

ecuacion = (a**3*(b**2-2*a*c))/(2*b)

print (f"El resultado de la ecuación es {ecuacion}")

# ------------------ EJERCICIO---------------
x = float(input("x-> "))
y = float(input("y-> "))
z = float(input("z-> "))

ecuacion = (y*(x**2)+(y*x)+z**2)/(x**3*y**2)

print (ecuacion)
redondeo = round(ecuacion)
print(redondeo)

# ----------- EJERCICIO SIN INPUT----------
x = 12
y = 7
z = 5
print (ecuacion)

# ------------------ CONDICIONAL -------------

#Definimos datos de aignación

a = int (input ("el numero es: "))

if a>0:
    print ("positivo")
elif a==0:
    print ("a es cero")
else:
    print ("negativo")

    print ("fin")