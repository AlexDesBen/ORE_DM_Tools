#*-* coding: utf-8*-*
'''
################################################################################
################################################################################
Author : 
Date : 
Company : ProximityHCI
Name of module : 
Version : 
Description : 
################################################################################
################################################################################
'''

#import numpy as np
#import matplotlib.pyplot as plt
import random as rand
from Character import *


####################################################################################################
####################################################################################################
def perso_def():
    print("\ntest define of Extras, NPCs and Players")
    try:
        Name,Body,Coord,Sense,Mind,Charm,Command = "Bob",1,2,3,4,5,6
        Allied,Nbr,Rate,Acti = True,7,8,True
        Bob = Extra(Name,Body,Coord,Sense,Mind,Charm,Command,Allied,Nbr,Rate,Acti,XTough = False)
        if Bob.Name != Name:1/0
        if Bob.Body != Body:1/0
        if Bob.Coordination != Coord:1/0
        if Bob.Sense != Sense:1/0
        if Bob.Mind != Mind:1/0
        if Bob.Charm != Charm:1/0
        if Bob.Command != Command:1/0
        if Bob.Allied != Allied:1/0
        if Bob.Nbr != Nbr:1/0
        if Bob.Rating != Rate:1/0
        if Bob.Active != Acti:1/0
        if Bob.Life != True:1/0
        Bob = Extra(Name,Body,Coord,Sense,Mind,Charm,Command,Allied,Nbr,Rate,Acti,XTough = 4)
        Bob = Extra(Name,Body,Coord,Sense,Mind,Charm,Command,Allied,Nbr,Rate,Acti,XTough = [0,0,0,0,5,0])
        #Bob.get_info()
        Bob = NPC(Name,Body,Coord,Sense,Mind,Charm,Command,Allied,Acti,XTough = False)
        if Bob.Name != Name:1/0
        if Bob.Body != Body:1/0
        if Bob.Coordination != Coord:1/0
        if Bob.Sense != Sense:1/0
        if Bob.Mind != Mind:1/0
        if Bob.Charm != Charm:1/0
        if Bob.Command != Command:1/0
        if Bob.Allied != Allied:1/0
        if Bob.Active != Acti:1/0
        if Bob.Life != True:1/0
        Bob = NPC(Name,Body,Coord,Sense,Mind,Charm,Command,Allied,Acti,XTough = 4)
        Bob = NPC(Name,Body,Coord,Sense,Mind,Charm,Command,Allied,Acti,XTough = [0,0,0,0,5,0])
        #Bob.get_info()
        Bob = Player(Name,Sense,Acti)
        if Bob.Name != Name:1/0
        if Bob.Sense != Sense:1/0
        if Bob.Active != Acti:1/0
        if Bob.Life != True:1/0
        #Bob.get_info()
        print("########## Success to define Characters ##########\n")
    except:
        print("########## failed to load Characters ##########\n")
####################################################################################################
####################################################################################################
def rolls():
    print("\ntest rolls")
    try:
        for i in range(0,100):
            Name,Body,Coord,Sense,Mind,Charm,Command = "Bob",1,2,3,4,5,6
            Allied,Nbr,Rate,Acti = True,7,8,True
            Bob = Extra(Name,Body,Coord,Sense,Mind,Charm,Command,Allied,Nbr,Rate,Acti,XTough = False)
            Bob.Roll()
            if (sum(Bob.Rolled) == sum(Bob.Pool)) or ((sum(Bob.Pool)>10) and (sum(Bob.Rolled) == 10)):1+1
            else:1/0
            Bob = NPC(Name,Body,Coord,Sense,Mind,Charm,Command,Allied,Acti,XTough = False)
            Bob.Pool[0] = rand.randint(0,10)
            Bob.Pool[1] = rand.randint(0,10)
            Bob.Roll()
            if (sum(Bob.Rolled) == sum(Bob.Pool)) or ((sum(Bob.Pool)>10) and (sum(Bob.Rolled) == 10)):1+1
            else:1/0
            Bob.Pool[0] = 0
            Bob.Pool[1] = rand.randint(0,10)
            Bob.Roll()
            if (sum(Bob.Rolled) == sum(Bob.Pool)) or ((sum(Bob.Pool)>10) and (sum(Bob.Rolled) == 10)):1+1
            else:1/0
            if Bob.Rolled[9] != Bob.Pool[1]:1/0
        print("########## Success to Roll ##########\n")
    except:
        print("########## failed to Roll ##########\n")
####################################################################################################
####################################################################################################
def damage():
    print("\ntest damage")
    try:
        Name,Body,Coord,Sense,Mind,Charm,Command = "Bob",1,2,3,4,5,6
        Allied,Nbr,Rate,Acti = True,7,10,True
        permut = [[i,j,k] for i in range(1,10) for j in range(0,10-i) for k in range(1,11)]
        #Extra with no armor
        for cas in permut:
            Bob = Extra(Name,Body,Coord,Sense,Mind,Charm,Command,Allied,Nbr,Rate,Acti,XTough = False)
            S,K,Loc = cas
            Pierced,Engulf,Burn,Electrocute=False,False,False,False
            Bob.LAR = [0,0]
            Bob.MAR = [0,0]
            Bob.Rolled[9] = 2
            Bob.Rolled[8] = 1
            Bob.Rolled[7] = 2
            Bob.Damaged(S,K,Loc)
            if (Bob.HP != Bob.MaxHP-(S+K)):1/0
            if (Bob.Rolled[9] != 1):1/0
            Bob.HP = Bob.MaxHP
            Bob.Damaged(10,0,10)
            if (Bob.HP != Bob.MaxHP):1/0
            if (Bob.Rolled[7] != 1):1/0
        print("########## Success to damage ##########\n")
    except:
        print("########## failed to damage ##########\n")
####################################################################################################
####################################################################################################













####################################################################################################
####################################################################################################
def Template():
    print("\ntest Template")
    try:
        for i in range(0,100):
            1+1
        print("########## Success to Template ##########\n")
    except:
        print("########## failed to Template ##########\n")
####################################################################################################
####################################################################################################



