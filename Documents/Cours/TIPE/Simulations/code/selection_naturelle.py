#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 24 21:35:50 2017

@author: Tregoat Johanne
"""

from random import *
import numpy as np

'''stratégies'''

def naif(p,L,a):  #0 pour coopérer, argument muet
    return(0)

def traitre(p,L,a):  #1 pour trahir,  argument muet
    return(1)

def rancunnier(p,L,a):  #L est l'historique des jeux,  p muet
    for k in range (len(L)): 
        if L[k][0]==1:
            return(1)  #S'il a été trahit une fois, il trahit tout le temps
    return(0)


def lunatique(p,L,a):  #p : probabilité de coopérer (en %), à 2 chiffres, L et a muets
    a=randrange(0,100)
    if a<p:
        return(0)
    return(1)


def donnant_donnant(p,L,a):  #L, historique des jeux, p muet, a=1 si J1, a=0 si J2 ( colonne à copier )
    if len(L)==0:
        return(0)
    return(L[len(L)-1][a])


def per_cct(p,L,a):  #p et a muets
    if len(L)%3==0:
        return(1)
    return(0)


def per_ttc(p,L,a):  #p et a muets
    if len(L)%3==0:
        return(0)
    return(1)


'''programmes annexes'''

def regles():  #choisi 4 gains différents et les classe
    a=randrange(0,8)
    b=randrange(a+1,9)
    c=randrange(b+1,10)
    d=randrange(c+1,11)  
    return([a,b,c,d])

def Gain(L,regle):  #détermine les gains en fonction de la partie jouée pour le J1. cf tableau
    if L[0]==L[1]:
        if L[0]==0:
            return(regle[2])
        return(regle[1])
    elif L[0]==0 and L[1]==1:
        return(regle[0])
    else:
        return(regle[3])  
    

'''Tri des stratégies en fonction des gains'''

def Max(L):  #renvoie l'indice du plus grand élément de la liste
    maxi=L[0][1]
    indice=0
    for k in range(len(L)-1): 
        if ( L[k+1][1] > maxi ) :
            indice=k+1  # k+1 - permet d'éviter de le tester contre lui-même
    return(indice)        
            
def tri(L):  # du meilleur au moins bon
    M=[]
    while len(L)!=0:
        M.append(L[Max(L)])
        L.pop(Max(L))
    return(M)

def somme(L):
    S=0
    for k in range(len(L)):
        S+=L[k][1]
    return(S)


'''Pour une partie'''

def DPI(s,p):  # s= nombre de parties jouées contre une stratégie, p : proba pour lunatique
    regle=regles() #une règle pour tous les combats pour pouvoir comparer
    L=[naif,traitre,rancunnier,lunatique,donnant_donnant,per_cct,per_ttc]
    M=['naif','traitre','rancunnier','lunatique','donnant_donnant','per_cct','per_ttc']
    gains=[]  #liste des gains des différentes stratégies
    for k in range(len(L)): #choix de la stratégie du 1er joueur, dont les gains nous intéresse.
        g=0  #gain de la stratégie k, tous combats confondu
        for i in range(len(L)): #choix de la stratégie du 2ème joueur, chaque stratégie affronte toutes les autres.
            jeu = np.zeros(s)
            for j in range(s):  # s combat entre les deux stratégies choisie
                jeu[j] = [L[k](p, jeu,1),L[i](p,jeu,0)]
                g[j] = Gain(jeu[j], regle)
        gains.append([M[k],g])
        #gains=tri(gains) à ne pas mettre pour l'arène
    return(gains)
        

'''codage de la mise en compétition des stratégies, méthode de la sélection naturelle'''

def arene(e,n,s,p):  
    """
    Etudie la variation de population d'une strategie au cours d'un test.
    
    e : effectif total
    
    n : nombre de générations étudiées
    
    s : nombre de parties jouees contre une strategie
    
    p : probabilite qu'une strategie aleatoire / lunatique coopere
    """
    L = [naif, traitre, rancunnier, lunatique, donnant_donnant, 
         per_cct,per_ttc]
    pop = np.zeros([len(L), n]) 
    pop[0, :] = int(e/len(L))
    generation = np.linspace(0, n-1, num=n)
    
    
    
    pop = [[int(e/len(L))] for k in range(len(L))]  #même population initiale pour chaque stratégie
    generation = np.linspace(0, n-1, num=n)
    
    for k in range(n-1):  # k° génération, n-1 car on a initialisé et on veut n génération
        gain = DPI(s,p)
        S = 0
        for i in range(len(L)):  #cf formule de calcul de la j° population
            S += pop[k, i] * gain[i][1]
        for j in range(len(L)):  #j° population, calcul de la population de la k+1° génération
            M = pop[j]  #liste muette
            M.insert(k+1,int(pop[k, j]*e*gain[j][1]/S))  #pas de retouche sur L, modifiée avec M
    return generation, pop 



