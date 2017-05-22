#*-* coding: utf-8 *-*
####################################################################################################
####################################################################################################
#                              %
# Author      : Alexandre Desilets-Benoit, Ph.D. Phys.
# Institution : None
# Group       : 
# Year        : 2017
# Version     : 0.2
# function    : to fill
#
####################################################################################################
####################################################################################################

import math
import random as rand
import csv
from copy import deepcopy

from TallyAlgorithm import *
from SortAlgorithm import *

class Extra():
    def __init__(self,Name,Body,Coordination,Sense,Mind,Charm,Command,Allied,Nbr,Rating,Active,XTough=False):
        self.Life = True
        self.Active = Active
        self.Nbr = Nbr
        self.Rating = Rating
        self.Allied = Allied
        self.Name = Name
        self.Body = Body
        self.Coordination = Coordination
        self.Sense = Sense
        self.Mind = Mind
        self.Charm = Charm
        self.Command = Command
        self.MaxHP = self.Rating
        self.HP = self.Rating
        #LAR = Reduce S to 1 and Convert K -> S
        #Example :LAR 2 on (4S + 3K) = (3S + 1K)
        #MAR = Substract MAR from S and K
        #Example : MAR 2 on (4S + 3K) = (2S + 1K)
        #With both LAR and MAR always apply MAR first and LAR second
        #Example : LAR 2 and MAR 2 on (10S + 10K) = (-MAR) = (8S + 8K) = (-LAR) = (3S + 6K)
        #NOT CORRECT : LAR 2 and MAR 2 on (10S + 10K) = (-LAR) = (3S + 8K) = (-MAR) = (1S + 6K)
        #Natural armor is not pierced or penetrated
        self.LAR = [0,0] #[natural, artificial]
        self.MAR = [0,0] #[natural, artificial]
        self.Nature = 'Extra' #nature
        self.Daze = False
        self.Penalities = 0
        self.Burning = False
        self.Pool = [self.Nbr*self.Rating,0,0]
        self.WD_to_set = self.Pool[2]
        self.Damage = [True,False] #[Shock, Killing]
        self.Atk = 0
        self.Speed = 0
        self.Penetration = 0
        self.Defence = None
        self.Rolled = [0,0,0,0,0,0,0,0,0,0]
    def get_info(self):
        print "%12s : "%("Life"),self.Life
        print "%12s : "%("Active"),self.Active
        print "%12s : "%("Nbr"),self.Nbr
        print "%12s : "%("Rating"),self.Rating
        print "%12s : "%("Allied"),self.Allied
        print "%12s : "%("Name"),self.Name
        print "%12s : "%("Body"),self.Body
        print "%12s : "%("Coordination"),self.Coordination
        print "%12s : "%("Sense"),self.Sense
        print "%12s : "%("Mind"),self.Mind
        print "%12s : "%("Charm"),self.Charm
        print "%12s : "%("Command"),self.Command
        print "%12s : "%("MaxHP"),self.MaxHP
        print "%12s : "%("HP"),self.HP
        print "%12s : "%("LAR"),self.LAR
        print "%12s : "%("MAR"),self.MAR
        print "%12s : "%("Nature"),self.Nature
        print "%12s : "%("Daze"),self.Daze
        print "%12s : "%("Penalities"),self.Penalities
        print "%12s : "%("Burning"),self.Burning
        print "%12s : "%("Pool"),self.Pool
        print "%12s : "%("WD_to_set"),self.WD_to_set
        print "%12s : "%("Damage"),self.Damage
        print "%12s : "%("Atk"),self.Atk
        print "%12s : "%("Speed"),self.Speed
        print "%12s : "%("Penetration"),self.Penetration
        print "%12s : "%("Defence"),self.Defence
        print "%12s : "%("Rolled"),self.Rolled
    def Heal(self,Healing,Loc,Engulf=False):
        ToHeal = max(Healing)
        if Engulf:
            ToHeal = 6*Healing
        if (self.HP + ToHeal) >= self.Rating:
            self.HP = self.Rating
        else:
            self.HP = self.HP + ToHeal
    def Deal_Damage(self,Damage):
        while (Damage > 0) and self.Life:
            if self.HP > Damage:
                print("HP is bigger")
                self.HP = self.HP - Damage
                Damage = 0
            elif self.HP == Damage:
                print("HP is equal")
                self.Nbr = self.Nbr -1
                Damage = 0
                if self.Nbr == 0:
                    self.Killed()
            else:
                print("HP is lower")
                Damage = Damage-self.HP
                self.Nbr = self.Nbr - 1
                if self.Nbr == 0:
                    self.Killed()
                else:
                    self.HP = self.Rating
    def Damaged(self,S,K,Loc,Pierced=False,Engulf=False,Burn=False,Electrocute=False):
        ToDeal = [S,K]
        if Pierced == False:
            LAR = sum(self.LAR)
            MAR = sum(self.MAR)
            ToDeal = [ToDeal[0] - MAR,ToDeal[1]-MAR]
            for i in range(0,2):
                if ToDeal[i] < 0:ToDeal[i] = 0
            if (ToDeal[0] > 0) and (LAR != 0):
                ToDeal[0] = 1
            if (LAR > ToDeal[1]):
                ToDeal[0] += ToDeal[1]
                ToDeal[1] = 0
            else:
                ToDeal[0] += LAR
                ToDeal[1] = ToDeal[1] - LAR
        elif (Pierced == True) and (type(Pierced) == type(True)):
            print(type(Pierced))
            LAR = self.LAR[0]
            MAR = self.MAR[0]
            ToDeal = [ToDeal[0] - MAR,ToDeal[1]-MAR]
            for i in range(0,2):
                if ToDeal[i] < 0:ToDeal[i] = 0
            if (ToDeal[0] > 0) and (LAR != 0):
                ToDeal[0] = 1
            if (LAR > ToDeal[1]):
                ToDeal[0] += ToDeal[1]
                ToDeal[1] = 0
            else:
                ToDeal[0] += LAR
                ToDeal[1] = ToDeal[1] - LAR
        else:
            LAR = self.LAR[0]
            LAR += max([0,self.LAR[1] - Pierced])
            MAR = self.MAR[0]
            MAR += max([0,self.MAR[1] - Pierced])
            ToDeal = [ToDeal[0] - MAR,ToDeal[1]-MAR]
            for i in range(0,2):
                if ToDeal[i] < 0:ToDeal[i] = 0
            if (ToDeal[0] > 0) and (LAR != 0):
                ToDeal[0] = 1
            if (LAR > ToDeal[1]):
                ToDeal[0] += ToDeal[1]
                ToDeal[1] = 0
            else:
                ToDeal[0] += LAR
                ToDeal[1] = ToDeal[1] - LAR
        if Engulf:
            if sum(ToDeal) > 0:self.ReduceRoll()
            self.Deal_Damage(self.Nbr*sum(ToDeal))
        elif Electrocute:
            if sum(ToDeal) > 0:self.ReduceRoll()
            if Loc in [10,6,5,4,3]:
                self.Deal_Damage(3*sum(ToDeal))
            elif Loc in [7,8,9]:
                self.Deal_Damage(2*sum(ToDeal))
            else:
                self.Deal_Damage(sum(ToDeal))
        else:
            if sum(ToDeal) > 0:self.ReduceRoll()
            self.Deal_Damage(sum(ToDeal))
        if (self.Nbr <= 0) and (self.HP <= 0):
            self.Killed()
        if Burn != False:
            self.Burned = True
            self.Penalities = Burn
    def Killed(self):
        self.Life = False
        self.Active = False
        self.Pool = [0,0,0]
        self.HP = 0
    def Roll(self):
        wd = self.Pool[2]
	hd = self.Pool[1]
	if sum(self.Pool) <= 10:
	    d = self.Pool[0]
	else:
	    d = max((0,10-hd-wd))
	Reste = max((0,10-d-wd))
	if Reste < hd:
	    hd = Reste
	Pool = [rand.randint(1,10) for i in range(0,d)]
	Pool.sort()
	self.Rolled = Tally(Pool)
	self.Rolled[9] += hd
	self.WD_to_set = min((10,self.Pool[2]))
    def ReduceRoll(self):
	ToReduce = True
	i = 9
	while ToReduce:
	    if self.Rolled[i]>1:
		self.Rolled[i]-=1
		ToReduce = False
	    i-=1
	    if i == -1:
		ToReduce = False
