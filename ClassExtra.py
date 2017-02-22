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

from ClassPerso import *
from ClassHitLocation import *
from TallyAlgorithm import *
from SortAlgorithm import *

class Extra():
	def __init__(self, Name, Sense, HP, NatLAR, LAR,NatMAR,MAR, Nbr, rating):
		self.Name = Name
		self.Sense = Sense
		self.Allied = 0
		self.HP = HP
		self.HPMax = HP
		self.Nbr = Nbr
		self.Alive = 1
		self.Nature = "Extra"
		self.Rating = HP
		self.Order = 0

		self.NatLAR = NatLAR
		self.LAR = LAR
		self.NatMAR = NatMAR
		self.MAR = MAR
		
		self.Dazed = 0
		self.Burning = 0
		self.Pool = self.Rating*Nbr
		self.Atk = 'S'
		self.AtkBonus = 0
		self.SpeedBonus = 0
		self.Penetration = 0
		self.Defence = 0
		self.InstantDefence = 0
		self.WD = 0

		self.Rolled = [0,0,0,0,0,0,0,0,0,0]
	def Damaged(self,S,K,Loc,Pierced=None,Engulf = None,Burn = None):
		Loss = 0
		Loss = (self.HP)
		if Pierced == None and Burn == None:
			Sdam = max((0,(S-self.NatMAR - self.MAR)))
			Kdam = max((0,(K-self.NatMAR - self.MAR)))
			if Engulf == None:
				if Sdam == 0 and (self.LAR + self.NatLAR) != 0:
					Sdam = min((Kdam,(self.NatLAR + self.LAR)))
				elif Sdam != 0 and (self.LAR + self.NatLAR) != 0:
					Sdam = 1+min((Kdam,(self.NatLAR + self.LAR)))
				Kdam = max((0,Kdam-(self.NatLAR + self.LAR)))
				self.HP = self.HP - (Sdam+Kdam)
			else:
				self.HP = self.HP - 3*(Sdam+Kdam)
			while self.HP <= 0 and self.Nbr > 1 and self.Alive == 1:
				self.Nbr -= 1
				self.HP += self.HPMax
				if self.Nbr <= 0 and self.HP <= 0:
					self.Alive = 0
					self.HP = 0
			if self.Nbr == 1 and self.HP <= 0:
				self.Alive = 0
			if self.Alive == 0:
				self.HP = 0
		elif Pierced != None and Burn == None:
			LAR = self.LAR - Pierced
			if LAR < 0:
				LAR = 0
			MAR = self.MAR - Pierced
			if MAR < 0:
				MAR = 0
			Sdam = max((0,S-MAR))
			Kdam = max((0,K-MAR))
			if Engulf == None:
				if Sdam == 0 and (self.LAR + self.NatLAR) != 0:
					Sdam = min((Kdam,LAR))
				if Sdam != 0 and (self.LAR + self.NatLAR) != 0:
					Sdam = 1+min((Kdam,LAR))
				Kdam = max((0,Kdam-LAR))
				self.HP = self.HP - (Sdam+Kdam)
			else:
				self.HP = self.HP -3* max((0,Sdam)) - max((0,Kdam))
			while self.HP <= 0 and self.Nbr > 0 and self.Alive == 1:
				self.Nbr -= 1
				self.HP += 1
				if self.Nbr <= 0 and self.HP <= 0:
					self.Alive = 0
			if self.Nbr == 1 and self.HP <= 0:
				self.Alive = 0
			if self.Alive == 0:
				self.HP = 0
		if self.Nbr <= 1 and self.HP <= 0:
			self.Nbr = 0
			self.Alive = 0
		Loss -= (self.HP)
		if Loss > 0:
			self.ReduceRoll()
		if Burn != None:
			self.HP -= 2
			while self.HP <= 0 and self.Nbr > 0 and self.Alive == 1:
				self.Nbr -= 1
				self.HP += 1
				if self.Nbr <= 0 and self.HP <= 0:
					self.Alive = 0
			if self.Nbr == 1 and self.HP <= 0:
				self.Alive = 0
			if self.Alive == 0:
				self.HP = 0
		self.Pool = self.Rating*self.Nbr
	def Electrocuted(self,S,K,Loc,PP=None):
		if PP == None:
			if Loc in [1,2]:
				self.Damaged(S,K,Loc)
			if Loc in [7,8,9]:
				self.Damaged(2*S,2*K,Loc)
			if Loc in [3,4,5,6,10]:
				self.Damaged(3*S,3*K,Loc)	
		else:
			if Loc in [1,2]:
				self.Damaged(S,K,Loc,Pierced = PP)
			if Loc in [7,8,9]:
				Damaged(2*S,2*K,Loc,Pierced = 2*PP)
			if Loc in [3,4,5,6,10]:
				Damaged(3*S,3*K,Loc,Pierced = 3*PP)	
	def Heal(self,N,Loc, Engulf = None):
		self.HP = min((self.HPMax,self.HP + N))
	def Roll(self):
		if self.Pool <= 10:
			Pool = [rand.randint(1,10) for i in range(0,self.Pool)]
		else:
			Pool = [rand.randint(1,10) for i in range(0,10)]
		Pool.sort()
		self.Rolled = Tally(Pool)
	def ReduceRoll(self):
		Tored = 1
		i=9
		while Tored == 1:
			if self.Rolled[i]>1:
				self.Rolled[i]-=1
				Tored = 0
			if i == 0:
				Tored = 0
			i-=1



