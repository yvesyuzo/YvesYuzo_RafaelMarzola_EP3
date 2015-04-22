# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 18:42:23 2015

@author: Yves Yuzo
"""
from Mini_Projeto_3 import*
        
#lista_de_alimentos é um dicionario onde cada key é o nome de uma alimento e seus values são as informações na ordem: 
    #Quantidade(g),Calorias (kcal),Proteínas (g),Carboidratos (g),Gorduras (g)
dicionario_de_alimentos = criador_info_nutricional (alimentos)

# Lista com as seguintes informações do usuario na ordem: Idade(anos), Peso(kg), Altura(m)
info_usuario_parcial = criador_lista_com_numeros_do_usuario (usuario)

# Valor da quantidade de calorias diarias necessarias para manter o peso atual
    #de acordo com a fórmula de Harris-Benedict
tmb = calcula_tmb (info_usuario_parcial, usuario)

#Indice de Massa Corporal, de acordo com a fórmula de Nick Trefethen
imc = calcula_imc (info_usuario_parcial)

datas = intervalo_de_tempo_do_usuario (usuario)
datas2 = intervalo_de_tempo_do_usuario (usuario_teste)

x =  float(dicionario_de_alimentos['quindim'][2])
y = x + 2 

print(y)

calorias_consumidas_a_cada_dia (usuario, dicionario_de_alimentos)
