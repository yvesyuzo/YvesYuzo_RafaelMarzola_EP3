# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 19:15:18 2015

@author: rafaelmarzolla
"""

# MARZOLA Vamos trabalhar no grafico cada um em arquivos separados para não dar erro de sincronização

from Mini_Projeto_3 import*
        
import matplotlib.pyplot as plt


lista_de_alimentos = criador_info_nutricional (alimentos)
info_usuario_parcial = criador_lista_com_numeros_do_usuario (usuario)
tmb = calcula_tmb (info_usuario_parcial, usuario)
imc = calcula_imc (info_usuario_parcial)

print (tmb)

 
   #Calorias
   #grafico do dia 06/04/15. Comparacao do consumo diario de energia com o consumo ideal de energia
fig, ax1 = plt.subplots()
t = tmb #escala
ax1.plot(t, 'b-')
ax1.set_xlabel('Consumo de Calorias (kcal)')
ax1.set_ylabel('Consumo do usuario', color='b')
u = imc
 
plt.title ("Gráfico do dia 06/04/15")
ax2 = ax1.twinx()
ax2.plot(u, 'b-')
ax2.set_ylabel('Consumo ideal', color='r')
plt.show()

    #grafico do dia 07/04/15. Comparacao do consumo diario de energia e do consumo ideal
fig, ax1 = plt.subplots()
t = tmb
ax1.plot(t, "b-")
ax1.set_xlabel('Consumo de Calorias (kcal)')
ax1.set_ylabel('Consumo do usuario', color='b')
u = imc
 
plt.title ("Gráfico do dia 07/04/15")
ax2 = ax1.twinx()
ax2.plot(u, 'b-', color='r')
ax2.set_ylabel('Consumo ideal', color='r')
plt.show()


   #Proteinas
   #grafico do dia 06/04/15. Comparacao do consumo diario de energia com o consumo ideal de energia
fig, ax1 = plt.subplots()
t = tmb #escala
ax1.plot(t, 'b-')
ax1.set_xlabel('Consumo de Proteinas (g)')
ax1.set_ylabel('Consumo do usuario', color='b')

u = imc
 
plt.title ("Gráfico do dia 06/04/15")
ax2 = ax1.twinx()
ax2.plot(u, 'b-')
ax2.set_ylabel('Consumo ideal', color='r')
plt.show()

    #grafico do dia 07/04/15. Comparacao do consumo diario de energia e do consumo ideal
fig, ax1 = plt.subplots()
t = tmb
ax1.plot(t, "b-")
ax1.set_xlabel('Consumo de Proteinas (g)')
ax1.set_ylabel('Consumo do usuario', color='b')
u = imc
 
plt.title ("Gráfico do dia 07/04/15")
ax2 = ax1.twinx()
ax2.plot(u, 'b-', color='r')
ax2.set_ylabel('Consumo ideal', color='r')
plt.show()

 #Carboidratos
   #grafico do dia 06/04/15. Comparacao do consumo diario de energia com o consumo ideal de energia
fig, ax1 = plt.subplots()
t = tmb #escala
ax1.plot(t, 'b-')
ax1.set_xlabel('Consumo de Carboidratos (g)')
ax1.set_ylabel('Consumo do usuario', color='b')

u = imc
 
plt.title ("Gráfico do dia 06/04/15")
ax2 = ax1.twinx()
ax2.plot(u, 'b-')
ax2.set_ylabel('Consumo ideal', color='r')
plt.show()

    #grafico do dia 07/04/15. Comparacao do consumo diario de energia e do consumo ideal
fig, ax1 = plt.subplots()
t = tmb
ax1.plot(t, "b-")
ax1.set_xlabel('Consumo de Carboidratos (g)')
ax1.set_ylabel('Consumo do usuario', color='b')
u = imc
 
plt.title ("Gráfico do dia 07/04/15")
ax2 = ax1.twinx()
ax2.plot(u, 'b-', color='r')
ax2.set_ylabel('Consumo ideal', color='r')
plt.show()


 #Gordura
   #grafico do dia 06/04/15. Comparacao do consumo diario de energia com o consumo ideal de energia
fig, ax1 = plt.subplots()
t = tmb #escala
ax1.plot(t, 'b-')
ax1.set_xlabel('Consumo de Gordura (g)')
ax1.set_ylabel('Consumo do usuario', color='b')

u = imc
 
plt.title ("Gráfico do dia 06/04/15")
ax2 = ax1.twinx()
ax2.plot(u, 'b-')
ax2.set_ylabel('Consumo ideal', color='r')
plt.show()

    #grafico do dia 07/04/15. Comparacao do consumo diario de energia e do consumo ideal
fig, ax1 = plt.subplots()
t = tmb
ax1.plot(t, "b-")
ax1.set_xlabel('Consumo de Gordura (g)')
ax1.set_ylabel('Consumo do usuario', color='b')
u = imc
 
plt.title ("Gráfico do dia 07/04/15")
ax2 = ax1.twinx()
ax2.plot(u, 'b-', color='r')
ax2.set_ylabel('Consumo ideal', color='r')
plt.show()



