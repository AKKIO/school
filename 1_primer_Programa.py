# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 10:11:19 2022

@author: YnwrdCreso
"""
"""
altura <-- 9

"""
altura = 9 #Variable entera -4, -3, -2, ... 2, 3, 4
base = 5.5 #Variable flotante o de punto decimal.
caracter = 'A' #variable con un caracter
nombre = "Luis" #cadena de caracteres
es_mayor = 5>3 #boleano True o False
#si se escribe clear en la consola, está se limpiara
z1 = 3 + 5j #Variable del tipo compleja
calificaciones = [70, 80, 90] #Lista o vector
calificaciones[1] = 100 #cambiar el contenido en la posicion 2
"""
Para desplegar el contenido de una variable
DESPLEGAR altura
"""

#print(altura)
#print("la altura es: ", altura)
#print("La altura es: ", altura, " La base es: ", base, " El área es: ", base*altura)

"""
Para asignar a una variable, desde la consola
Pedir altura
"""
#a = input("valor de a: ")
#print("La variable a contiene: ", a)

"""
Operadores artimeticos Logicos y su precedencia
+   suma                            a + b
-   resta                           a - b
*   multiplicación                  a * b
**  Potencia                        a ** b
/   Cociente de la división         a / b
//  Cociente de la división entera  a // b
%   resto de la división entera     a % b

"""

a = 2
b = 9

print("%f + %f = %f"%(a, b, a + b))
print("%f - %f = %f"%(a, b, a - b))
print("%f * %f = %f"%(a, b, a * b))
print("%f ^ %f = %f"%(a, b, a ** b))
print("%f ^ %f = %f"%(a, 0.5, a ** 0.5)) #Raiz cuadrada
print("%f / %f = %f"%(b, a, b / a))
print("%f // %f = %f"%(b, a, b // a))
print("%f  %f = %f"%(b, a, b % a))

"""
Operadores de asignación
=       asignación simple           a = b
+=      asignación suma             a += b      a = a + b
-=      asignación resta            a -= b      a = a - b
*=      asignación multiplicación   a *= b      a = a * b
/=      asignación división         a /= b      a = a / b
%=      asignación modulo           a %= b      a = a % b
**=     asignacion exponente        a **= b     a = a ** b
//=     asignación division entera  a //= b     a = a // b

Operadores Relacionales
== igual a              a == b
!= distinto de          a != b
>  mayor que            a > b
<  menor que            a < b
>= mayor o igual que    a >= b
<= menor o igual que    a <= b

"""

a = 3
b = 2
print(a, "==", b,"   ", a == b)
print(a, "!=", b,"   ", a != b)
print(a, "> ", b,"   ", a >  b)
print(a, "< ", b,"   ", a <  b)
print(a, ">=", b,"   ", a >= b)
print(a, "<=", b,"   ", a <= b)

"""
Operadores Logicos

and     operador y      a and b
or      operador o      a or b
not     operador no     not a
"""

T = True
F = False

print(F, "and", F, " ", F and F)
print(F, "and", T, "  ", F and T)
print(T, " and", F, " ", T and F)
print(T, " and", T, "  ", T and T)
print("--------")
print(F, "or", F, " ", F or F)
print(F, "or", T, "  ", F or T)
print(T, " or", F, " ", T or F)
print(T, " or", T, "  ", T or T)
print("--------")
print("not", F, " ", not F)
print("not", T, "  ", not T)


"""
Precendencia de los operadores
**					1
*, /, %, // 		2
+, - 				3
<=, <, >=, > 		4
==, != 				5
=, %=, /=, //=		6
-=, +=, *=, **= 	7
"""
