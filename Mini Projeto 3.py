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
#Criação de uma lista com a info do usuario
        
usuario_raw = open("usuario.csv", encoding = "cp1252")
leitura2 = usuario_raw.readlines()
usuario = []
for la in leitura2:
    y = la.strip().lower()
    if y != "":
        usuario.append(y)
#--------------------------
def criador_info_usuario (usuario_csv):
    info_usuario = {}
    split_da_linha1 = usuario_csv[1].split(',')
    info_usuario[split_da_linha1[0]] = split_da_linha1[1:]
    
    return info_usuario


print(usuario)


def info_nutricional(lista_de_alimentos_com_info):
    info_nutricional = dict
    for i in range (1,len[lista_de_alimentos_com_info]):
#print (info_nutricional)
        
#def criador_info_nutricional(lista_de_alimentos_com_info):
 #   info_nutricional = {}    
  #  for i in range(1,len(lista_de_alimentos_com_info)):        
   #     split_da_linha = lista_de_alimentos_com_info[i].split(',')
    #    info_nutricional = {split_da_linha[0]: split_da_linha[1:]}
     #   info_nutricional[split_da_linha[0]] = split_da_linha[1:]
        
    #return info_nutricional
        

lista_de_alimentos = criador_info_nutricional (alimentos)
info_usuario = criador_info_usuario (usuario)

print(usuario)
=======
#info_nutricional(alimentos)    
#d = criador_info_nutricional (alimentos)
#print(d['acerola'][3])"""


#-----------

import matplotlib.pyplot as plt


def grafico_do_usuario():
    for i in range(usuario.csv):
        print(usuario.csv(dados))



import numpy as np
import matplotlib.pyplot as plt

#minimo = 0
#baixo = 1:3
#medio = 3:5
#alto = 6:7

def Calcula_cal_usuario(usuario.csv): #calcula a quantidade minima de energia para o organismo
    
    if Sexo == "M"    
        TMB = 88.36 + (13.4*Peso) + ((4.8*Altura)/100) + (5.7*Idade)
    
    else:
        TMB = 447.6 + (9.2*Peso) + ((3.1*Altura)/100) + (4.3*Idade)
        
    return(Calcula_cal_usuario)
    
    
def Calcula_cal_ideal(): #calcula a necessidade energetica e calorica do organismo de acordo com o nivel de atividade fisica

    if Fator == "minimo"
        ideal = TMB*1.2
    
    if Fator == "baixo"
        ideal = TMB*1.375
        
    if Fator == "medio"
        ideal = TMB*1.55
        
    if Fator == "alto"
        ideal = TMB*1.9
    
    return (Calcula_cal_ideal)
    
def Calcula_cal_consumida_usuario(): #calcula o real consumo de energia do usuario baseado na sua alimentação
    
    for i in range (06/04/15):

        u = chave[0]*quantidade + chave[1]*quantiade + chave[2]*quantidade + chave[3]*quantidade
    
    for i in range (07/04/15):
        
        r = chave[0]*quantidade + chave[1]*quantidade + chave[2]*quantidade + chave[3]*quantidade
   
   #Calorias
   #grafico do dia 07/04/15. Comparacao do consumo diario de energia com o consumo ideal de energia
fig, ax1 = plt.subplots()
t = (0.01, 10.0, 0.01) #escala
ax1.plot(t, 'b-')
ax1.set_xlabel('Consumo de Calorias (kcal)')
ax1.set_ylabel('Consumo do usuario', color='b')

 
plt.title ("Gráfico do dia 06/04/15")
ax2 = ax1.twinx()
ax2.plot(t, 'r.')
ax2.set_ylabel('Consumo ideal', color='r')
plt.show()

    #grafico do dia 06/04/15. Comparacao do consumo diario de energia e do consumo ideal
fig, ax1 = plt.subplots()
t = (0.01, 10.0, 0.01) #escala
ax1.plot(t, 'b-')
ax1.set_xlabel('Consumo de Calorias (kcal)')
ax1.set_ylabel('Consumo do usuario', color='b')

 
plt.title ("Gráfico do dia 07/04/15")
ax2 = ax1.twinx()
ax2.plot(t, 'r.')
ax2.set_ylabel('Consumo ideal', color='r')
plt.show()

    #proteinas
#grafico do dia 07/04/15. Comparacao do consumo diario de energia com o consumo ideal de energia
fig, ax1 = plt.subplots()
t = (0.01, 10.0, 0.01) #escala
ax1.plot(t, 'b-')
ax1.set_xlabel('Consumo de Proteínas (g)')
ax1.set_ylabel('Consumo do usuario', color='b')

 
plt.title ("Gráfico do dia 06/04/15")
ax2 = ax1.twinx()
ax2.plot(t, 'r.')
ax2.set_ylabel('Consumo ideal', color='r')
plt.show()

    #grafico do dia 06/04/15. Comparacao do consumo diario de energia e do consumo ideal
fig, ax1 = plt.subplots()
t = (0.01, 10.0, 0.01) #escala
ax1.plot(t, 'b-')
ax1.set_xlabel('Consumo de Proteínas (g)')
ax1.set_ylabel('Consumo do usuario', color='b')

 
plt.title ("Gráfico do dia 07/04/15")
ax2 = ax1.twinx()
ax2.plot(t, 'r.')
ax2.set_ylabel('Consumo ideal', color='r')
plt.show()


    #Carboidratos
#grafico do dia 07/04/15. Comparacao do consumo diario de energia com o consumo ideal de energia
fig, ax1 = plt.subplots()
t = (0.01, 10.0, 0.01) #escala
ax1.plot(t, 'b-')
ax1.set_xlabel('Consumo de Carboidratos (g)')
ax1.set_ylabel('Consumo do usuario', color='b')

 
plt.title ("Gráfico do dia 06/04/15")
ax2 = ax1.twinx()
ax2.plot(t, 'r.')
ax2.set_ylabel('Consumo ideal', color='r')
plt.show()

    #grafico do dia 06/04/15. Comparacao do consumo diario de energia e do consumo ideal
fig, ax1 = plt.subplots()
t = (0.01, 10.0, 0.01) #escala
ax1.plot(t, 'b-')
ax1.set_xlabel('Consumo de Carboidratos (g)')
ax1.set_ylabel('Consumo do usuario', color='b')

 
plt.title ("Gráfico do dia 07/04/15")
ax2 = ax1.twinx()
ax2.plot(t, 'r.')
ax2.set_ylabel('Consumo ideal', color='r')
plt.show()


    #gordura
#grafico do dia 07/04/15. Comparacao do consumo diario de energia com o consumo ideal de energia
fig, ax1 = plt.subplots()
t = (0.01, 10.0, 0.01) #escala
ax1.plot(t, 'b-')
ax1.set_xlabel('Consumo de Gordura (g)')
ax1.set_ylabel('Consumo do usuario', color='b')

 
plt.title ("Gráfico do dia 06/04/15")
ax2 = ax1.twinx()
ax2.plot(t, 'r.')
ax2.set_ylabel('Consumo ideal', color='r')
plt.show()

    #grafico do dia 06/04/15. Comparacao do consumo diario de energia e do consumo ideal
fig, ax1 = plt.subplots()
t = (0.01, 10.0, 0.01) #escala
ax1.plot(t, 'b-')
ax1.set_xlabel('Consumo de Gordura (g)')
ax1.set_ylabel('Consumo do usuario', color='b')

 
plt.title ("Gráfico do dia 07/04/15")
ax2 = ax1.twinx()
ax2.plot(t, 'r.')
ax2.set_ylabel('Consumo ideal', color='r')
plt.show()

