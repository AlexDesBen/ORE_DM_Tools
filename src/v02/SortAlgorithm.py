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

#from ClassExtra import *
#from ClassPerso import *
#from ClassHitLocation import *
from TallyAlgorithm import *

def MySort(A):
	#A = [NPC,extra,allied,active,name,sense, other stuff]
	Nbr = len(A)/13
	tempdata = []
	for i in range(0,Nbr):
		if A[i][3] != 0:
			tempdata.append(A[i])
	sorteddata = sorted(tempdata,key = lambda tempdata: tempdata[5], reverse=False)
	Nbr = len(sorteddata)/13
	for i in range(0,Nbr):
		for j in range(0,Nbr-1):
			if sorteddata[j][2] == 1 and sorteddata[j+1][2] == 0:
				if sorteddata[j][5] == sorteddata[j+1][5]:
					temp = sorteddata[j]
					sorteddata[j] = sorteddata[j+1]
					sorteddata[j+1] = temp
	return sorteddata

