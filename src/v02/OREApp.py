
#!/usr/bin/env python
#*-* coding: utf-8 *-*
####################################################################################################
####################################################################################################
#                                  %
# Author      : Alexandre Desilets-Benoit, Ph.D. Phys.
# Institution : None
# Group       : 
# Year        : 2017
# Version     : 0.2
# function    : to fill
#
####################################################################################################
####################################################################################################

import kivy
kivy.require('1.9.1')
import math
import random as rand
import csv

from kivy.app import App
from kivy.graphics import *
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout

#from ClassExtra import *
#from ClassHitLocation import *
#from ClassPerso import *
#from SortAlgorithm import *
#from TallyAlgorithm import *
from Character import *
from Init_Page import *
from Setup_Page import *
from Round_Page import *
import test


class OREApp(App):
    Data = [[u'' for i in range(0,16)] for j in range(0,25)]
    for i in range(0,25):
        Data[i][0]=i
    kv_directory = '.'











