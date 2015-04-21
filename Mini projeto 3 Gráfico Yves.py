# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 18:42:23 2015

@author: Yves Yuzo
"""
from Mini_Projeto_3 import*

#Criação de uma lista com os valores do arquivo alimentos 
raw = open("alimentos.csv")
leitura = raw.readlines()
alimentos = []
for pa in leitura:
    x = pa.strip().lower()
    if x != "":
        alimentos.append(x)
#Criação de uma lista com a info do usuario
        
usuario_raw = open("usuario.csv", encoding = "cp1252")
leitura2 = usuario_raw.readlines()
usuario = []
for la in leitura2:
    y = la.strip().lower()
    if y != "":
        usuario.append(y)
        
        

lista_de_alimentos = criador_info_nutricional (alimentos)
info_usuario_parcial = criador_lista_com_numeros_do_usuario (usuario)
tmb = calcula_tmb (info_usuario_parcial, usuario)
imc = calcula_imc (info_usuario_parcial)

print (tmb)


