# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 08:10:08 2015

@author: Yves Yuzo
"""
#Criação de uma lista com os valores do arquivo alimentos 
raw = open("alimentos.csv")
leitura = raw.readlines()
alimentos = []
for pa in leitura:
    x = pa.strip().lower()
    if x != "":
        alimentos.append(x)
        
usuario_raw = open("usuario.csv", encoding = "cp1252")
leitura2 = usuario_raw.readlines()
usuario = []
for la in leitura:
    y = la.strip().lower()
    if y != "":
        usuario.append(y)
#--------------------------
print(usuario)

