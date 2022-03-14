#!/usr/bin/env python
# coding: utf-8

# In[42]:


import random

# Projeto01 - pedra, papel, tesoura

lista=['pedra', 'papel', 'tesoura']
contwilson=0
contpc=0
jogarnovamente=str()

while jogarnovamente !='nao':

    eu = input('\nFaça sua jogada, escolha: pedra ou papel ou tesoura:')

    while eu!= 'pedra' and eu!='papel' and eu!='tesoura':
        eu = input('\nFaça sua jogada, escolha: pedra ou papel ou tesoura:')

    else:
        pass

    computador = random.choice(lista)

    if eu=='pedra'and computador=='tesoura':
        print('O Computador jogou: %s' %computador)
        print('Wilson ganhou')
        contwilson=contwilson+1
    elif eu=='tesoura'and computador=='papel':
        print('O Computador jogou: %s' %computador)
        print('Wilson ganhou')
        contwilson=contwilson+1
    elif eu=='papel'and computador=='pedra':
        print('O Computador jogou: %s' %computador)
        print('Wilson ganhou')
        contwilson=contwilson+1
    elif eu=='tesoura'and computador=='tesoura':
        print('O Computador jogou: %s' %computador)
        print('Empate')
    elif eu=='papel'and computador=='papel':
        print('O Computador jogou: %s' %computador)
        print('Empate')
    elif eu=='pedra'and computador=='pedra':
        print('O Computador jogou: %s' %computador)
        print('Empate')
    else:
        print('O Computador jogou: %s' %computador)
        print('\nComputador ganhou')
        contpc=contpc+1

    print('\nPlacar Atualizado: Wilson %s | %s Computador' %(contwilson,contpc))
    
    jogarnovamente=input('Jogar novamente? [sim] ou [nao]: ')


# In[ ]:




