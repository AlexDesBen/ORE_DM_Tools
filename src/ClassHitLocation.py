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

from ClassExtra import *
from ClassPerso import *
from TallyAlgorithm import *
from SortAlgorithm import *

class HitLocations():
	def __init__(self,XTough):
		self.Lives = 1
		self.LlegMax = self.Lleg = 5 + XTough
		self.RlegMax = self.Rleg = 5 + XTough
		self.RarmMax = self.Rarm = 5 + XTough
		self.LarmMax = self.Larm = 5 + XTough
		self.TorsoMax = self.Torso = 10 + XTough
		self.HeadMax = self.Head = 4 + XTough
	def DamCreep(self,Loc):
		if Loc == 7 or Loc == 8 or Loc == 9:
			self.Head += self.Torso
			self.Torso = 0
			if self.Head <= 0:
				self.Lives = 0
		if Loc == 5 or Loc == 6:
			self.Torso += self.Rarm
			self.Rarm = 0
			if self.Torso < 0:
				self.Head += self.Torso
				self.Torso = 0
				if self.Head <= 0:
					self.Lives = 0
		if Loc == 3 or Loc == 4:
			self.Torso += self.Larm
			self.Larm = 0
			if self.Torso < 0:
				self.Head += self.Torso
				self.Torso = 0
				if self.Head <= 0:
					self.Lives = 0
		if Loc == 2:
			self.Torso += self.Rleg
			self.Rleg = 0
			if self.Rleg < 0:
				self.Head += self.Torso
				self.Torso = 0
				if self.Head <= 0:
					self.Lives = 0
		if Loc == 1:
			self.Torso += self.Lleg
			self.Lleg = 0
			if self.Torso < 0:
				self.Head += self.Torso
				self.Torso = 0
				if self.Head <= 0:
					self.Lives = 0
	def DealDamage(self,S,K,Loc,LAR,MAR,Engulf = None):
		if LAR != 0:
			if S != 0 and K >= LAR:
				s = 1 + LAR
			elif S != 0 and K < LAR:
				s = 1 + K
			elif S == 0 and K >= LAR:
				s = LAR
			else:
				s = K
			k = K - LAR - MAR
			if k < 0:
				k = 0
		else:
			s = S - MAR
			if s < 0:
				s = 0
			k = K - MAR
			if k < 0:
				k = 0
		Dam = k + s
		if Loc == 1:
			self.Lleg -= Dam
			if self.Lleg < 0:
				self.DamCreep(Loc)
		if Loc == 2:
			self.Rleg -= Dam
			if self.Rleg < 0:
				self.DamCreep(Loc)
		if Loc == 3 or Loc == 4:
			self.Larm -= Dam
			if self.Larm < 0:
				self.DamCreep(Loc)
		if Loc == 5 or Loc == 6:
			self.Rarm -= Dam
			if self.Rarm < 0:
				self.DamCreep(Loc)
		if Loc == 7 or Loc == 8 or Loc == 9:
			self.Torso -= Dam
			if self.Torso < 0:
				self.DamCreep(Loc)
		if Loc == 10:
			self.Head -= Dam
			if self.Head <= 0:
				self.Lives = 0
	def Heal(self,N,Loc,E = None):
		if E == None:
			if Loc == 1:
				self.Lleg = min((self.Lleg + N,self.LlegMax))
			if Loc == 2:
				self.Rleg = min((self.Rleg + N,self.RlegMax))
			if Loc == 3 or Loc == 4:
				self.Larm = min((self.Larm + N,self.LarmMax))
			if Loc == 5 or Loc == 6:
				self.Rarm = min((self.Rarm + N,self.RarmMax))
			if Loc == 7 or Loc == 8 or Loc == 9:
				self.Torso = min((self.Torso + N,self.TorsoMax))
			if Loc == 10:
				self.Head = min((self.Head + N,self.HeadMax))
		else:
			self.Lleg = min((self.Lleg + N,self.LlegMax))
			self.Rleg = min((self.Rleg + N,self.RlegMax))
			self.Larm = min((self.Larm + N,self.LarmMax))
			self.Rarm = min((self.Rarm + N,self.RarmMax))
			self.Torso = min((self.Torso + N,self.TorsoMax))
			self.Head = min((self.Head + N,self.HeadMax))



