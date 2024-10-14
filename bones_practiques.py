#!/usr/bin/env python

"""
Nom del programa: Divisió entera i residu

Descripció: Aquest programa permet introduir dos nombres
enters (dividend i divisor),
realitza la divisió entera, calcula el quocient
i el residu, i mostra els resultats.

__author__ = [Amira Shobet Biyah]
__email__ = [afathi@instituticaria.cat]
__date__ = 2024/10/12
Institut Icària - Programació 1r Batxillerat - Curs 2023-24
"""

Divident= int(input("Introdueix el Divident:"))
Divisor = int(input("Introdueix el Divisor:"))
Quocient = Divident // Divisor
Residu = Divident % Divisor
print(f"Divisió: {Divident}/{Divisor}")
print(f"Quocient: {Quocient}")
print(f"Residu: {Residu}")
