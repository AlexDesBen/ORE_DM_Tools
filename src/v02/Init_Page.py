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
from OREApp import *
from Setup_Page import *
from Round_Page import *
import test



#Init Page elements
###Frame for initialisation of app
class Init_Page(GridLayout):
    pass
###Slider to allow vertical scrolling
class Init_V_Slider(Slider):
    pass
###Slider to allow Horizontal scrolling
class Init_H_Slider(Slider):
    pass
###Center Table with columns and rows in character informations
class Init_Core(RelativeLayout):
    pass
###List of column names
class Init_Columns(GridLayout):
    pass
###one column name
class Init_Col(Label):
    pass
###One Character Entry
class Init_One_Entry(GridLayout):
    idnbr = 1
###Character Index
class Init_Index(Label):
    def OnSetText(self,i,j,value):
        OREApp.get_running_app().Data[i][j] = value
    def get_value(self):
        return self.text
    def set_value(self,i):
        self.text = str(i)
###Character Status
class Init_Status(Label):
    def OnSetText(self,i,j,value):
        OREApp.get_running_app().Data[i][j] = value
    def get_value(self):
        return self.text
    def set_value(self,i):
        self.text = u''
###Character Name
class Init_Name(TextInput):
    def OnSetText(self,i,j,value):
        OREApp.get_running_app().Data[i][j] = value
    def get_value(self):
        return self.text
    def set_value(self,i):
        self.text = u''
###Character Nature
class Init_Nature(Label):
    def OnSetText(self,i,j,value):
        OREApp.get_running_app().Data[i][j] = value
    def get_value(self):
        return self.text
    def set_value(self,i):
        self.text = u''
###Character Aliegance
class Init_Aliegance(Label):
    def OnSetText(self,i,j,value):
        OREApp.get_running_app().Data[i][j] = value
    def get_value(self):
        return self.text
    def set_value(self,i):
        self.text = u''
###Character Sense
class Init_Sense(TextInput):
    def OnSetText(self,i,j,value):
        OREApp.get_running_app().Data[i][j] = value
    def get_value(self):
        return self.text
    def set_value(self,i):
        self.text = u''
###Character Damage type
class Init_Damage(TextInput):
    def OnSetText(self,i,j,value):
        OREApp.get_running_app().Data[i][j] = value
    def get_value(self):
        return self.text
    def set_value(self,i):
        self.text = u''
###Character LAR
class Init_LAR(TextInput):
    def OnSetText(self,i,j,value):
        OREApp.get_running_app().Data[i][j] = value
    def get_value(self):
        return self.text
    def set_value(self,i):
        self.text = u''
###Character MAR
class Init_MAR(TextInput):
    def OnSetText(self,i,j,value):
        OREApp.get_running_app().Data[i][j] = value
    def get_value(self):
        return self.text
    def set_value(self,i):
        self.text = u''
###Character Atk
class Init_Atk(TextInput):
    def OnSetText(self,i,j,value):
        OREApp.get_running_app().Data[i][j] = value
    def get_value(self):
        return self.text
    def set_value(self,i):
        self.text = u''
###Character Spd
class Init_Spd(TextInput):
    def OnSetText(self,i,j,value):
        OREApp.get_running_app().Data[i][j] = value
    def get_value(self):
        return self.text
    def set_value(self,i):
        self.text = u''
###Character XTough
class Init_XTough(TextInput):
    def OnSetText(self,i,j,value):
        OREApp.get_running_app().Data[i][j] = value
    def get_value(self):
        return self.text
    def set_value(self,i):
        self.text = u''
###Character Units
class Init_Units(TextInput):
    def OnSetText(self,i,j,value):
        OREApp.get_running_app().Data[i][j] = value
    def get_value(self):
        return self.text
    def set_value(self,i):
        self.text = u''
###Character Rating
class Init_Rating(TextInput):
    def OnSetText(self,i,j,value):
        OREApp.get_running_app().Data[i][j] = value
    def get_value(self):
        return self.text
    def set_value(self,i):
        self.text = u''
###Character Penetration
class Init_Penetration(TextInput):
    def OnSetText(self,i,j,value):
        OREApp.get_running_app().Data[i][j] = value
    def get_value(self):
        return self.text
    def set_value(self,i):
        self.text = u''
###Character Gobble dice
class Init_Gobble(TextInput):
    def OnSetText(self,i,j,value):
        OREApp.get_running_app().Data[i][j] = value
    def get_value(self):
        return self.text
    def set_value(self,i):
        self.text = u''

###Menu with 4 options in Initialisation
class Init_Menu(GridLayout):
    pass
class Init_Menu_Clear(Button):
    def OnClick(self):
        for i in range(0,25):
            for j in range(0,16):
                OREApp.get_running_app().Data[i][j] = u''
        for i in range(0,25):
            OREApp.get_running_app().Data[i][0] = i
        PointTemp = OREApp.get_running_app().root.ids["InitPage"]
        Entries = ["FirstEntry","Entry_2","Entry_3","Entry_4","Entry_5","Entry_6","Entry_7",
                "Entry_8","Entry_9","Entry_10","Entry_11","Entry_12","Entry_13","Entry_14",
                "Entry_15","Entry_16","Entry_17","Entry_18","Entry_19","Entry_20","Entry_21",
                "Entry_22","Entry_23","Entry_24","Entry_25"]
        labels  = ["Index","Status","Name","Nature","Aliegance","Sense","Damage","LAR","MAR","Atk","Spd",
                "XTough","Units","Rating","Penetration","Gobble"]
        for i in range(0,25):
            for j in range(0,16):
                PointTemp.ids[Entries[i]].ids[labels[j]].set_value(i)
class Init_Menu_Save(Button):
    def OnClick(self):
        print("Save")
class Init_Menu_Load(Button):
    def OnClick(self):
        print("Load")
class Init_Menu_Start(Button):
    def OnClick(self,Data):
        Data = OREApp.get_running_app().Data
        PointTemp = OREApp.get_running_app().root.ids["InitPage"]
        Entries = ["FirstEntry","Entry_2","Entry_3","Entry_4","Entry_5","Entry_6","Entry_7",
                "Entry_8","Entry_9","Entry_10","Entry_11","Entry_12","Entry_13","Entry_14",
                "Entry_15","Entry_16","Entry_17","Entry_18","Entry_19","Entry_20","Entry_21",
                "Entry_22","Entry_23","Entry_24","Entry_25"]
        labels  = ["Index","Status","Name","Nature","Aliegance","Sense","Damage","LAR","MAR","Atk","Spd",
                "XTough","Units","Rating","Penetration","Gobble"]
        for i in range(0,25):
            for j in range(0,16):
                Data[i][j] = PointTemp.ids[Entries[i]].ids[labels[j]].get_value()
        print("Start")
                
        



















