# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 19:12:11 2015

@author: Yves Yuzo
"""
# MARZOLA Vamos trabalhar no grafico cada um em arquivos separados para não dar erro de sincronização

from Mini_Projeto_3 import*
        

lista_de_alimentos = criador_info_nutricional (alimentos)
info_usuario_parcial = criador_lista_com_numeros_do_usuario (usuario)
tmb = calcula_tmb (info_usuario_parcial, usuario)
imc = calcula_imc (info_usuario_parcial)

print (tmb)
