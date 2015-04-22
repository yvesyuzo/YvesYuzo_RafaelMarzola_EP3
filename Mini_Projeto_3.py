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
        
usuario_teste_raw = open("usuario_teste.csv")
leitura3 = usuario_teste_raw.readlines()
usuario_teste = []
for la in leitura3:
    z = la.strip().lower()
    if z != "":
        usuario_teste.append(z)
#--------------------------
        
    
def criador_lista_com_numeros_do_usuario (usuario_csv):
    
    #função que RETORNA uma lista com 'floats' do PESO(kg), ALTURA(m) e Idade(anos) do usuario
    #Entradas: arquivo do excel com info do usuario
    
    info_usuario_total = usuario_csv[1].split(',')    
    info_usuario_parcial = []
    
#adiciona apenas os dados numericos do usuario a uma segunda lista    
    info_usuario_parcial.append(info_usuario_total[1])
    info_usuario_parcial.append(info_usuario_total[2])
    info_usuario_parcial.append(info_usuario_total[4])
    
#transforma a segunda lista em float para realizar as operações
    info_usuario_parcial = [float(i) for i in info_usuario_parcial]
    
    return info_usuario_parcial

def calcula_tmb (info_usuario_parcial, usuario_csv):
    
    #ENTRADAS:
    #info_usuario_parcial: lista 'floats' da Idade(anos), PESO(kg) e ALTURA(m) do usuario
    #usuario-csv: lista com todas as informações do usuario presentes no Excel
    
    info_usuario_total = usuario_csv[1].split(',')
    tmb = float
    
    
    #Calcula as necessidades caloricas ideais para o corpo manter o seu peso com 
#   a fórmula de Harris-Benedict (TMB)
    
    peso = info_usuario_parcial[1]
    altura = info_usuario_parcial[2] * 100 #transformada em "cm"
    idade = info_usuario_parcial[0]
    
    if 'm' in info_usuario_total:
    #Para homens TMB = 88,36 + (13,4 x peso, kg) + (4,8 x altura, cm) - (5,7 x idade em anos)

        tmb = 88.36 + peso * 13.4 + 4.8 * altura - 5.7 * idade    
    
    if 'f' in info_usuario_total:
    #Para mulheres TMB = 447,6 + (9.2 x peso, kg) + (3,1 x altura, cm) - (4,3 x idade em anos)

        tmb = 447.6 + 9.2 * peso + 3.1 * altura - 4.3 * idade
    # multiplica o fator de atividade física ao "tmb" caso seja diferente de "mínimo"
    if 'baixo' in info_usuario_total:        
        tmb = tmb * 1.375
    if 'médio' in info_usuario_total:
        tmb = tmb * 1.55
    if 'alto' in info_usuario_total:
        tmb = tmb * 1.725
    if 'muito alto' in info_usuario_total:
        tmb = tmb * 1,9        
    
    return tmb
    
def calcula_imc (info_usuario_parcial):
    
    #Função que calcula o IMC com a fórmula de Nick Trefethen: peso(kg)/altura(m)^2
    #ENTRADAS: lista com informações do usuario na ordem: IDADE(anos), PESO(kg), ALTURA(m)
    imc = info_usuario_parcial[1]/info_usuario_parcial[2]**2
    return imc



def criador_info_nutricional(lista_de_alimentos_com_info):
    info_nutricional = {}    
    for i in range(1,len(lista_de_alimentos_com_info)):        
        split_da_linha = lista_de_alimentos_com_info[i].split(',')
        info_nutricional[split_da_linha[0]] = split_da_linha[1:]
    return info_nutricional


def intervalo_de_tempo_do_usuario (usuario_csv):
    datas = []
    for i in range (3, len(usuario_csv)):
        split_da_linha = usuario_csv[i].split(',')
        if split_da_linha[0] not in datas:
            datas.append(split_da_linha[0])
        else:
            pass
    datas.sort()
    return datas
        
    
