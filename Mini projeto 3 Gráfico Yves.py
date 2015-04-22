# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 18:42:23 2015

@author: Yves Yuzo
"""
from Mini_Projeto_3 import*
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.legend_handler import HandlerLine2D
        
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

'''
----------------------------------------
LISTAS QUE GERAM OS GRÁFICOS
----------------------------------------
'''
#Retorna lista das datas do arquivo passado
datas = intervalo_de_tempo_do_usuario (usuario)

#retorna lista de datas de um arquivo de usuario com 7 dias diferentes
datas2 = intervalo_de_tempo_do_usuario (usuario_teste)

lista_tmb = [tmb] * 8

#gera lista das calorias consumidas
lista_calorias = gerar_lista_calorias (usuario_teste, dicionario_de_alimentos)

#gera lista das proteinas consumidas
lista_proteinas = gerar_lista_proteinas (usuario_teste, dicionario_de_alimentos)

#gera lista dos carboidratos consumidas
lista_carboidratos = gerar_lista_carboidratos (usuario_teste, dicionario_de_alimentos)

#gera lista das gorduras consumidas
lista_gorduras = gerar_lista_gorduras (usuario_teste, dicionario_de_alimentos)


print(datas2, lista_calorias, lista_proteinas, lista_carboidratos, lista_gorduras)

"""
----------------------------------------
GRÁFICOS
----------------------------------------
"""
"""
Calorias consumidas e calorias recomendadas por dia
"""
plt.plot(datas2, lista_calorias, label = "calorias consumidas")
plt.plot(datas2, lista_tmb, label = 'calorias recomendadas')
#verde = mpatches.Patch(color='green', label='Calorias recomendadas p/dia')
#azul = mpatches.Patch(color='blue', label='Calorias Consumidas')
#plt.legend(handles=[verde])
#plt.legend(handles = [azul])
plt.legend()
plt.xlabel('Dias do mes')
plt.ylabel('kcal')
plt.show()

plt.plot(datas2, lista_proteinas, label = "Proteinas Consumidas")
plt.plot(datas2, lista_carboidratos, label = 'Carboidratos Consumidos')
plt.plot(datas2, lista_gorduras, label = 'Gorduras Consumidas')
verde = mpatches.Patch(color='green', label='Calorias recomendadas p/dia')

plt.legend()
plt.xlabel('Dias do Mes')
plt.ylabel('Gramas')
plt.show()