################################################################################
################################################################################
class NPC(Extra):
    def __init__(self,Name,Body,Coordination,Sense,Mind,Charm,Command,Allied,Active,XTough=False):
        Extra.__init__(self,Name,Body,Coordination,Sense,Mind,Charm,Command,Allied,1,1,Active,XTough=XTough)
        self.MaxHP = [5,5,5,5,10,4] #[L-leg, R-leg, L-arm, R-arm, Torso, Head]]
        self.HP = [5,5,5,5,10,4] #[L-leg, R-leg, L-arm, R-arm, Torso, Head]]
        if XTough != False:
            if type(XTough) == int:
                for i in range(0,6):
                    self.HP[i] += XTough
                    self.MaxHP[i] += XTough
            elif (type(XTough) == type([])) and (len(XTough) == 6):
                for i in range(0,6):
                    self.HP[i] += XTough[i]
                    self.MaxHP[i] += XTough[i]
        self.LAR = [0,0] #[natural, artificial]
        self.MAR = [0,0] #[natural, artificial]
        self.Nature = 'NPC' #nature
        self.Pool = [0,0,0] #[Normal dice, Hard dice, Wiggle dice]
    def get_info(self):
        print "%12s : "%("Life"),self.Life
        print "%12s : "%("Active"),self.Active
        print "%12s : "%("Nbr"),self.Nbr
        print "%12s : "%("Rating"),self.Rating
        print "%12s : "%("Allied"),self.Allied
        print "%12s : "%("Name"),self.Name
        print "%12s : "%("Body"),self.Body
        print "%12s : "%("Coordination"),self.Coordination
        print "%12s : "%("Sense"),self.Sense
        print "%12s : "%("Mind"),self.Mind
        print "%12s : "%("Charm"),self.Charm
        print "%12s : "%("Command"),self.Command
        print "%12s : "%("MaxHP"),self.MaxHP
        print "%12s : "%("HP"),self.HP
        print "%12s : "%("LAR"),self.LAR
        print "%12s : "%("MAR"),self.MAR
        print "%12s : "%("Nature"),self.Nature
        print "%12s : "%("Daze"),self.Daze
        print "%12s : "%("Penalities"),self.Penalities
        print "%12s : "%("Burning"),self.Burning
        print "%12s : "%("Pool"),self.Pool
        print "%12s : "%("WD_to_set"),self.WD_to_set
        print "%12s : "%("Damage"),self.Damage
        print "%12s : "%("Atk"),self.Atk
        print "%12s : "%("Speed"),self.Speed
        print "%12s : "%("Penetration"),self.Penetration
        print "%12s : "%("Defence"),self.Defence
        print "%12s : "%("Rolled"),self.Rolled
    def Heal(self,Healing,Loc,Engulf=False):
        ToHeal = max(Healing)
        if Engulf:
            for i in [0,1,2,3,4,5]:
                if (self.HP[i] + ToHeal) >= self.MaxHP[i]:
                    self.HP[i] = self.MaxHP[i]
                else:
                    self.HP[i] = self.HP[i] + ToHeal
        else:
            if Loc in [1,2]:
                RealLoc = Loc-1
            elif Loc in [3,4]:
                RealLoc = 2
            elif Loc in [5,6]:
                RealLoc = 3
            elif Loc in [7,8,9]:
                RealLoc = 4
            else:
                RealLoc = 5
            if (self.HP[RealLoc] + ToHeal) >= self.MaxHP[RealLoc]:
                self.HP[RealLoc] = self.MaxHP[RealLoc]
            else:
                self.HP[RealLoc] = self.HP[RealLoc] + ToHeal
    def Deal_Damage(self,ToDeal,Loc):
        Damage = deepcopy(ToDeal)
        print("In deal_damage : ",Damage)
        RealLoc = None
        if Loc in [1,2]:
            RealLoc = Loc-1
        elif Loc in [3,4]:
            RealLoc = 2
        elif Loc in [5,6]:
            RealLoc = 3
        elif Loc in [7,8,9]:
            RealLoc = 4
        else:
            RealLoc = 5
        if RealLoc in [0,1,2,3]:
            if self.HP[RealLoc] == 0:
                RealLoc = 4
            if Damage[0] < self.HP[RealLoc]:
                self.HP[RealLoc] = self.HP[RealLoc] - Damage[0]
                Damage[0] = 0
                if Damage[1] < self.HP[RealLoc]:
                    self.HP[RealLoc] = self.HP[RealLoc] - Damage[1]
                    Damage[1] = 0
                else:
                    Damage[1] = Damage[1] - self.HP[RealLoc]
                    self.HP[RealLoc] = 0
                    RealLoc = 4
            else:
                Damage[0] = Damage[0] - self.HP[RealLoc]
                self.HP[RealLoc] = 0
                RealLoc = 4
        if RealLoc == 4:
            if self.HP[RealLoc] == 0:
                RealLoc = 5
            if Damage[0] < self.HP[RealLoc]:
                self.HP[RealLoc] = self.HP[RealLoc] - Damage[0]
                Damage[0] = 0
                if Damage[1] < self.HP[RealLoc]:
                    self.HP[RealLoc] = self.HP[RealLoc] - Damage[1]
                    Damage[1] = 0
                else:
                    Damage[1] = Damage[1] - self.HP[RealLoc]
                    self.HP[RealLoc] = 0
                    RealLoc = 5
            else:
                Damage[0] = Damage[0] - self.HP[RealLoc]
                self.HP[RealLoc] = 0
                RealLoc = 5
        if RealLoc == 5:
            if self.HP[RealLoc] == 0:
                self.Killed()
            if Damage[0] < self.HP[RealLoc]:
                self.HP[RealLoc] = self.HP[RealLoc] - Damage[0]
                Damage[0] = 0
                if Damage[1] < self.HP[RealLoc]:
                    self.HP[RealLoc] = self.HP[RealLoc] - Damage[1]
                    Damage[1] = 0
                else:
                    Damage[1] = Damage[1] - self.HP[RealLoc]
                    self.HP[RealLoc] = 0
                    self.Killed()
            else:
                Damage[0] = Damage[0] - self.HP[RealLoc]
                self.HP[RealLoc] = 0
                self.Killed()
        if self.HP[5] <= 0:
            self.Killed()
    def Damaged(self,S,K,Loc,Pierced=False,Engulf=False,Burn=False,Electrocute=False):
        ToDeal = [S,K]
        if Pierced == False:
            LAR = sum(self.LAR)
            MAR = sum(self.MAR)
            ToDeal = [ToDeal[0] - MAR,ToDeal[1]-MAR]
            for i in range(0,2):
                if ToDeal[i] < 0:ToDeal[i] = 0
            if (ToDeal[0] > 0) and (LAR != 0):
                ToDeal[0] = 1
            if (LAR > ToDeal[1]):
                ToDeal[0] += ToDeal[1]
                ToDeal[1] = 0
            else:
                ToDeal[0] += LAR
                ToDeal[1] = ToDeal[1] - LAR
        elif (Pierced == True) and (type(Pierced) == type(True)):
            LAR = self.LAR[0]
            MAR = self.MAR[0]
            ToDeal = [ToDeal[0] - MAR,ToDeal[1]-MAR]
            for i in range(0,2):
                if ToDeal[i] < 0:ToDeal[i] = 0
            if (ToDeal[0] > 0) and (LAR != 0):
                ToDeal[0] = 1
            if (LAR > ToDeal[1]):
                ToDeal[0] += ToDeal[1]
                ToDeal[1] = 0
            else:
                ToDeal[0] += LAR
                ToDeal[1] = ToDeal[1] - LAR
        else:
            LAR = self.LAR[0]
            LAR += max([0,self.LAR[1] - Pierced])
            MAR = self.MAR[0]
            MAR += max([0,self.MAR[1] - Pierced])
            ToDeal = [ToDeal[0] - MAR,ToDeal[1]-MAR]
            for i in range(0,2):
                if ToDeal[i] < 0:ToDeal[i] = 0
            if (ToDeal[0] > 0) and (LAR != 0):
                ToDeal[0] = 1
            if (LAR > ToDeal[1]):
                ToDeal[0] += ToDeal[1]
                ToDeal[1] = 0
            else:
                ToDeal[0] += LAR
                ToDeal[1] = ToDeal[1] - LAR
        if Engulf:
            if sum(ToDeal) > 0:self.ReduceRoll()
            for i in [1,2,3,5,8,10]:
                self.Deal_Damage(ToDeal,i)
        elif Electrocute:
            if sum(ToDeal) > 0:self.ReduceRoll()
            if Loc in [3,4,5,6,10]:
                self.Deal_Damage(ToDeal,Loc)
                self.Deal_Damage(ToDeal,8)
		LR = rand.randint(1,2)
                self.Deal_Damage(ToDeal,LR)
            elif Loc in [7,8,9]:
                self.Deal_Damage(ToDeal,Loc)
		LR = rand.randint(1,2)
                self.Deal_Damage(ToDeal,LR)
            else:
                self.Deal_Damage(ToDeal,Loc)
        else:
            if sum(ToDeal) > 0:self.ReduceRoll()
            self.Deal_Damage(ToDeal,Loc)
        if Burn != False:
            self.Burned = True
            self.Penalities = Burn
    def Killed(self):
        self.Life = False
        self.Active = False
        self.Pool = [0,0,0]
        self.Nbr = 0
        for i in range(0,6):
            if self.HP[i] < 0:
                self.HP[i] = 0
################################################################################
################################################################################
class Player(NPC):
    def __init__(self,Name,Sense,Active):
        NPC.__init__(self,Name,0,0,Sense,0,0,0,True,Active)
        self.Nature = "Player"
################################################################################
################################################################################


