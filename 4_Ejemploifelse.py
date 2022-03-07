# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 10:13:19 2022

@author: YnwrdCreso

Ejemplo IF Else, con operadores relacionales y logicos

Realizar un programa que diga si dos valores son
iguales uno o el otro a cero
pero que sean diferentes de enetre si

"""

x = float(input("Valor de x: "))
y = float(input("Valor de y: "))
if (x == 0 or y == 0) and x != y:
	print("X o Y son igual a cero, pero no ambas")
else:
	print("X o Y son diferentes de cero o iguales")
print(x, " ", y)