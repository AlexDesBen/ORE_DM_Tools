#*-* coding: utf-8 *-*
####################################################################################################
####################################################################################################
#                              %
# Author      : Alexandre Desilets-Benoit, Ph.D. Phys.
# Institution : Université de Montréal
# Group       : 
# Year        : 2015
# Version     : 0.1
# function    : to fill
#
####################################################################################################
####################################################################################################

import math
import random as rand
import csv

from ClassExtra import *
from ClassHitLocation import *
from TallyAlgorithm import *
from SortAlgorithm import *

class Perso():
	def __init__(self, Nature, Name, Sense, XTough, NatLAR, LAR,NatMAR,MAR,Nbr):
		self.Name = Name
		self.Sense = Sense
		self.Allied = 0
		self.HP = HitLocations(XTough)
		self.Nbr = min((1,Nbr))
		self.Alive = self.Nbr
		self.Order = 0
		if Nature == 1:
			self.Nature = "NPC"
		elif Nature == 0:
			self.Nature = "Char"
		
		self.NatLAR = NatLAR
		self.LAR = LAR
		self.NatMAR = NatMAR
		self.MAR = MAR
		
		self.Dazed = 0
		self.Burning = 0
		self.Pool = [0,0,0]
		self.WD = min((10,self.Pool[2]))
		self.Atk = 'S'
		self.AtkBonus = 0
		self.SpeedBonus = 0
		self.Penetration = 0
		self.Defence = 0
		self.InstantDefence = 0
		self.InstantWiggle = 0
		
		self.Rolled = [0,0,0,0,0,0,0,0,0,0]
	def Damaged(self,S,K,Loc,Pierced=None,Engulf = None,Burn = None):
		Loss = 0
		if Engulf == None and Burn == None:
			if Pierced == None:
				#Loss = max((0,S - self.NatLAR - self.LAR)) + max((0,K - self.NatMAR - self.MAR))
				Loss = (self.HP.Head + self.HP.Torso + self.HP.Rarm + self.HP.Larm + self.HP.Rleg + self.HP.Lleg)
				self.HP.DealDamage(S,K,Loc,self.NatLAR+self.LAR,self.NatMAR + self.MAR)
				Loss -= (self.HP.Head + self.HP.Torso + self.HP.Rarm + self.HP.Larm + self.HP.Rleg + self.HP.Lleg)
			else:
				Loss = (self.HP.Head + self.HP.Torso + self.HP.Rarm + self.HP.Larm + self.HP.Rleg + self.HP.Lleg)
				LAR = self.LAR - Pierced
				if LAR < 0:
					LAR = 0
				MAR = self.MAR - Pierced
				if MAR < 0:
					MAR = 0
				#Loss = max((0,S - self.NatLAR - LAR)) + max((0,K - self.NatMAR - MAR))
				self.HP.DealDamage(S,K,Loc,self.NatLAR + LAR,self.NatMAR + MAR)
				Loss -= (self.HP.Head + self.HP.Torso + self.HP.Rarm + self.HP.Larm + self.HP.Rleg + self.HP.Lleg)
			if self.HP.Lives == 0:
				self.Alive = 0
				self.Nbr = 0
			if Loss > 0:
				self.ReduceRoll()
		elif Engulf != None and Burn == None:
			#Loss = max((0,S - self.NatLAR - self.LAR)) + max((0,K - self.NatMAR - self.MAR))
			Loss = (self.HP.Head + self.HP.Torso + self.HP.Rarm + self.HP.Larm + self.HP.Rleg + self.HP.Lleg)
			if Pierced == None:
				#Loss = max((0,S - self.NatLAR - self.LAR)) + max((0,K - self.NatMAR - self.MAR))
				self.HP.DealDamage(S,K,1,self.NatLAR+self.LAR,self.NatMAR + self.MAR)
				self.HP.DealDamage(S,K,2,self.NatLAR+self.LAR,self.NatMAR + self.MAR)
				self.HP.DealDamage(S,K,3,self.NatLAR+self.LAR,self.NatMAR + self.MAR)
				self.HP.DealDamage(S,K,5,self.NatLAR+self.LAR,self.NatMAR + self.MAR)
				self.HP.DealDamage(S,K,7,self.NatLAR+self.LAR,self.NatMAR + self.MAR)
				self.HP.DealDamage(S,K,10,self.NatLAR+self.LAR,self.NatMAR + self.MAR)
			else:
				LAR = self.LAR - Pierced
				if LAR < 0:
					LAR = 0
				MAR = self.MAR - Pierced
				if MAR < 0:
					MAR = 0
				#Loss = max((0,S - self.NatLAR - LAR)) + max((0,K - self.NatMAR - MAR))
				self.HP.DealDamage(S,K,1,self.NatLAR + LAR,self.NatMAR + MAR)
				self.HP.DealDamage(S,K,2,self.NatLAR + LAR,self.NatMAR + MAR)
				self.HP.DealDamage(S,K,3,self.NatLAR + LAR,self.NatMAR + MAR)
				self.HP.DealDamage(S,K,5,self.NatLAR + LAR,self.NatMAR + MAR)
				self.HP.DealDamage(S,K,7,self.NatLAR + LAR,self.NatMAR + MAR)
				self.HP.DealDamage(S,K,10,self.NatLAR + LAR,self.NatMAR + MAR)
			Loss -= (self.HP.Head + self.HP.Torso + self.HP.Rarm + self.HP.Larm + self.HP.Rleg + self.HP.Lleg)
			if self.HP.Lives == 0:
				self.Alive = 0
				self.Nbr = 0
			if Loss > 0:
				self.ReduceRoll()
		elif Burn != None:
			self.HP.DealDamage(0,1,1,0,0)
			self.HP.DealDamage(0,1,2,0,0)
			self.HP.DealDamage(0,1,3,0,0)
			self.HP.DealDamage(0,1,5,0,0)
			self.HP.DealDamage(0,1,7,0,0)
			if self.HP.Lives == 0:
				self.Alive = 0
				self.Nbr = 0
	def Electrocuted(self,S,K,Loc,PP=None):
		if PP == None:
			Loss = (self.HP.Head + self.HP.Torso + self.HP.Rarm + self.HP.Larm + self.HP.Rleg + self.HP.Lleg)
			self.HP.DealDamage(S,K,Loc,self.NatLAR+self.LAR,self.NatMAR + self.MAR)
			Loss -= (self.HP.Head + self.HP.Torso + self.HP.Rarm + self.HP.Larm + self.HP.Rleg + self.HP.Lleg)
			LR = rand.randint(1,2)
			if Loc in [7,8,9]:
				self.HP.DealDamage(S,K,LR,self.NatLAR+self.LAR,self.NatMAR + self.MAR)
			if Loc in [3,4,5,6,10]:
				self.HP.DealDamage(S,K,7,self.NatLAR+self.LAR,self.NatMAR + self.MAR)
				self.HP.DealDamage(S,K,LR,self.NatLAR+self.LAR,self.NatMAR + self.MAR)
		else:
			LAR = self.LAR - PP
			if LAR < 0:
				LAR = 0
			MAR = self.MAR - PP
			if MAR < 0:
				MAR = 0
			Loss = (self.HP.Head + self.HP.Torso + self.HP.Rarm + self.HP.Larm + self.HP.Rleg + self.HP.Lleg)
			self.HP.DealDamage(S,K,Loc,self.NatLAR + LAR,self.NatMAR + MAR)
			Loss -= (self.HP.Head + self.HP.Torso + self.HP.Rarm + self.HP.Larm + self.HP.Rleg + self.HP.Lleg)
			LR = rand.randint(1,2)
			if Loc in [7,8,9]:
				self.HP.DealDamage(S,K,LR,self.NatLAR+self.LAR,self.NatMAR + self.MAR)
			if Loc in [3,4,5,6,10]:
				self.HP.DealDamage(S,K,7,self.NatLAR+self.LAR,self.NatMAR + self.MAR)
				self.HP.DealDamage(S,K,LR,self.NatLAR+self.LAR,self.NatMAR + self.MAR)
		if self.HP.Lives == 0:
			self.Alive = 0
			self.Nbr = 0
		if Loss > 0:
			self.ReduceRoll()
	def Heal(self,N,Loc,Engulf = None):
		self.HP.Heal(N,Loc,E = Engulf)
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
		self.WD = min((10,self.Pool[2]))
	def ReduceRoll(self):
		Tored = 1
		i = 9
		while Tored == 1:
			if self.Rolled[i]>1:
				self.Rolled[i]-=1
				Tored = 0
			i-=1
			if i == -1:
				Tored = 0

