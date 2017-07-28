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
from SortAlgorithm import *

def Tally(A):
	Sets = []
	for i in range(1,11):
		Sets.append(sum([A[j] == i for j in range(0,len(A))]))
	return Sets


