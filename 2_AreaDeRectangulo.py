# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 11:16:53 2022

@author: YnwrdCreso

Calcula el área de un rectangulo

     _________________
    |                |
    |                |
    |                |
    |                | Altura
    |                |
    |                |
    |                |
    |                |
    __________________
          Base
    Area <---- Base * Altura
    
"""
print("Calcula el área de un rectangulo")
base = float(input("Valor de la base: "))
altura = float(input("Valor de la altura: "))
area = base * altura
print("El área es:", area)