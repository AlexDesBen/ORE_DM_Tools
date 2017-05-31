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
from OREApp import *
from Setup_Page import *
from Round_Page import *
import test


##############################################################################################################
##############################################################################################################
##############################################################################################################
#test.perso_def()
#test.rolls()
#test.damage()
##############################################################################################################
##############################################################################################################
##############################################################################################################



class Page_Label(Label):
    pass


if __name__ == '__main__':
    OREApp().run()




















'''
##############################################################################################################
##############################################################################################################
##############################################################################################################
class InitLine():
	def __init__(self,i):
		self.Which = i
		self.Order = Label(text='%i'%(i+1),size_hint_x = 1,font_size = 15,width = 10, height = 20,size_hint_y = 1)
		self.NPC = CheckBox(text='',size_hint_x = 1,width = 10, height = 20,size_hint_y = 1)
		self.Extra = CheckBox(text='',size_hint_x = 1,width = 10, height = 20,size_hint_y = 1)
		self.Allied = CheckBox(text='',size_hint_x = 1,width = 10, height = 20,size_hint_y = 1)
		self.Active = CheckBox(text='',size_hint_x = 1,width = 10, height = 20,size_hint_y = 1)
		self.Name = TextInput(text='',size_hint_x = 1,font_size = 12,width = 20, height = 20,size_hint_y = 1)
		self.Sense = TextInput(text='',size_hint_x = 1,font_size = 12,width = 10, height = 20,size_hint_y = 1)
		self.ExtraHP = TextInput(text='',size_hint_x = 1,font_size = 12,width = 10, height = 20,size_hint_y = 1)
		self.Units = TextInput(text='',size_hint_x = 1,font_size = 12,width = 10, height = 20,size_hint_y = 1)
		self.LAR = TextInput(text='',size_hint_x = 1,font_size = 12,width = 10, height = 20,size_hint_y = 1)
		self.MAR = TextInput(text='',size_hint_x = 1,font_size = 12,width = 10, height = 20,size_hint_y = 1)
		self.Dam = TextInput(text='',size_hint_x = 1,font_size = 12,width = 10, height = 20,size_hint_y = 1)
		self.AtkBonus = TextInput(text='',size_hint_x = 1,font_size = 12,width = 10, height = 20,size_hint_y = 1)
		self.SpdBonus = TextInput(text='',size_hint_x = 1,font_size = 12,width = 10, height = 20,size_hint_y = 1)
		self.ColLayout = BoxLayout(orientation='vertical',width = 70,size_hint = (0,1))
		self.ColLayout.add_widget(self.Order)
		self.ColLayout.add_widget(self.NPC)
		self.ColLayout.add_widget(self.Extra)
		self.ColLayout.add_widget(self.Allied)
		self.ColLayout.add_widget(self.Active)
		self.ColLayout.add_widget(self.Name)
		self.ColLayout.add_widget(self.Sense)
		self.ColLayout.add_widget(self.ExtraHP)
		self.ColLayout.add_widget(self.Units)
		self.ColLayout.add_widget(self.LAR)
		self.ColLayout.add_widget(self.MAR)
		self.ColLayout.add_widget(self.Dam)
		self.ColLayout.add_widget(self.AtkBonus)
		self.ColLayout.add_widget(self.SpdBonus)

class ClearConfirmation():
	def __init__(self,parent,grandparent,s):
		self.Parent = parent
		self.GrandParent = grandparent
		self.ConfLabel = Label(text='Clear?',font_size = 20,bold = True,size = (200,40)\
			,pos_hint = {'center_x':0.5,'top':0.9},color = [0.9,0.9,0.9,1],size_hint = (0,0))
		self.Back = Button(text='Cancel',font_size = 20,size = (75,30),pos_hint = {'x':0.1,'y':0.1},size_hint=(0,0))
		self.Confirm = Button(text='Ok',font_size = 20,size = (75,30),pos_hint = {'right':0.9,'y':0.1},size_hint=(0,0))
		self.MenuLayout = RelativeLayout(size = s,pos_hint={'x':0,'y':0},size_hint=(1,1))
		with self.MenuLayout.canvas:
			Color(0.3,0.3,0.3)
			Rectangle(pos = (0,0),size = self.MenuLayout.size)
			Line(points = [0,0,0,s[1],s[0],s[1],s[0],0,0,0],width = 10)
		self.MenuLayout.add_widget(self.Back)
		self.MenuLayout.add_widget(self.Confirm)
		self.MenuLayout.add_widget(self.ConfLabel)
		self.TotalLayout = BoxLayout(size = s,pos_hint = {'center_x':0.5,'center_y':0.5},size_hint = (0,0))
		self.TotalLayout.add_widget(self.MenuLayout)
		self.Back.bind(on_press=self.Nothing)
		self.Confirm.bind(on_press=self.ClearBoard)
	def Nothing(self,instance):
		self.TotalLayout.clear_widgets()
		self.Parent.Clearing = 0
	def ClearBoard(self,instance):
		self.Parent.Clearing = 0
		for i in range(0,25):
			self.Parent.LineLayouts[i].NPC.active = 0
			self.Parent.LineLayouts[i].Extra.active = 0
			self.Parent.LineLayouts[i].Allied.active = 0
			self.Parent.LineLayouts[i].Active.active = 0
			self.Parent.LineLayouts[i].Name.text = ''
			self.Parent.LineLayouts[i].Sense.text = ''
			self.Parent.LineLayouts[i].ExtraHP.text = ''
			self.Parent.LineLayouts[i].Units.text = ''
			self.Parent.LineLayouts[i].LAR.text = ''
			self.Parent.LineLayouts[i].MAR.text = ''
			self.Parent.LineLayouts[i].Dam.text = ''
			self.Parent.LineLayouts[i].AtkBonus.text = ''
			self.Parent.LineLayouts[i].SpdBonus.text = ''
		self.GrandParent.Roaster = []
		self.GrandParent.WhichRound = 1
		self.TotalLayout.clear_widgets()
		self.Parent.MidLayout.add_widget(self.Parent.MidHLayout)

class LoadConfirmation():
	def __init__(self,parent,grandparent,s):
		self.Parent = parent
		self.GrandParent = grandparent
		self.TextField = TextInput(text='../../Input/data.csv',font_size = 20,bold = True,size = (200,40)\
			,pos_hint = {'center_x':0.5,'top':0.9},color = [0.9,0.9,0.9,1],size_hint = (0,0))
		self.Back = Button(text='Cancel',font_size = 20,size = (75,30),pos_hint = {'x':0.1,'y':0.1},size_hint=(0,0))
		self.Confirm = Button(text='Load',font_size = 20,size = (75,30),pos_hint = {'right':0.9,'y':0.1},size_hint=(0,0))
		self.MenuLayout = RelativeLayout(size = s,pos_hint={'x':0,'y':0},size_hint=(1,1))
		with self.MenuLayout.canvas:
			Color(0.3,0.3,0.3)
			Rectangle(pos = (0,0),size = self.MenuLayout.size)
			Line(points = [0,0,0,s[1],s[0],s[1],s[0],0,0,0],width = 10)
		self.MenuLayout.add_widget(self.Back)
		self.MenuLayout.add_widget(self.Confirm)
		self.MenuLayout.add_widget(self.TextField)
		self.TotalLayout = BoxLayout(size = s,pos_hint = {'center_x':0.5,'center_y':0.5},size_hint = (0,0))
		self.TotalLayout.add_widget(self.MenuLayout)
		self.Back.bind(on_press=self.Nothing)
		self.Confirm.bind(on_press=self.LoadBoard)
	def Nothing(self,instance):
		self.TotalLayout.clear_widgets()
		self.Parent.Clearing = 0
	def LoadBoard(self,instance):
		self.Parent.Clearing = 0
		for i in range(0,25):
			self.Parent.LineLayouts[i].NPC.active = 0
			self.Parent.LineLayouts[i].Extra.active = 0
			self.Parent.LineLayouts[i].Allied.active = 0
			self.Parent.LineLayouts[i].Active.active = 0
			self.Parent.LineLayouts[i].Name.text = ''
			self.Parent.LineLayouts[i].Sense.text = ''
			self.Parent.LineLayouts[i].ExtraHP.text = ''
			self.Parent.LineLayouts[i].Units.text = ''
			self.Parent.LineLayouts[i].LAR.text = ''
			self.Parent.LineLayouts[i].MAR.text = ''
			self.Parent.LineLayouts[i].Dam.text = ''
			self.Parent.LineLayouts[i].AtkBonus.text = ''
			self.Parent.LineLayouts[i].SpdBonus.text = ''
		self.GrandParent.Roaster = []
		self.GrandParent.WhichRound = 1
		self.TotalLayout.clear_widgets()
		self.Parent.MidLayout.add_widget(self.Parent.MidHLayout)
		with open(self.TextField.text,'rb') as csvfile:
			LoadedData = csv.reader(csvfile)
			i = 0
			for row in LoadedData:
				data = row
				#NPC line
				j=0
				if data[j].isdigit() and (data[j] == '1' or data[j] == '0'):
					self.Parent.LineLayouts[i].NPC.active = int(data[j])
				elif data[j] == True:
					self.Parent.LineLayouts[i].NPC.active = True
				elif data[j] == False or data[j].isdigit() == False:
					self.Parent.LineLayouts[i].NPC.active = False
				#Extra line
				j=1
				if data[j].isdigit() and (data[j] == '1' or data[j] == '0'):
					self.Parent.LineLayouts[i].Extra.active = int(data[j])
				elif data[j] == True:
					self.Parent.LineLayouts[i].Extra.active = True
				elif data[j] == False or data[j].isdigit() == False:
					self.Parent.LineLayouts[i].Extra.active = False
				#Allied line
				j=2
				if data[j].isdigit() and (data[j] == '1' or data[j] == '0'):
					self.Parent.LineLayouts[i].Allied.active = int(data[j])
				elif data[j] == True:
					self.Parent.LineLayouts[i].Allied.active = True
				elif data[j] == False or data[j].isdigit() == False:
					self.Parent.LineLayouts[i].Allied.active = False
				#Active line
				j=3
				if data[j].isdigit() and (data[j] == '1' or data[j] == '0'):
					self.Parent.LineLayouts[i].Active.active = int(data[j])
				elif data[j] == True:
					self.Parent.LineLayouts[i].Active.active = True
				elif data[j] == False or data[j].isdigit() == False:
					self.Parent.LineLayouts[i].Active.active = False
				#Name line
				j=4
				if data[j].isalnum():
					self.Parent.LineLayouts[i].Name.text = str(data[j])
				elif data[j] == '':
					self.Parent.LineLayouts[i].Name.text = str(i)
				#Sense line
				j=5
				if data[j].isalnum():
					self.Parent.LineLayouts[i].Sense.text = str(data[j])
				elif data[j] == '':
					self.Parent.LineLayouts[i].Sense.text = str(1)
				#ExtraHP line
				j=6
				if data[j].isalnum():
					self.Parent.LineLayouts[i].ExtraHP.text = str(data[j])
				elif data[j] == '' and self.Parent.LineLayouts[i].Extra.active == False:
					self.Parent.LineLayouts[i].ExtraHP.text = str(0)
				elif data[j] == '' and self.Parent.LineLayouts[i].Extra.active == True:
					self.Parent.LineLayouts[i].ExtraHP.text = str(1)
				#Units line
				j=7
				if data[j].isalnum():
					self.Parent.LineLayouts[i].Units.text = str(data[j])
				elif data[j] == '':
					self.Parent.LineLayouts[i].Units.text = str(1)
				#LAR line
				j=8
				if data[j].isalnum():
					self.Parent.LineLayouts[i].LAR.text = str(data[j])
				elif data[j] == '':
					self.Parent.LineLayouts[i].LAR.text = str(0)
				#MAR line
				j=9
				if data[j].isalnum():
					self.Parent.LineLayouts[i].MAR.text = str(data[j])
				elif data[j] == '':
					self.Parent.LineLayouts[i].MAR.text = str(0)
				#Dam line
				j=10
				if data[j].isalnum():
					self.Parent.LineLayouts[i].Dam.text = str(data[j])
				elif data[j] == '':
					self.Parent.LineLayouts[i].Dam.text = str(S)
				#AtkBonus line
				j=11
				if data[j].isalnum():
					self.Parent.LineLayouts[i].AtkBonus.text = str(data[j])
				elif data[j] == '':
					self.Parent.LineLayouts[i].AtkBonus.text = str(0)
				#SpdBonus line
				j=12
				if data[j].isalnum():
					self.Parent.LineLayouts[i].SpdBonus.text = str(data[j])
				elif data[j] == '':
					self.Parent.LineLayouts[i].SpdBonus.text = str(0)
				i+=1

class SaveConfirmation():
	def __init__(self,parent,grandparent,s):
		self.Parent = parent
		self.GrandParent = grandparent
		self.TextField = TextInput(text='../../Input/SavedData.csv',font_size = 20,size = (200,40)\
			,pos_hint = {'center_x':0.5,'top':0.9},size_hint = (1,None))
		self.Back = Button(text='Cancel',font_size = 20,size = (75,30),pos_hint = {'x':0.1,'y':0.1},size_hint=(0,0))
		self.Confirm = Button(text='Save',font_size = 20,size = (75,30),pos_hint = {'right':0.9,'y':0.1},size_hint=(0,0))
		self.MenuLayout = RelativeLayout(size = s,pos_hint={'x':0,'y':0},size_hint=(1,1))
		with self.MenuLayout.canvas:
			Color(0.3,0.3,0.3)
			Rectangle(pos = (0,0),size = self.MenuLayout.size)
			Line(points = [0,0,0,s[1],s[0],s[1],s[0],0,0,0],width = 10)
		self.MenuLayout.add_widget(self.Back)
		self.MenuLayout.add_widget(self.Confirm)
		self.MenuLayout.add_widget(self.TextField)
		self.TotalLayout = BoxLayout(size = s,pos_hint = {'center_x':0.5,'center_y':0.5},size_hint = (0,0))
		self.TotalLayout.add_widget(self.MenuLayout)
		self.Back.bind(on_press=self.Nothing)
		self.Confirm.bind(on_press=self.SaveBoard)
	def Nothing(self,instance):
		self.TotalLayout.clear_widgets()
		self.Parent.Clearing = 0
	def SaveBoard(self,instance):
		with open(self.TextField.text,'wb') as csvfile:
			DataToSave = csv.writer(csvfile)
			for i in range(0,25):
				if self.Parent.LineLayouts[i].Name.text.isalnum():
					LineData = []
					LineData.append(self.Parent.LineLayouts[i].NPC.active)
					LineData.append(self.Parent.LineLayouts[i].Extra.active)
					LineData.append(self.Parent.LineLayouts[i].Allied.active)
					LineData.append(self.Parent.LineLayouts[i].Active.active)
					LineData.append(self.Parent.LineLayouts[i].Name.text)
					LineData.append(self.Parent.LineLayouts[i].Sense.text)
					LineData.append(self.Parent.LineLayouts[i].ExtraHP.text)
					LineData.append(self.Parent.LineLayouts[i].Units.text)
					LineData.append(self.Parent.LineLayouts[i].LAR.text)
					LineData.append(self.Parent.LineLayouts[i].MAR.text)
					LineData.append(self.Parent.LineLayouts[i].Dam.text)
					LineData.append(self.Parent.LineLayouts[i].AtkBonus.text)
					LineData.append(self.Parent.LineLayouts[i].SpdBonus.text)
					DataToSave.writerow(LineData)
		self.Parent.Clearing = 0
		self.GrandParent.WhichRound = 1
		self.TotalLayout.clear_widgets()
		self.Parent.MidLayout.add_widget(self.Parent.MidHLayout)

class InitLayout():
	def ClearBoard(self,instance):
		self.MidLayout.remove_widget(self.MidHLayout)
		if self.Clearing == 0:
			self.Clearing = 1
			self.MenuInitClear = ClearConfirmation(self,self.Parent,(200,100))
			self.Parent.TotalLayout.add_widget(self.MenuInitClear.TotalLayout)
	def SaveBoard(self,instance):
		self.MidLayout.remove_widget(self.MidHLayout)
		if self.Clearing == 0:
			self.Clearing = 1
			self.MenuInitSave = SaveConfirmation(self,self.Parent,(300,100))
			self.Parent.TotalLayout.add_widget(self.MenuInitSave.TotalLayout)
	def LoadData(self,instance):
		self.MidLayout.remove_widget(self.MidHLayout)
		if self.Clearing == 0:
			self.Clearing = 1
			self.MenuInitLoad = LoadConfirmation(self,self.Parent,(300,100))
			self.Parent.TotalLayout.add_widget(self.MenuInitLoad.TotalLayout)
	def StartCombat(self,instance):
		temp = []
		tempRoaster = []
		for i in range(0,25):
			if self.LineLayouts[i].Active.active == 1:
				temp.append(int(self.LineLayouts[i].Order.text)-1)
		j = 0
		for i in temp:
			if self.LineLayouts[i].Sense.text != '':
				temp[j] = [int(self.LineLayouts[i].Sense.text),temp[j],self.LineLayouts[i].Allied.active]
			else:
				temp[j] = [1,temp[j],self.LineLayouts[i].Allied.active]
			j += 1
		temp.sort()
		for i in range(0,j):
			for k in range(0,j-1):
				if (temp[k][2] == 1 and temp[k+1][2] == 0) and temp[k][0] == temp[k+1][0]:
					temptemp = temp[k+1]
					temp[k+1] = temp[k]
					temp[k] = temptemp
		self.Parent.Roaster = []
		for i in range(0,j):
			Name = self.LineLayouts[temp[i][1]].Name.text
			NPC = int(self.LineLayouts[temp[i][1]].NPC.active)
			Allied = int(self.LineLayouts[temp[i][1]].Allied.active)
			if Allied == 1:
				Nature = 0
			elif Allied == 0:
				Nature = 1
			Sense = 1
			if self.LineLayouts[temp[i][1]].Sense.text.isdigit():
				Sense = int(self.LineLayouts[temp[i][1]].Sense.text)
			HP = 0
			if self.LineLayouts[temp[i][1]].ExtraHP.text.isdigit():
				HP = int(self.LineLayouts[temp[i][1]].ExtraHP.text)
			if HP == 0 and self.LineLayouts[temp[i][1]].Extra.active == True:
				HP = 1
			LAR = 0
			if self.LineLayouts[temp[i][1]].LAR.text.isdigit():
				LAR = int(self.LineLayouts[temp[i][1]].LAR.text)
			MAR = 0
			if self.LineLayouts[temp[i][1]].MAR.text.isdigit():
				MAR = int(self.LineLayouts[temp[i][1]].MAR.text)
			Nbr = 1
			if self.LineLayouts[temp[i][1]].Units.text.isdigit():
				Nbr = int(self.LineLayouts[temp[i][1]].Units.text)
			Dam = 'S'
			if self.LineLayouts[temp[i][1]].Dam.text.isdigit():
				Dam = self.LineLayouts[temp[i][1]].Dam.text
			Atk = 0
			if self.LineLayouts[temp[i][1]].AtkBonus.text.isdigit():
				Atk = int(self.LineLayouts[temp[i][1]].AtkBonus.text)
			Spd = 0
			if self.LineLayouts[temp[i][1]].SpdBonus.text.isdigit():
				Spd = int(self.LineLayouts[temp[i][1]].SpdBonus.text)
			if self.LineLayouts[temp[i][1]].Extra.active == 1:
				self.Parent.Roaster.append(Extra(Name,Sense,HP,0,LAR,0,MAR,Nbr,0))
			if self.LineLayouts[temp[i][1]].Extra.active == 0:
				self.Parent.Roaster.append(Perso(NPC,Name,Sense,HP,0,LAR,0,MAR,Nbr))
			self.Parent.Roaster[i].Allied = Allied
			self.Parent.Roaster[i].Atk = Dam
			self.Parent.Roaster[i].AtkBonus = Atk
			self.Parent.Roaster[i].SpdBonus = Spd
		if self.TotalLayout.pos == [0,0]:
			self.TotalLayout.pos = [0,5000]
			self.Parent.MenuDeclaration.TotalLayout.pos = [0,0]
			self.Parent.MenuRound.TotalLayout.pos = [0,5000]
		self.Parent.MenuDeclaration.LoadRoaster(self.Parent)
	def SliderSelect(self,instance,value):
		fenl = self.TotalLayout.width
		L = self.MidLayout.width
		DeltaL = L-fenl
		if L > fenl:
			self.MidLayout.pos_hint = {'x':(-(value/100.0)*DeltaL)/fenl,'top':0.93}
	def __init__(self,parent,s):
		self.Parent = parent
		self.Clearing = 0

		self.TopLabel = Label(text='Initialisation',font_size = 30,width = 80, height = 40,size_hint_y = 0\
			,pos_hint= {'x':0,'top':1},color = (1,1,1,1))
		
		self.TitleColLayout = BoxLayout(orientation='vertical',width = 70,height = 500,\
			size_hint = (None,1))
		self.ValuesColLayout = BoxLayout(orientation='horizontal',width = 1500,height = 500,\
			size_hint = (None,1))
		self.MidHLayout = BoxLayout(orientation = 'horizontal',width = 1500,height = 500,size_hint = (None,1))
		self.MidLayout = BoxLayout(orientation = 'vertical',pos_hint={'x':0,'top':0.93},width = 1850,\
			height = 450,size_hint = (None,0.75))
		
		self.BotMenuLayout = BoxLayout(orientation='horizontal',height = 35,size_hint = (1,1))
		self.BotLayout = BoxLayout(orientation='horizontal',size_hint = (1,0),\
			height = 40,pos_hint={'x':0,'y':0})
		
		self.TotalLayout = FloatLayout(size = s)
		
		self.Order = Label(text='Order',font_size = 12,width = 80, height = 20,size_hint_y = 1)
		self.NPC = Label(text='NPC',font_size = 12,width = 80, height = 20,size_hint_y = 1)
		self.Extra = Label(text='Extra',font_size = 12,width = 80, height = 20,size_hint_y = 1)
		self.Allied = Label(text='Allied',font_size = 12,width = 80, height = 20,size_hint_y = 1)
		self.Active = Label(text='Active',font_size = 12,width = 80, height = 20,size_hint_y = 1)
		self.Name = Label(text='Name',font_size = 12,width = 80, height = 20,size_hint_y = 1)
		self.Sense = Label(text='Sense',font_size = 12,width = 80, height = 20,size_hint_y = 1)
		self.ExtraHP = Label(text='Extra HP',font_size = 12,width = 80, height = 20,size_hint_y = 1)
		self.Units = Label(text='Units',font_size = 12,width = 80, height = 20,size_hint_y = 1)
		self.LAR = Label(text='LAR',font_size = 12,width = 80, height = 20,size_hint_y = 1)
		self.MAR = Label(text='MAR',font_size = 12,width = 80, height = 20,size_hint_y = 1)
		self.Dam = Label(text='Damage',font_size = 12,width = 80, height = 20,size_hint_y = 1)
		self.AtkBonus = Label(text='+Atk',font_size = 12,width = 80, height = 20,size_hint_y = 1)
		self.SpdBonus = Label(text='+Spd',font_size = 12,width = 80, height = 20,size_hint_y = 1)
		self.LineLayouts = [InitLine(i) for i in range(0,25)]
		self.TitleColLayout.add_widget(self.Order)
		self.TitleColLayout.add_widget(self.NPC)
		self.TitleColLayout.add_widget(self.Extra)
		self.TitleColLayout.add_widget(self.Allied)
		self.TitleColLayout.add_widget(self.Active)
		self.TitleColLayout.add_widget(self.Name)
		self.TitleColLayout.add_widget(self.Sense)
		self.TitleColLayout.add_widget(self.ExtraHP)
		self.TitleColLayout.add_widget(self.Units)
		self.TitleColLayout.add_widget(self.LAR)
		self.TitleColLayout.add_widget(self.MAR)
		self.TitleColLayout.add_widget(self.Dam)
		self.TitleColLayout.add_widget(self.AtkBonus)
		self.TitleColLayout.add_widget(self.SpdBonus)
		self.MidHLayout.add_widget(self.TitleColLayout)
		for i in range(0,25):
			self.ValuesColLayout.add_widget(self.LineLayouts[i].ColLayout)
		self.MidHLayout.add_widget(self.ValuesColLayout)
		self.MidLayout.add_widget(self.MidHLayout)
		
		self.Hslider = Slider(orientation='horizontal',pos_hint = {'x':0,'center_y':0.13},height = 20,\
			size_hint = (1,None))
		
		self.Clear = Button(text='Clear',font_size = 20)
		self.Save = Button(text='Save',font_size = 20)
		self.Load = Button(text='Load',font_size = 20)
		self.Start = Button(text='Start',font_size = 20)
		
		self.BotMenuLayout.add_widget(self.Clear)
		self.BotMenuLayout.add_widget(self.Save)
		self.BotMenuLayout.add_widget(self.Load)
		self.BotMenuLayout.add_widget(self.Start)
		self.BotLayout.add_widget(self.BotMenuLayout)
		
		self.TotalLayout.add_widget(self.TopLabel)
		self.TotalLayout.add_widget(self.BotLayout)
		self.TotalLayout.add_widget(self.MidLayout)
		self.TotalLayout.add_widget(self.Hslider)
		
		self.test = 0
		self.Hslider.bind(value=self.SliderSelect)
		self.Clear.bind(on_press=self.ClearBoard)
		self.Save.bind(on_press=self.SaveBoard)
		self.Load.bind(on_press=self.LoadData)
		self.Start.bind(on_press=self.StartCombat)
##############################################################################################################
##############################################################################################################
##############################################################################################################

class DeclarationLine():
	def __init__(self,parent,i,y):
		self.Parent = parent
		self.IsChar = 0
		self.I = i
		self.Y = y
		self.Height = 30
		self.InitY = 60-self.I*self.Height
		self.Activated = 1
		self.InRoaster = 1
		self.Opened = parent.Opened
		self.LineLayout = BoxLayout(orientation = 'horizontal',height = 30,\
			size_hint = (1,None),pos = (0,self.InitY))
		self.Name = Label(text='Alexandre %i'%self.I,font_size = 20,width = 200, height = 20,size_hint = (None,1))
		self.NameChar = Label(text='Alexandre %i'%self.I,font_size = 20,width = 200, height = 20,size_hint = (None,1))
		self.d = TextInput(text='',font_size = 15,width = 40, height = self.Height,size_hint = (None,1))
		self.hd = TextInput(text='',font_size = 15,width = 40, height = self.Height,size_hint = (None,1))
		self.wd = TextInput(text='',font_size = 15,width = 40, height = self.Height,size_hint = (None,1))
		self.hdExtra = Label(text='',font_size = 15,width = 40, height = self.Height,size_hint = (None,1))
		self.wdExtra = Label(text='',font_size = 15,width = 40, height = self.Height,size_hint = (None,1))
		self.gobble = TextInput(text='',font_size = 15,width = 40, height = self.Height,size_hint = (None,1))
		
		self.InfoSup1 = GridLayout(cols = 2,height = 6*30,width = 130,size_hint = (None,None))
		self.InfoSup2 = GridLayout(cols = 2,height = 6*30,width = 130,size_hint = (None,None))
		self.InfoSup = BoxLayout(orientation = 'horizontal',height = 6*30,\
			size_hint = (1,None),pos = (110,150))
		self.TitleDam = Label(text='Damage',font_size = 15,width = 90, height = 20,size_hint = (None,1))
		self.Dam = TextInput(text = '',font_size = 15,width=40, height = self.Height,size_hint = (None,1))
		self.TitleAtk = Label(text='Atk bonus',font_size = 15,width = 90, height = 20,size_hint = (None,1))
		self.AtkBonus = TextInput(text = '',font_size = 15,width=40, height = self.Height,size_hint = (None,1))
		self.TitleSpd = Label(text='Spd bonus',font_size = 15,width = 90, height = 20,size_hint = (None,1))
		self.SpdBonus = TextInput(text = '',font_size = 15,width=40, height = self.Height,size_hint = (None,1))
		self.TitlePen = Label(text='Penetration',font_size = 15,width = 90, height = 20,size_hint = (None,1))
		self.Penetration = TextInput(text = '',font_size = 15,width=40, height = self.Height,size_hint = (None,1))
		self.TitleLAR = Label(text='LAR',font_size = 15,width = 90, height = 20,size_hint = (None,1))
		self.LAR = TextInput(text = '',font_size = 15,width=40, height = self.Height,size_hint = (None,1))
		self.TitleMAR = Label(text='MAR',font_size = 15,width = 90, height = 20,size_hint = (None,1))
		self.MAR = TextInput(text = '',font_size = 15,width=40, height = self.Height,size_hint = (None,1))
		self.TitleHead = Label(text='Head',font_size = 15,width = 80, height = 20,size_hint = (None,1))
		self.Head = Label(text = '',font_size = 15,width=40, height = self.Height,size_hint = (None,1))
		self.TitleTorso = Label(text='Torso',font_size = 15,width = 80, height = 20,size_hint = (None,1))
		self.Torso = Label(text = '',font_size = 15,width=40, height = self.Height,size_hint = (None,1))
		self.TitleRarm = Label(text='Rarm',font_size = 15,width = 80, height = 20,size_hint = (None,1))
		self.Rarm = Label(text = '',font_size = 15,width=40, height = self.Height,size_hint = (None,1))
		self.TitleLarm = Label(text='Larm',font_size = 15,width = 80, height = 20,size_hint = (None,1))
		self.Larm = Label(text = '',font_size = 15,width=40, height = self.Height,size_hint = (None,1))
		self.TitleRleg = Label(text='Rleg',font_size = 15,width = 80, height = 20,size_hint = (None,1))
		self.Rleg = Label(text = '',font_size = 15,width=40, height = self.Height,size_hint = (None,1))
		self.TitleLleg = Label(text='Lleg',font_size = 15,width = 80, height = 20,size_hint = (None,1))
		self.Lleg = Label(text = '',font_size = 15,width=40, height = self.Height,size_hint = (None,1))
		
		self.InfoSup1.add_widget(self.TitleDam)
		self.InfoSup1.add_widget(self.Dam)
		self.InfoSup1.add_widget(self.TitleAtk)
		self.InfoSup1.add_widget(self.AtkBonus)
		self.InfoSup1.add_widget(self.TitleSpd)
		self.InfoSup1.add_widget(self.SpdBonus)
		self.InfoSup1.add_widget(self.TitlePen)
		self.InfoSup1.add_widget(self.Penetration)
		self.InfoSup1.add_widget(self.TitleLAR)
		self.InfoSup1.add_widget(self.LAR)
		self.InfoSup1.add_widget(self.TitleMAR)
		self.InfoSup1.add_widget(self.MAR)
		self.InfoSup2.add_widget(self.TitleHead)
		self.InfoSup2.add_widget(self.Head)
		self.InfoSup2.add_widget(self.TitleTorso)
		self.InfoSup2.add_widget(self.Torso)
		self.InfoSup2.add_widget(self.TitleRarm)
		self.InfoSup2.add_widget(self.Rarm)
		self.InfoSup2.add_widget(self.TitleLarm)
		self.InfoSup2.add_widget(self.Larm)
		self.InfoSup2.add_widget(self.TitleRleg)
		self.InfoSup2.add_widget(self.Rleg)
		self.InfoSup2.add_widget(self.TitleLleg)
		self.InfoSup2.add_widget(self.Lleg)
		self.InfoSup.add_widget(self.InfoSup1)
		self.InfoSup.add_widget(self.InfoSup2)
		
		self.More = Button(text='More',font_size = 15,width = 70, height = self.Height,size_hint =(None,1))
		self.Less = Button(text='Less',font_size = 15,width = 70, height = self.Height,size_hint =(None,1))
		self.LineLayout.add_widget(self.Name)
		self.LineLayout.add_widget(self.d)
		self.LineLayout.add_widget(self.hd)
		self.LineLayout.add_widget(self.wd)
		self.LineLayout.add_widget(self.gobble)
		self.LineLayout.add_widget(self.More)
		self.More.bind(on_press = self.OpenUp)
		self.Less.bind(on_press = self.CloseUp)
	def OpenUp(self,instance):
		self.Parent.Opened = 1
		self.LineLayout.remove_widget(self.More)
		self.LineLayout.add_widget(self.Less)
		self.Parent.InsertSubMenu(self.I)
	def CloseUp(self,instance):
		self.Parent.Opened = 0
		self.LineLayout.remove_widget(self.Less)
		self.LineLayout.add_widget(self.More)
		self.Parent.RemoveSubMenu(self.I)
	def RefreshLines(self,parent,value):
		Hauteur = parent.TotalLayout.height * 0.8 - 100
		Where = ((value-100)/100.0)*((parent.Participants-int(Hauteur/30-8))*30)
		self.LineLayout.pos[1] = self.InitY - Where
		self.InfoSup.pos[1] = self.InitY - Where - 6*30
		Where = -(self.LineLayout.pos[1]-75)
		if (Where > Hauteur or Where < 0) and self.Activated == 1:
			parent.TestLayout.remove_widget(self.LineLayout)
			self.Activated = 0
		elif (Where <= Hauteur and Where > 0) and self.Activated == 0 and self.InRoaster == 1:
			parent.TestLayout.add_widget(self.LineLayout)
			self.Activated = 1

class ClearCombatConfirmation():
	def __init__(self,parent,grandparent,s):
		self.Parent = parent
		self.GrandParent = grandparent
		self.ConfLabel = Label(text='Clear?',font_size = 20,bold = True,size = (200,40)\
			,pos_hint = {'center_x':0.5,'top':0.9},color = [0.9,0.9,0.9,1],size_hint = (0,0))
		self.Back = Button(text='Cancel',font_size = 20,size = (75,30),pos_hint = {'x':0.1,'y':0.1},size_hint=(0,0))
		self.Confirm = Button(text='Ok',font_size = 20,size = (75,30),pos_hint = {'right':0.9,'y':0.1},size_hint=(0,0))
		self.MenuLayout = RelativeLayout(size = s,pos_hint={'x':0,'y':0},size_hint=(1,1))
		with self.MenuLayout.canvas:
			Color(0.3,0.3,0.3)
			Rectangle(pos = (0,0),size = self.MenuLayout.size)
			Line(points = [0,0,0,s[1],s[0],s[1],s[0],0,0,0],width = 10)
		self.MenuLayout.add_widget(self.Back)
		self.MenuLayout.add_widget(self.Confirm)
		self.MenuLayout.add_widget(self.ConfLabel)
		self.TotalLayout = BoxLayout(size = s,pos_hint = {'center_x':0.5,'center_y':0.5},size_hint = (0,0))
		self.TotalLayout.add_widget(self.MenuLayout)
		self.Back.bind(on_press=self.Nothing)
		self.Confirm.bind(on_press=self.ClearBoard)
	def Nothing(self,instance):
		self.TotalLayout.clear_widgets()
		self.Parent.Clearing = 0
	def ClearBoard(self,instance):
		self.Parent.Clearing = 0
		if self.Parent.TotalLayout.pos == [0,0]:
			self.GrandParent.MenuInit.TotalLayout.pos = [0,0]
			self.Parent.TotalLayout.pos = [0,5000]
			self.GrandParent.MenuRound.TotalLayout.pos = [0,5000]
		self.GrandParent.Roaster = []
		self.GrandParent.WhichRound = 1
		if self.Parent.Opened != 0:
			for i in range(0,self.Parent.Participants):
				if self.Parent.DeclarationLines[i].Opened != 0:
					self.Parent.RemoveSubMenu(i)
		self.TotalLayout.clear_widgets()

class DeclarationLayout():
	def RefreshDisplay(self,instance):
		self.Hslider.value = 0
		self.Vslider.value = 100
		for i in range(0,len(self.Parent.Roaster)):
			self.DeclarationLines[i].RefreshLines(self,100)
			self.MidLayout.pos_hint = {'x':0,'top':1}
	def ReturnToInit(self,instance):
		for i in range(0,self.Participants):
			if self.DeclarationLines[i].Opened == 1:
				self.Opened = 0
				self.DeclarationLines[i].Opened = 0
				self.RemoveSubMenu(i)
				self.DeclarationLines[i].LineLayout.remove_widget(self.DeclarationLines[i].Less)
				self.DeclarationLines[i].LineLayout.add_widget(self.DeclarationLines[i].More)
		if self.Clearing == 0:
			self.Clearing = 1
			self.MenuDeclarationClear = ClearCombatConfirmation(self,self.Parent,(200,100))
			self.Parent.TotalLayout.add_widget(self.MenuDeclarationClear.TotalLayout)
	def ExecuteRound(self,instance):
		for i in range(0,self.Participants):
			if self.DeclarationLines[i].Opened == 1:
				self.Opened = 0
				self.DeclarationLines[i].Opened = 0
				self.RemoveSubMenu(i)
				self.DeclarationLines[i].LineLayout.remove_widget(self.DeclarationLines[i].Less)
				self.DeclarationLines[i].LineLayout.add_widget(self.DeclarationLines[i].More)
		self.UpdateRoaster(self.Parent)
		self.Parent.MenuRound.StartNewRound()
		if self.TotalLayout.pos == [0,0]:
			self.Parent.MenuInit.TotalLayout.pos = [0,5000]
			self.TotalLayout.pos = [0,5000]
			self.Parent.MenuRound.TotalLayout.pos = [0,0]
		elif self.TotalLayout.pos == [0,5000]:
			self.Parent.MenuInit.TotalLayout.pos = [0,5000]
			self.TotalLayout.pos = [0,0]
			self.Parent.MenuRound.TotalLayout.pos = [0,5000]
	def VSliderSelect(self,instance,value):
		fenl = self.TotalLayout.width
		L = self.MidLayout.width
		DeltaL = L-fenl
		fenh = self.TotalLayout.height
		H = self.MidLayout.height
		DeltaH = L-fenl
		for i in range(0,len(self.DeclarationLines)):
			self.DeclarationLines[i].RefreshLines(self,value)
	def HSliderSelect(self,instance,value):
		fenl = self.TotalLayout.width
		L = self.MidLayout.width
		DeltaL = L-fenl
		fenh = self.TotalLayout.height
		H = self.MidLayout.height
		DeltaH = L-fenl
		if L > fenl and H > fenh:
			self.MidLayout.pos_hint = {'x':(-(value/100.0)*DeltaL)/fenl,'top':(-(value/100.0)*DeltaH)/fenh}
		if L > fenl and H <= fenh:
			self.MidLayout.pos_hint = {'x':(-(value/100.0)*DeltaL)/fenl,'top':1}
	def LoadRoaster(self,parent):
		self.Participants = len(parent.Roaster)
		for i in range(0,len(parent.Roaster)):
			if self.DeclarationLines[i].Activated == 0:
				self.TestLayout.add_widget(self.DeclarationLines[i].LineLayout)
				self.DeclarationLines[i].Activated = 1
				self.DeclarationLines[i].InRoaster = 1
			if parent.Roaster[i].Name == '':
				self.DeclarationLines[i].Name.text = str(i)
				self.DeclarationLines[i].NameChar.text = str(i)
			else:
				self.DeclarationLines[i].Name.text = parent.Roaster[i].Name
				self.DeclarationLines[i].NameChar.text = parent.Roaster[i].Name
			self.DeclarationLines[i].Name.bold = True
			self.DeclarationLines[i].NameChar.bold = True
			if parent.Roaster[i].Nature == "Char":
				if self.DeclarationLines[i].IsChar == 0:
					self.DeclarationLines[i].IsChar = 1
					self.DeclarationLines[i].LineLayout.remove_widget(self.DeclarationLines[i].Name)
					self.DeclarationLines[i].LineLayout.remove_widget(self.DeclarationLines[i].d)
					self.DeclarationLines[i].LineLayout.remove_widget(self.DeclarationLines[i].hd)
					self.DeclarationLines[i].LineLayout.remove_widget(self.DeclarationLines[i].wd)
					self.DeclarationLines[i].LineLayout.remove_widget(self.DeclarationLines[i].gobble)
					self.DeclarationLines[i].LineLayout.remove_widget(self.DeclarationLines[i].More)
					self.DeclarationLines[i].LineLayout.add_widget(self.DeclarationLines[i].NameChar)
				self.DeclarationLines[i].Name.color = [0.3,1,0.3,1]
				self.DeclarationLines[i].NameChar.color = [0.3,1,0.3,1]
			elif parent.Roaster[i].Allied == 1:
				self.DeclarationLines[i].Name.color = [0.3,0.3,1,1]
				if self.DeclarationLines[i].IsChar == 1:
					self.DeclarationLines[i].IsChar = 0
					self.DeclarationLines[i].LineLayout.remove_widget(self.DeclarationLines[i].NameChar)
					self.DeclarationLines[i].LineLayout.add_widget(self.DeclarationLines[i].Name)
					self.DeclarationLines[i].LineLayout.add_widget(self.DeclarationLines[i].d)
					self.DeclarationLines[i].LineLayout.add_widget(self.DeclarationLines[i].hd)
					self.DeclarationLines[i].LineLayout.add_widget(self.DeclarationLines[i].wd)
					self.DeclarationLines[i].LineLayout.add_widget(self.DeclarationLines[i].gobble)
					self.DeclarationLines[i].LineLayout.add_widget(self.DeclarationLines[i].More)
			elif parent.Roaster[i].Allied == 0:
				self.DeclarationLines[i].Name.color = [1,0.3,0.3,1]
				if self.DeclarationLines[i].IsChar == 1:
					self.DeclarationLines[i].IsChar = 0
					self.DeclarationLines[i].LineLayout.remove_widget(self.DeclarationLines[i].NameChar)
					self.DeclarationLines[i].LineLayout.add_widget(self.DeclarationLines[i].Name)
					self.DeclarationLines[i].LineLayout.add_widget(self.DeclarationLines[i].d)
					self.DeclarationLines[i].LineLayout.add_widget(self.DeclarationLines[i].hd)
					self.DeclarationLines[i].LineLayout.add_widget(self.DeclarationLines[i].wd)
					self.DeclarationLines[i].LineLayout.add_widget(self.DeclarationLines[i].gobble)
					self.DeclarationLines[i].LineLayout.add_widget(self.DeclarationLines[i].More)
			if parent.Roaster[i].Nature != "Char":
				self.DeclarationLines[i].InRoaster = 1
				self.DeclarationLines[i].RefreshLines(self,100)
				self.DeclarationLines[i].Dam.text = parent.Roaster[i].Atk
				self.DeclarationLines[i].AtkBonus.text = str(parent.Roaster[i].AtkBonus)
				self.DeclarationLines[i].SpdBonus.text = str(parent.Roaster[i].SpdBonus)
				self.DeclarationLines[i].Penetration.text = str(parent.Roaster[i].Penetration)
				self.DeclarationLines[i].LAR.text = str(parent.Roaster[i].LAR)
				self.DeclarationLines[i].MAR.text = str(parent.Roaster[i].MAR)
				if parent.Roaster[i].Nature == "Extra":
					self.DeclarationLines[i].TitleHead.text = 'HP'
					self.DeclarationLines[i].Head.text = str(parent.Roaster[i].HP)
					self.DeclarationLines[i].TitleTorso.text = 'Units'
					self.DeclarationLines[i].Torso.text = str(parent.Roaster[i].Nbr)
					self.DeclarationLines[i].TitleRarm.text = ''
					self.DeclarationLines[i].Rarm.text = ''
					self.DeclarationLines[i].TitleLarm.text = ''
					self.DeclarationLines[i].Larm.text = ''
					self.DeclarationLines[i].TitleRleg.text = ''
					self.DeclarationLines[i].Rleg.text = ''
					self.DeclarationLines[i].TitleLleg.text = ''
					self.DeclarationLines[i].Lleg.text = ''
					self.DeclarationLines[i].d.text = str(parent.Roaster[i].Pool)
				if parent.Roaster[i].Nature == "NPC":
					self.DeclarationLines[i].d.text = str(parent.Roaster[i].Pool[0])
					self.DeclarationLines[i].hd.text = str(parent.Roaster[i].Pool[1])
					self.DeclarationLines[i].wd.text = str(parent.Roaster[i].Pool[2])
					self.DeclarationLines[i].TitleHead.text = 'Head'
					self.DeclarationLines[i].Head.text = str(parent.Roaster[i].HP.Head)
					self.DeclarationLines[i].TitleTorso.text = 'Torso'
					self.DeclarationLines[i].Torso.text = str(parent.Roaster[i].HP.Torso)
					self.DeclarationLines[i].TitleRarm.text = 'Rarm'
					self.DeclarationLines[i].Rarm.text = str(parent.Roaster[i].HP.Rarm)
					self.DeclarationLines[i].TitleLarm.text = 'Larm'
					self.DeclarationLines[i].Larm.text = str(parent.Roaster[i].HP.Larm)
					self.DeclarationLines[i].TitleRleg.text = 'Rleg'
					self.DeclarationLines[i].Rleg.text = str(parent.Roaster[i].HP.Rleg)
					self.DeclarationLines[i].TitleLleg.text = 'Lleg'
					self.DeclarationLines[i].Lleg.text = str(parent.Roaster[i].HP.Lleg)
		for i in range(len(parent.Roaster),25):
			self.TestLayout.remove_widget(self.DeclarationLines[i].LineLayout)
			self.DeclarationLines[i].Activated = 0
			self.DeclarationLines[i].InRoaster = 0
	def UpdateRoaster(self,parent):
		self.Participants = len(parent.Roaster)
		for i in range(0,len(parent.Roaster)):
			parent.Roaster[i].Order = i
			if parent.Roaster[i].Nature != "Char":
				parent.Roaster[i].Defence = 0
				parent.Roaster[i].InstantDefence = 0
				if self.DeclarationLines[i].gobble.text.isdigit() and parent.Roaster[i].Defence != self.DeclarationLines[i].gobble.text:
					parent.Roaster[i].Defence = int(self.DeclarationLines[i].gobble.text)
					parent.Roaster[i].InstantDefence = parent.Roaster[i].Defence
				if parent.Roaster[i].Atk != self.DeclarationLines[i].Dam.text:
					parent.Roaster[i].Atk = self.DeclarationLines[i].Dam.text
				if parent.Roaster[i].AtkBonus != int(self.DeclarationLines[i].AtkBonus.text):
					parent.Roaster[i].AtkBonus = int(self.DeclarationLines[i].AtkBonus.text)
				if parent.Roaster[i].SpeedBonus != int(self.DeclarationLines[i].SpdBonus.text):
					parent.Roaster[i].SpeedBonus = int(self.DeclarationLines[i].SpdBonus.text)
				if parent.Roaster[i].Penetration != int(self.DeclarationLines[i].Penetration.text):
					parent.Roaster[i].Penetration = int(self.DeclarationLines[i].Penetration.text)
				if parent.Roaster[i].LAR != int(self.DeclarationLines[i].LAR.text):
					parent.Roaster[i].LAR = int(self.DeclarationLines[i].LAR.text)
				if parent.Roaster[i].MAR != int(self.DeclarationLines[i].MAR.text):
					parent.Roaster[i].MAR = int(self.DeclarationLines[i].MAR.text)
				if parent.Roaster[i].Nature == "Extra":
					parent.Roaster[i].Pool = int(self.DeclarationLines[i].d.text)
					self.DeclarationLines[i].hd.text = ''
					self.DeclarationLines[i].wd.text = ''
				if parent.Roaster[i].Nature == "NPC":
					parent.Roaster[i].Pool[0] = int(self.DeclarationLines[i].d.text)
					parent.Roaster[i].Pool[1] = int(self.DeclarationLines[i].hd.text)
					parent.Roaster[i].Pool[2] = int(self.DeclarationLines[i].wd.text)
					parent.Roaster[i].WD = parent.Roaster[i].Pool[2]
	def InsertSubMenu(self,i):
		for j in range(0,self.Participants):
			if self.DeclarationLines[j].Opened == 1 and i != j:
				self.Opened = 0
				self.DeclarationLines[j].Opened = 0
				self.RemoveSubMenu(j)
				self.DeclarationLines[j].LineLayout.remove_widget(self.DeclarationLines[j].Less)
				self.DeclarationLines[j].LineLayout.add_widget(self.DeclarationLines[j].More)
		self.DeclarationLines[i].Opened = 1
		self.Opened = 1
		Hauteur = self.TotalLayout.height * 0.8 - 100
		for j in range(i+1,self.Participants):
			Where = -(self.DeclarationLines[j].LineLayout.pos[1]-75)
			self.DeclarationLines[j].LineLayout.pos[1] -= 7*30
			self.DeclarationLines[j].InitY -= 7*30
			if (Where > Hauteur or Where < 0) and self.DeclarationLines[j].Activated == 1:
				self.TestLayout.remove_widget(self.DeclarationLines[j].LineLayout)
				self.DeclarationLines[j].Activated = 0
			elif (Where <= Hauteur and Where > 0) and self.DeclarationLines[j].Activated == 0\
				and self.DeclarationLines[j].InRoaster == 1:
				self.TestLayout.add_widget(self.DeclarationLines[j].LineLayout)
				self.DeclarationLines[j].Activated = 1
		self.TestLayout.add_widget(self.DeclarationLines[i].InfoSup)
		self.UpdateRoaster(self.Parent)
		self.Vslider.value = self.Vslider.value + 1
		self.Vslider.value = self.Vslider.value - 1
	def RemoveSubMenu(self,i):
		self.DeclarationLines[i].Opened = 0
		Hauteur = self.TotalLayout.height * 0.8 - 100
		for j in range(i+1,self.Participants):
			Where = -(self.DeclarationLines[j].LineLayout.pos[1]-75)
			self.DeclarationLines[j].LineLayout.pos[1] += 7*30
			self.DeclarationLines[j].InitY += 7*30
			if (Where > Hauteur or Where < 0) and self.DeclarationLines[j].Activated == 1:
				self.TestLayout.remove_widget(self.DeclarationLines[j].LineLayout)
				self.DeclarationLines[j].Activated = 0
			elif (Where <= Hauteur and Where > 0) and self.DeclarationLines[j].Activated == 0\
				and self.DeclarationLines[j].InRoaster == 1:
				self.TestLayout.add_widget(self.DeclarationLines[j].LineLayout)
				self.DeclarationLines[j].Activated = 1
		self.TestLayout.remove_widget(self.DeclarationLines[i].InfoSup)
		self.UpdateRoaster(self.Parent)
		self.Vslider.value = self.Vslider.value + 1
		self.Vslider.value = self.Vslider.value - 1
	def __init__(self,parent,s):
		self.Parent = parent
		self.Clearing = 0
		self.Participants = 25
		self.Opened = 0
		
		self.TotalLayout = FloatLayout(size = s, pos=(0,5000))
		
		self.TopLabel = Label(text='Declaration',font_size = 30,width = 80, height = 40,size_hint_y = 0\
			,pos_hint= {'x':0,'top':1},color = (1,1,1,1))
		
		self.MidwtScrollLayout = FloatLayout(pos_hint={'x':0,'top':0.90},width = 150,\
			height = 450,size_hint = (1,0.75))
		self.MidLayout = StackLayout(orientation = 'lr-tb',pos_hint = {'x':0,'top':1},\
			width = 470,size_hint=(None,None))
		self.MidTitleLayout = BoxLayout(orientation = 'horizontal',height = 30,\
			size_hint = (1,None))
		self.TestLayout = RelativeLayout(height = 500,\
			size_hint = (1,1),pos_hint = {'x':0,'top':1})
		
		self.BotLayout = BoxLayout(orientation='horizontal',size_hint = (1,0),\
			height = 40,pos_hint={'x':0,'y':0})
		
		self.Name = Label(text='Name',font_size = 20,width = 200, height = 20,size_hint = (None,1))
		self.d = Label(text='d',font_size = 20,width = 40, height = 20,size_hint = (None,1))
		self.hd = Label(text='hd',font_size = 20,width = 40, height = 20,size_hint = (None,1))
		self.wd = Label(text='wd',font_size = 20,width = 40, height = 20,size_hint = (None,1))
		self.gobble = Label(text='Def',font_size = 20,width = 40, height = 20,size_hint =(None,1))
		self.More = Label(text='',font_size = 20,width = 70, height = 20,size_hint =(None,1))
		self.MidTitleLayout.add_widget(self.Name)
		self.MidTitleLayout.add_widget(self.d)
		self.MidTitleLayout.add_widget(self.hd)
		self.MidTitleLayout.add_widget(self.wd)
		self.MidTitleLayout.add_widget(self.gobble)
		self.MidTitleLayout.add_widget(self.More)
		self.MidLayout.add_widget(self.MidTitleLayout)
		
		self.DeclarationLines = [DeclarationLine(self,i,i) for i in range(0,25)]
		self.TotalLayout.height = 450/0.75
		for i in range(0,25):
			if self.DeclarationLines[i].LineLayout.pos[1] >= -(self.TotalLayout.height*0.75 - 150):
				self.TestLayout.add_widget(self.DeclarationLines[i].LineLayout)
				self.DeclarationLines[i].Activated = 1
			else:
				self.DeclarationLines[i].Activated = 0
		
		self.MidLayout.add_widget(self.TestLayout)
		self.Vslider = Slider(orientation='vertical',pos_hint = {'right':0.97,'center_y':0.5},width = 20,\
			size_hint = (None,1),value = 100)
		self.MidwtScrollLayout.add_widget(self.MidLayout)
		self.MidwtScrollLayout.add_widget(self.Vslider)
		
		self.Hslider = Slider(orientation='horizontal',pos_hint = {'x':0,'center_y':0.13},height = 20,\
			size_hint = (1,None))
		
		self.Back = Button(text='Back',font_size = 20)
		self.Refresh = Button(text='Refresh',font_size = 20)
		self.NextRound = Button(text='Execute',font_size = 20)
		self.BotLayout.add_widget(self.Back)
		self.BotLayout.add_widget(self.Refresh)
		self.BotLayout.add_widget(self.NextRound)
		
		self.TotalLayout.add_widget(self.TopLabel)
		self.TotalLayout.add_widget(self.BotLayout)
		self.TotalLayout.add_widget(self.MidwtScrollLayout)
		self.TotalLayout.add_widget(self.Hslider)
		
		self.Back.bind(on_press=self.ReturnToInit)
		self.Refresh.bind(on_press=self.RefreshDisplay)
		self.NextRound.bind(on_press=self.ExecuteRound)
		self.Hslider.bind(value=self.HSliderSelect)
		self.Vslider.bind(value=self.VSliderSelect)
##############################################################################################################
##############################################################################################################
##############################################################################################################
class RoundColumns():
	def ImportValues(self,parent,grandparent):
		self.Name.text = parent.Participants[self.I].Name
		self.SValue.text = ''
		self.KValue.text = ''
		self.LValue.text = ''
		self.IsDamage.active = True
		self.IsHeal.active = False
		self.Burn.active = False
		self.Penetration.text = ''
		self.Engulf.active = False
		self.Electrocute.active = False
		if parent.Participants[self.I].Allied == 0:
			self.Name.color = [1,0.3,0.3,1]
		else:
			self.Name.color = [0.3,0.3,1,1]
		Rolled = parent.Participants[self.I].Rolled
		Val = range(1,11)
		self.Tallied = [[Rolled[i],Val[i]] for i in range(0,10)]
		self.Tallied.sort()
		DAMBONUS = parent.Participants[self.I].AtkBonus
		SPDBONUS = parent.Participants[self.I].SpeedBonus
		#Best set
		Largeur = self.Tallied[9][0]
		Hauteur = self.Tallied[9][1]
		if Largeur > 1:
			self.Result1.font_size = self.ResultFonts[Largeur+SPDBONUS]
			if DAMBONUS == 0 and SPDBONUS == 0:
				self.Result1.text = '[ref=0]%2.1i x %2.1i[/ref]'%(Largeur,Hauteur)
			elif DAMBONUS != 0 and SPDBONUS == 0:
				self.Result1.text = '[ref=0]%2.1i x %2.1i (+%i dam)[/ref]'%(Largeur,Hauteur,DAMBONUS)
			elif DAMBONUS == 0 and SPDBONUS != 0:
				self.Result1.text = '[ref=0]%2.1i x %2.1i (+%i spd)[/ref]'%(Largeur,Hauteur,SPDBONUS)
			elif DAMBONUS != 0 and SPDBONUS != 0:
				self.Result1.text = '[ref=0]%2.1i x %2.1i (+%i S +%i D)[/ref]'%(Largeur,Hauteur,SPDBONUS,DAMBONUS)
		else:
			self.Result1.text = ''
			self.Result1.font_size = self.ResultFonts[2]
		#Second best set
		Largeur = self.Tallied[8][0]
		Hauteur = self.Tallied[8][1]
		if Largeur > 1:
			self.Result2.font_size = self.ResultFonts[Largeur+SPDBONUS]
			if DAMBONUS == 0 and SPDBONUS == 0:
				self.Result2.text = '[ref=1]%2.1i x %2.1i[/ref]'%(Largeur,Hauteur)
			elif DAMBONUS != 0 and SPDBONUS == 0:
				self.Result2.text = '[ref=1]%2.1i x %2.1i (+%i dam)[/ref]'%(Largeur,Hauteur,DAMBONUS)
			elif DAMBONUS == 0 and SPDBONUS != 0:
				self.Result2.text = '[ref=1]%2.1i x %2.1i (+%i spd)[/ref]'%(Largeur,Hauteur,SPDBONUS)
			elif DAMBONUS != 0 and SPDBONUS != 0:
				self.Result2.text = '[ref=1]%2.1i x %2.1i (+%i S +%i D)[/ref]'%(Largeur,Hauteur,SPDBONUS,DAMBONUS)
		else:
			self.Result2.text = ''
			self.Result2.font_size = self.ResultFonts[2]
		#Third best set
		Largeur = self.Tallied[7][0]
		Hauteur = self.Tallied[7][1]
		if Largeur > 1:
			self.Result3.font_size = self.ResultFonts[Largeur+SPDBONUS]
			if DAMBONUS == 0 and SPDBONUS == 0:
				self.Result3.text = '[ref=2]%2.1i x %2.1i[/ref]'%(Largeur,Hauteur)
			elif DAMBONUS != 0 and SPDBONUS == 0:
				self.Result3.text = '[ref=2]%2.1i x %2.1i (+%i dam)[/ref]'%(Largeur,Hauteur,DAMBONUS)
			elif DAMBONUS == 0 and SPDBONUS != 0:
				self.Result3.text = '[ref=2]%2.1i x %2.1i (+%i spd)[/ref]'%(Largeur,Hauteur,SPDBONUS)
			elif DAMBONUS != 0 and SPDBONUS != 0:
				self.Result3.text = '[ref=2]%2.1i x %2.1i (+%i S +%i D)[/ref]'%(Largeur,Hauteur,SPDBONUS,DAMBONUS)
		else:
			self.Result3.text = ''
			self.Result3.font_size = self.ResultFonts[2]
		#Fourth best set
		Largeur = self.Tallied[6][0]
		Hauteur = self.Tallied[6][1]
		if Largeur > 1:
			self.Result4.font_size = self.ResultFonts[Largeur+SPDBONUS]
			if DAMBONUS == 0 and SPDBONUS == 0:
				self.Result4.text = '[ref=3]%2.1i x %2.1i[/ref]'%(Largeur,Hauteur)
			elif DAMBONUS != 0 and SPDBONUS == 0:
				self.Result4.text = '[ref=3]%2.1i x %2.1i (+%i dam)[/ref]'%(Largeur,Hauteur,DAMBONUS)
			elif DAMBONUS == 0 and SPDBONUS != 0:
				self.Result4.text = '[ref=3]%2.1i x %2.1i (+%i spd)[/ref]'%(Largeur,Hauteur,SPDBONUS)
			elif DAMBONUS != 0 and SPDBONUS != 0:
				self.Result4.text = '[ref=3]%2.1i x %2.1i (+%i S +%i D)[/ref]'%(Largeur,Hauteur,SPDBONUS,DAMBONUS)
		else:
			self.Result4.text = ''
			self.Result4.font_size = self.ResultFonts[2]
		#Least best set
		Largeur = self.Tallied[5][0]
		Hauteur = self.Tallied[5][1]
		if Largeur > 1:
			self.Result5.font_size = self.ResultFonts[Largeur+SPDBONUS]
			if DAMBONUS == 0 and SPDBONUS == 0:
				self.Result5.text = '[ref=4]%2.1i x %2.1i[/ref]'%(Largeur,Hauteur)
			elif DAMBONUS != 0 and SPDBONUS == 0:
				self.Result5.text = '[ref=4]%2.1i x %2.1i (+%i dam)[/ref]'%(Largeur,Hauteur,DAMBONUS)
			elif DAMBONUS == 0 and SPDBONUS != 0:
				self.Result5.text = '[ref=4]%2.1i x %2.1i (+%i spd)[/ref]'%(Largeur,Hauteur,SPDBONUS)
			elif DAMBONUS != 0 and SPDBONUS != 0:
				self.Result5.text = '[ref=4]%2.1i x %2.1i (+%i S +%i D)[/ref]'%(Largeur,Hauteur,SPDBONUS,DAMBONUS)
		else:
			self.Result5.text = ''
			self.Result5.font_size = self.ResultFonts[2]
		self.DamBon.text = 'Dam = (w + %i) %s'%(parent.Participants[self.I].AtkBonus,parent.Participants[self.I].Atk)
		#self.SpdBon.text = 'Spd = (w + %i)'%parent.Participants[self.I].SpeedBonus
		if parent.Participants[self.I].InstantDefence != 0:
			self.GobbleTitle.text = 'Gobble : %2.1i'%parent.Participants[self.I].InstantDefence
		else:
			self.GobbleTitle.text = 'Gobble : %2.1i'%0
			self.DefFrame.remove_widget(self.GobbleClick)
		if parent.Participants[self.I].Nature == "Extra":
			self.Head.text = 'HP     :  %4.1i'%parent.Participants[self.I].HP
			self.Torso.text = 'Unit   :  %4.1i'%parent.Participants[self.I].Nbr
			self.Larm.text = ''
			self.Rarm.text = ''
			self.Lleg.text = ''
			self.Rleg.text = ''
		if parent.Participants[self.I].Nature == "NPC":
			self.Head.text = 'Head   : %4.1i'%parent.Participants[self.I].HP.Head
			self.Torso.text = 'Torso  : %4.1i'%parent.Participants[self.I].HP.Torso
			self.Larm.text = 'L. arm : %4.1i'%parent.Participants[self.I].HP.Larm
			self.Rarm.text = 'R. arm : %4.1i'%parent.Participants[self.I].HP.Rarm
			self.Lleg.text = 'L. leg : %4.1i'%parent.Participants[self.I].HP.Lleg
			self.Rleg.text = 'R. leg : %4.1i'%parent.Participants[self.I].HP.Rleg
			self.NbrWiggle.text = 'Nbr of wiggle dice : %4.1i'%parent.Participants[self.I].WD
			self.OnesTitle.text = '%2.1ix  1 : '%parent.Participants[self.I].Rolled[0]
			self.TwosTitle.text = '%2.1ix  2 : '%parent.Participants[self.I].Rolled[1]
			self.ThreesTitle.text = '%2.1ix  3 : '%parent.Participants[self.I].Rolled[2]
			self.FoursTitle.text = '%2.1ix  4 : '%parent.Participants[self.I].Rolled[3]
			self.FivesTitle.text = '%2.1ix  5 : '%parent.Participants[self.I].Rolled[4]
			self.SixsTitle.text = '%2.1ix  6 : '%parent.Participants[self.I].Rolled[5]
			self.SevensTitle.text = '%2.1ix  7 : '%parent.Participants[self.I].Rolled[6]
			self.EightsTitle.text = '%2.1ix  8 : '%parent.Participants[self.I].Rolled[7]
			self.NinesTitle.text = '%2.1ix  9 : '%parent.Participants[self.I].Rolled[8]
			self.TensTitle.text = '%2.1ix 10 : '%parent.Participants[self.I].Rolled[9]
			if self.WiggleFrame.parent == None and parent.Participants[self.I].WD != 0:
				self.ColLayout.remove_widget(self.BonusFrame)
				self.ColLayout.remove_widget(self.DealHPFrame)
				self.ColLayout.remove_widget(self.HPFrame)
				self.ColLayout.add_widget(self.WiggleFrame)
			if self.WiggleFrame.parent != None and parent.Participants[self.I].WD == 0:
				self.ColLayout.remove_widget(self.WiggleFrame)
				self.ColLayout.add_widget(self.BonusFrame)
				self.ColLayout.add_widget(self.DealHPFrame)
				self.ColLayout.add_widget(self.HPFrame)
	def __init__(self,parent,grandparent,i,Largeur):
		self.Parent = parent
		self.GrandParent = grandparent
		self.I = i
		self.LargeFont = 20
		self.Font = 12
		self.ResultFonts = [10,11,12,16,20,20,20,20,20,20,20,20]
		self.Height = 25
		self.Tallied = []
		self.SpacerHeight = 5
		self.Width = Largeur
		self.NBR = len(parent.Participants)
		xFrac = 1
		self.FrameColor = (0.3,0.3,0.3)
		self.FrameLines = [40,0,self.Width-20,0]
		self.FrameWidth = 1
		if self.NBR != 0:
			xFrac = i*1.0/self.NBR
		self.ColLayout = BoxLayout(orientation='vertical',width = self.Width,\
			height = 20*self.Height + 3*self.SpacerHeight,size_hint=(None,1),pos_hint = {'x':xFrac,'bottom':0})
		
		#Name in column
		self.NameFrame = RelativeLayout(size = (self.Width,self.Height),size_hint = (None,1))
		self.Name = Label(text = 'Alexandre',font_size = self.LargeFont,size_hint=(1,1))
		self.NameFrame.add_widget(self.Name)
		with self.NameFrame.canvas:
			Color(self.FrameColor)
			Line(points = self.FrameLines,width = self.FrameWidth)
		
		#Bock to display up to 5 rolled pairs
		self.ResultsFrame = RelativeLayout(size = (self.Width,3*self.Height),size_hint = (None,3))
		self.RollResults = BoxLayout(orientation = 'vertical',width = self.Width,height = 3*self.Height\
			,size_hint=(1,1))
		self.Result1 = Label(text = '[ref=0]2x 8[/ref]',font_size =self.Font ,width = self.Width,\
			height = self.Height,size_hint=(None,1),markup=True)
		self.ResultsLigne2 = BoxLayout(orientation = 'horizontal',width = self.Width,height = self.Height\
			,size_hint=(None,1))
		self.Result2 = Label(text = '[ref=1]2x 6[/ref]',font_size = self.Font,height = self.Height,size_hint=(1,1),markup=True)
		self.Result3 = Label(text='[ref=2]2x 4[/ref]',font_size = self.Font,height = self.Height,size_hint=(1,1),markup=True)
		self.ResultsLigne2.add_widget(self.Result2)
		self.ResultsLigne2.add_widget(self.Result3)
		self.ResultsLigne3 = BoxLayout(orientation = 'horizontal',width = self.Width,height = self.Height\
			,size_hint=(None,1))
		self.Result4 = Label(text='[ref=3]2x 3[/ref]',font_size = self.Font,height = self.Height,size_hint=(1,1),markup=True)
		self.Result5 = Label(text='[ref=4]2x 1[/ref]',font_size = self.Font,height = self.Height,size_hint=(1,1),markup=True)
		self.ResultsLigne3.add_widget(self.Result4)
		self.ResultsLigne3.add_widget(self.Result5)
		self.RollResults.add_widget(self.Result1)
		self.RollResults.add_widget(self.ResultsLigne2)
		self.RollResults.add_widget(self.ResultsLigne3)
		with self.ResultsFrame.canvas:
			Color(self.FrameColor)
			Line(points = self.FrameLines,width = self.FrameWidth)
		self.ResultsFrame.add_widget(self.RollResults)
		
		#Block to dusplay bonuses to width for speed and damage. Also displays damage type
		self.BonusFrame = RelativeLayout(size = (self.Width,2*self.Height),size_hint = (None,2))
		self.Bonuses = BoxLayout(orientation = 'vertical',width = self.Width,height = 2*self.Height,size_hint=(None,1))
		self.DamBon = Label(text = 'Dam = (w + %i) %s'%(2,'SK'),font_size = self.Font,\
			size = (self.Width,self.Height),size_hint=(None,1))
		self.DefFrame = BoxLayout(orientation='horizontal',size = (self.Width,self.Height),size_hint=(1,1),padding = [50,0,50,0])
		#self.SpdBon = Label(text = 'Spd = (w + %i)'%1,font_size = self.Font,size = (self.Width,self.Height),size_hint=(None,1))
		self.GobbleTitle = Label(text='Gobbles : %2.1i'%0,size = (self.Width*1.0/2,self.Height),size_hint = (1,1),font_size = self.Font)
		self.GobbleClick = Button(text='Use 1 Gobble',size = (self.Width*1.0/2,self.Height),size_hint=(1,1),font_size = self.Font)
		self.DefFrame.add_widget(self.GobbleTitle)
		self.DefFrame.add_widget(self.GobbleClick)
		self.Bonuses.add_widget(self.DamBon)
		self.Bonuses.add_widget(self.DefFrame)
		with self.BonusFrame.canvas:
			Color(self.FrameColor)
			Line(points = self.FrameLines,width = self.FrameWidth)
		self.BonusFrame.add_widget(self.Bonuses)
		
		#Huge block for healing and applying damage
		self.DealHPFrame = RelativeLayout(size = (self.Width,2*self.Height),size_hint = (None,6))
		self.DealHP = BoxLayout(orientation='vertical',width = self.Width,height = 6*self.Height,size_hint=(None,1))
		self.HPType = BoxLayout(orientation = 'horizontal',size = (self.Width,self.Height),\
			size_hint=(1,1),spacing = 50,padding = [50,0,50,0])
		self.SLabel = Label(text='Shock',size = (self.Width*1.0/3,self.Height),\
			font_size= self.Font,size_hint=(1,1))
		self.KLabel = Label(text='Killing',size = (self.Width*1.0/3,self.Height),\
			font_size= self.Font,size_hint=(1,1))
		self.LLabel = Label(text='Location',size = (self.Width*1.0/3,self.Height),\
			font_size= self.Font,size_hint=(1,1))
		self.HPType.add_widget(self.SLabel)
		self.HPType.add_widget(self.KLabel)
		self.HPType.add_widget(self.LLabel)
		self.HPValue = BoxLayout(orientation = 'horizontal',size = (self.Width,self.Height),\
			size_hint=(1,1),spacing = 50,padding = [50,0,50,0])
		self.SValue = TextInput(text='',size = (self.Width*1.0/3,self.Height),\
			font_size= self.Font,size_hint=(1,None),padding = [6,6,6,6])
		self.KValue = TextInput(text='',size = (self.Width*1.0/3,self.Height),\
			font_size= self.Font,size_hint=(1,None),padding = [6,6,6,6])
		self.LValue = TextInput(text='',size = (self.Width*1.0/3,self.Height),\
			font_size= self.Font,size_hint=(1,None),padding = [6,6,6,6])
		self.HPValue.add_widget(self.SValue)
		self.HPValue.add_widget(self.KValue)
		self.HPValue.add_widget(self.LValue)
		self.LineType1 = BoxLayout(orientation = 'horizontal',size = (self.Width,self.Height),\
			size_hint = (1,1),padding = [50,0,50,0])
		self.IsDamLabel = Label(text='Damage',font_size = self.Font,height = self.Height,\
			size_hint=(1,1))
		self.IsDamage = CheckBox(active = 1,group='DamHeal%s'%self.I,height = self.Height,width = 15,\
			size_hint=(None,1))
		self.IsHealLabel = Label(text='Heal',font_size = self.Font,height = self.Height,\
			size_hint=(1,1))
		self.IsHeal = CheckBox(group='DamHeal%s'%self.I,height = self.Height,width = 15,\
			size_hint=(None,1))
		self.LineType1.add_widget(self.IsDamLabel)
		self.LineType1.add_widget(self.IsDamage)
		self.LineType1.add_widget(self.IsHealLabel)
		self.LineType1.add_widget(self.IsHeal)
		self.LineType2 = BoxLayout(orientation = 'horizontal',size = (self.Width,self.Height),\
			size_hint = (1,1),padding = [50,0,50,0])
		self.BurnLabel = Label(text='Burn',font_size = self.Font,height = self.Height,\
			size_hint=(1,1))
		self.Burn = CheckBox(height = self.Height,width = 15,size_hint=(None,None))
		self.DazeLabel = Label(text='Daze',font_size = self.Font,height = self.Height,\
			size_hint=(1,1))
		self.Daze = CheckBox(height = self.Height,width = 15,size_hint=(None,None))
		self.LineType2.add_widget(self.BurnLabel)
		self.LineType2.add_widget(self.Burn)
		self.LineType2.add_widget(self.DazeLabel)
		self.LineType2.add_widget(self.Daze)
		self.LineType3 = BoxLayout(orientation = 'horizontal',size = (self.Width,self.Height),\
			size_hint = (1,1),padding = [50,0,50,0])
		self.PenLabel = Label(text='Penetration',font_size = self.Font,height = self.Height,\
			size_hint=(1,1))
		self.Penetration = TextInput(text = '',height = self.Height,width = 30,font_size = self.Font,size_hint=(None,None))
		self.EngLabel = Label(text='Engulf',font_size = self.Font,height = self.Height,\
			size_hint=(1,1))
		self.Engulf = CheckBox(height = self.Height,width = 15,size_hint=(None,None))
		self.LineType3.add_widget(self.PenLabel)
		self.LineType3.add_widget(self.Penetration)
		self.LineType3.add_widget(self.EngLabel)
		self.LineType3.add_widget(self.Engulf)
		self.LineType4 = BoxLayout(orientation = 'horizontal',size = (self.Width,self.Height),\
			size_hint = (1,1),padding = [50,0,50,0])
		self.ElecLabel = Label(text='Electrocute',font_size = self.Font,height = self.Height,\
			size_hint=(1,1))
		self.Electrocute = CheckBox(height = self.Height,width = 15,size_hint=(None,None))
		self.DealLabel = Label(text='',font_size = self.Font,height = self.Height,width = 15,\
			size_hint=(None,1))
		self.Deal = Button(text = 'Execute',height = self.Height,size_hint=(1,None))
		self.LineType4.add_widget(self.ElecLabel)
		self.LineType4.add_widget(self.Electrocute)
		self.LineType4.add_widget(self.DealLabel)
		self.LineType4.add_widget(self.Deal)
		self.DealHP.add_widget(self.HPType)
		self.DealHP.add_widget(self.HPValue)
		self.DealHP.add_widget(self.LineType1)
		self.DealHP.add_widget(self.LineType2)
		self.DealHP.add_widget(self.LineType3)
		self.DealHP.add_widget(self.LineType4)
		with self.DealHPFrame.canvas:
			Color(self.FrameColor)
			Line(points = self.FrameLines,width = self.FrameWidth)
		self.DealHPFrame.add_widget(self.DealHP)
		
		#Display of current HP
		self.HPFrame = RelativeLayout(size = (self.Width,2*self.Height),size_hint = (None,3))
		self.HP = GridLayout(cols = 2,width = self.Width,height = 3*self.Height,size_hint=(None,1))
		self.Head = Label(text = 'Head   : %4.1i'%4,size = (self.Width/2.0,self.Height),\
			font_size = self.Font,size_hint = (None,None))
		self.Torso = Label(text = 'Torso  : %4.1i'%10,size = (self.Width/2.0,self.Height),\
			font_size = self.Font,size_hint = (None,None))
		self.Larm = Label(text = 'L. arm : %4.1i'%5,size = (self.Width/2.0,self.Height),\
			font_size = self.Font,size_hint = (None,None))
		self.Rarm = Label(text = 'R. arm : %4.1i'%5,size = (self.Width/2.0,self.Height),\
			font_size = self.Font,size_hint = (None,None))
		self.Lleg = Label(text = 'L. leg  : %4.1i'%5,size = (self.Width/2.0,self.Height),\
			font_size = self.Font,size_hint = (None,None))
		self.Rleg = Label(text = 'R. leg  : %4.1i'%5,size = (self.Width/2.0,self.Height),\
			font_size = self.Font,size_hint = (None,None))
		self.HP.add_widget(self.Head)
		self.HP.add_widget(self.Torso)
		self.HP.add_widget(self.Larm)
		self.HP.add_widget(self.Rarm)
		self.HP.add_widget(self.Lleg)
		self.HP.add_widget(self.Rleg)
		with self.HPFrame.canvas:
			Color(self.FrameColor)
			Line(points = self.FrameLines,width = self.FrameWidth)
		self.HPFrame.add_widget(self.HP)
		
		#Temporary menu dealing with wiggle dice
		self.WiggleFrame = RelativeLayout(size = (self.Width,9*self.Height),size_hint = (None,9))
		self.WiggleBox = BoxLayout(orientation='vertical',width = self.Width,height = 9*self.Height,size_hint=(None,1))
		self.NbrWiggle = Label(text = 'Nbr of wiggle dice : %4.1i'%0,size = (self.Width,self.Height),\
			font_size = self.Font,size_hint = (1,1))
		self.Spacer1Wiggle = Label(text = '',size = (self.Width,self.Height),\
			font_size = self.Font,size_hint = (1,1))
		#Line for 1s and 2s
		self.Line1Wiggle = BoxLayout(orientation='horizontal',width = self.Width,height = self.Height,size_hint=(1,1),padding=[50,1,50,1])
		self.OnesTitle = Label(text='%2.1ix  1  : '%0,height=self.Height,size_hint = (1,1))
		self.PlusOnes = Button(text='+1',font_size = self.Font,size=(self.Width*1.0/4,self.Height),size_hint=(1,1))
		self.TwosTitle = Label(text='%2.1ix  2  : '%0,height=self.Height,size_hint = (1,1))
		self.PlusTwos = Button(text='+1',font_size = self.Font,size=(self.Width*1.0/4,self.Height),size_hint=(1,1))
		self.Line1Wiggle.add_widget(self.OnesTitle)
		self.Line1Wiggle.add_widget(self.PlusOnes)
		self.Line1Wiggle.add_widget(self.TwosTitle)
		self.Line1Wiggle.add_widget(self.PlusTwos)
		#Line for 3s and 4s
		self.Line2Wiggle = BoxLayout(orientation='horizontal',width = self.Width,height = self.Height,size_hint=(1,1),padding=[50,1,50,1])
		self.ThreesTitle = Label(text='%2.1ix  3  : '%0,height=self.Height,size_hint = (1,1))
		self.PlusThrees = Button(text='+1',font_size = self.Font,size=(self.Width*1.0/4,self.Height),size_hint=(1,1))
		self.FoursTitle = Label(text='%2.1ix  4  : '%0,height=self.Height,size_hint = (1,1))
		self.PlusFours = Button(text='+1',font_size = self.Font,size=(self.Width*1.0/4,self.Height),size_hint=(1,1))
		self.Line2Wiggle.add_widget(self.ThreesTitle)
		self.Line2Wiggle.add_widget(self.PlusThrees)
		self.Line2Wiggle.add_widget(self.FoursTitle)
		self.Line2Wiggle.add_widget(self.PlusFours)
		#Line for 5s and 6s
		self.Line3Wiggle = BoxLayout(orientation='horizontal',width = self.Width,height = self.Height,size_hint=(1,1),padding=[50,1,50,1])
		self.FivesTitle = Label(text='%2.1ix  5  : '%0,height=self.Height,size_hint = (1,1))
		self.PlusFives = Button(text='+1',font_size = self.Font,size=(self.Width*1.0/4,self.Height),size_hint=(1,1))
		self.SixsTitle = Label(text='%2.1ix  6  : '%0,height=self.Height,size_hint = (1,1))
		self.PlusSixs = Button(text='+1',font_size = self.Font,size=(self.Width*1.0/4,self.Height),size_hint=(1,1))
		self.Line3Wiggle.add_widget(self.FivesTitle)
		self.Line3Wiggle.add_widget(self.PlusFives)
		self.Line3Wiggle.add_widget(self.SixsTitle)
		self.Line3Wiggle.add_widget(self.PlusSixs)
		#Line for 7s and 8s
		self.Line4Wiggle = BoxLayout(orientation='horizontal',width = self.Width,height = self.Height,size_hint=(1,1),padding=[50,1,50,1])
		self.SevensTitle = Label(text='%2.1ix  7  : '%0,height=self.Height,size_hint = (1,1))
		self.PlusSevens = Button(text='+1',font_size = self.Font,size=(self.Width*1.0/4,self.Height),size_hint=(1,1))
		self.EightsTitle = Label(text='%2.1ix  8  : '%0,height=self.Height,size_hint = (1,1))
		self.PlusEights = Button(text='+1',font_size = self.Font,size=(self.Width*1.0/4,self.Height),size_hint=(1,1))
		self.Line4Wiggle.add_widget(self.SevensTitle)
		self.Line4Wiggle.add_widget(self.PlusSevens)
		self.Line4Wiggle.add_widget(self.EightsTitle)
		self.Line4Wiggle.add_widget(self.PlusEights)
		#Line for 9s and 10s
		self.Line5Wiggle = BoxLayout(orientation='horizontal',width = self.Width,height = self.Height,size_hint=(1,1),padding=[50,1,50,1])
		self.NinesTitle = Label(text='%2.1ix  9  : '%0,height=self.Height,size_hint = (1,1))
		self.PlusNines = Button(text='+1',font_size = self.Font,size=(self.Width*1.0/4,self.Height),size_hint=(1,1))
		self.TensTitle = Label(text='%2.1ix 10 : '%0,height=self.Height,size_hint = (1,1))
		self.PlusTens = Button(text='+1',font_size = self.Font,size=(self.Width*1.0/4,self.Height),size_hint=(1,1))
		self.Line5Wiggle.add_widget(self.NinesTitle)
		self.Line5Wiggle.add_widget(self.PlusNines)
		self.Line5Wiggle.add_widget(self.TensTitle)
		self.Line5Wiggle.add_widget(self.PlusTens)
		self.WigDoneFrame = BoxLayout(orientation='horizontal',size=(self.Width,self.Height),size_hint=(1,1),padding=[100,0,100,0])
		self.WiggleDone = Button(text='Done!',width = self.Width*1.0,height = self.Height,size_hint=(1,1))
		self.WigDoneFrame.add_widget(self.WiggleDone)
		self.Spacer2Wiggle = Label(text = '',size = (self.Width,self.Height),\
			font_size = self.Font,size_hint = (1,1))

		self.WiggleBox.add_widget(self.NbrWiggle)
		self.WiggleBox.add_widget(self.Spacer1Wiggle)
		self.WiggleBox.add_widget(self.Line1Wiggle)
		self.WiggleBox.add_widget(self.Line2Wiggle)
		self.WiggleBox.add_widget(self.Line3Wiggle)
		self.WiggleBox.add_widget(self.Line4Wiggle)
		self.WiggleBox.add_widget(self.Line5Wiggle)
		self.WiggleBox.add_widget(self.Spacer2Wiggle)
		self.WiggleBox.add_widget(self.WigDoneFrame)
		with self.WiggleFrame.canvas:
			Color(self.FrameColor)
			Line(points = self.FrameLines,width = self.FrameWidth)
		self.WiggleFrame.add_widget(self.WiggleBox)
		
		self.ColLayout.add_widget(self.NameFrame)
		self.ColLayout.add_widget(self.ResultsFrame)
		self.ColLayout.add_widget(self.BonusFrame)
		self.ColLayout.add_widget(self.DealHPFrame)
		self.ColLayout.add_widget(self.HPFrame)

		self.Deal.bind(on_press = self.ExecuteHPModification)
		self.GobbleClick.bind(on_press = self.UseGobble)
		self.WiggleDone.bind(on_press = self.ExitWiggleMenu)
		self.PlusOnes.bind(on_press = self.AddOnes)
		self.PlusTwos.bind(on_press = self.AddTwos)
		self.PlusThrees.bind(on_press = self.AddThrees)
		self.PlusFours.bind(on_press = self.AddFours)
		self.PlusFives.bind(on_press = self.AddFives)
		self.PlusSixs.bind(on_press = self.AddSixs)
		self.PlusSevens.bind(on_press = self.AddSevens)
		self.PlusEights.bind(on_press = self.AddEights)
		self.PlusNines.bind(on_press = self.AddNines)
		self.PlusTens.bind(on_press = self.AddTens)
		self.Result1.bind(on_ref_press = self.ClickOnSet)
		self.Result2.bind(on_ref_press = self.ClickOnSet)
		self.Result3.bind(on_ref_press = self.ClickOnSet)
		self.Result4.bind(on_ref_press = self.ClickOnSet)
		self.Result5.bind(on_ref_press = self.ClickOnSet)
	def AddOnes(self,instance):
		if self.Parent.Participants[self.I].WD > 0:
			self.Parent.Participants[self.I].WD -= 1
			self.Parent.Participants[self.I].Rolled[0] += 1
			self.ImportValues(self.Parent,self.GrandParent)
		elif self.Parent.Participants[self.I].WD == 0:
			self.ColLayout.remove_widget(self.WiggleFrame)
			self.ColLayout.add_widget(self.BonusFrame)
			self.ColLayout.add_widget(self.DealHPFrame)
			self.ColLayout.add_widget(self.HPFrame)
	def AddTwos(self,instance):
		if self.Parent.Participants[self.I].WD > 0:
			self.Parent.Participants[self.I].WD -= 1
			self.Parent.Participants[self.I].Rolled[1] += 1
			self.ImportValues(self.Parent,self.GrandParent)
		elif self.Parent.Participants[self.I].WD == 0:
			self.ColLayout.remove_widget(self.WiggleFrame)
			self.ColLayout.add_widget(self.BonusFrame)
			self.ColLayout.add_widget(self.DealHPFrame)
			self.ColLayout.add_widget(self.HPFrame)
	def AddThrees(self,instance):
		if self.Parent.Participants[self.I].WD > 0:
			self.Parent.Participants[self.I].WD -= 1
			self.Parent.Participants[self.I].Rolled[2] += 1
			self.ImportValues(self.Parent,self.GrandParent)
		elif self.Parent.Participants[self.I].WD == 0:
			self.ColLayout.remove_widget(self.WiggleFrame)
			self.ColLayout.add_widget(self.BonusFrame)
			self.ColLayout.add_widget(self.DealHPFrame)
			self.ColLayout.add_widget(self.HPFrame)
	def AddFours(self,instance):
		if self.Parent.Participants[self.I].WD > 0:
			self.Parent.Participants[self.I].WD -= 1
			self.Parent.Participants[self.I].Rolled[3] += 1
			self.ImportValues(self.Parent,self.GrandParent)
		elif self.Parent.Participants[self.I].WD == 0:
			self.ColLayout.remove_widget(self.WiggleFrame)
			self.ColLayout.add_widget(self.BonusFrame)
			self.ColLayout.add_widget(self.DealHPFrame)
			self.ColLayout.add_widget(self.HPFrame)
	def AddFives(self,instance):
		if self.Parent.Participants[self.I].WD > 0:
			self.Parent.Participants[self.I].WD -= 1
			self.Parent.Participants[self.I].Rolled[4] += 1
			self.ImportValues(self.Parent,self.GrandParent)
		elif self.Parent.Participants[self.I].WD == 0:
			self.ColLayout.remove_widget(self.WiggleFrame)
			self.ColLayout.add_widget(self.BonusFrame)
			self.ColLayout.add_widget(self.DealHPFrame)
			self.ColLayout.add_widget(self.HPFrame)
	def AddSixs(self,instance):
		if self.Parent.Participants[self.I].WD > 0:
			self.Parent.Participants[self.I].WD -= 1
			self.Parent.Participants[self.I].Rolled[5] += 1
			self.ImportValues(self.Parent,self.GrandParent)
		elif self.Parent.Participants[self.I].WD == 0:
			self.ColLayout.remove_widget(self.WiggleFrame)
			self.ColLayout.add_widget(self.BonusFrame)
			self.ColLayout.add_widget(self.DealHPFrame)
			self.ColLayout.add_widget(self.HPFrame)
	def AddSevens(self,instance):
		if self.Parent.Participants[self.I].WD > 0:
			self.Parent.Participants[self.I].WD -= 1
			self.Parent.Participants[self.I].Rolled[6] += 1
			self.ImportValues(self.Parent,self.GrandParent)
		elif self.Parent.Participants[self.I].WD == 0:
			self.ColLayout.remove_widget(self.WiggleFrame)
			self.ColLayout.add_widget(self.BonusFrame)
			self.ColLayout.add_widget(self.DealHPFrame)
			self.ColLayout.add_widget(self.HPFrame)
	def AddEights(self,instance):
		if self.Parent.Participants[self.I].WD > 0:
			self.Parent.Participants[self.I].WD -= 1
			self.Parent.Participants[self.I].Rolled[7] += 1
			self.ImportValues(self.Parent,self.GrandParent)
		elif self.Parent.Participants[self.I].WD == 0:
			self.ColLayout.remove_widget(self.WiggleFrame)
			self.ColLayout.add_widget(self.BonusFrame)
			self.ColLayout.add_widget(self.DealHPFrame)
			self.ColLayout.add_widget(self.HPFrame)
	def AddNines(self,instance):
		if self.Parent.Participants[self.I].WD > 0:
			self.Parent.Participants[self.I].WD -= 1
			self.Parent.Participants[self.I].Rolled[8] += 1
			self.ImportValues(self.Parent,self.GrandParent)
		elif self.Parent.Participants[self.I].WD == 0:
			self.ColLayout.remove_widget(self.WiggleFrame)
			self.ColLayout.add_widget(self.BonusFrame)
			self.ColLayout.add_widget(self.DealHPFrame)
			self.ColLayout.add_widget(self.HPFrame)
	def AddTens(self,instance):
		if self.Parent.Participants[self.I].WD > 0:
			self.Parent.Participants[self.I].WD -= 1
			self.Parent.Participants[self.I].Rolled[9] += 1
			self.ImportValues(self.Parent,self.GrandParent)
		elif self.Parent.Participants[self.I].WD == 0:
			self.ColLayout.remove_widget(self.WiggleFrame)
			self.ColLayout.add_widget(self.BonusFrame)
			self.ColLayout.add_widget(self.DealHPFrame)
			self.ColLayout.add_widget(self.HPFrame)
	def ExecuteHPModification(self,instance):
		Shock = 0
		if self.SValue.text.isdigit():
			Shock = int(self.SValue.text)
		Kill = 0
		if self.KValue.text.isdigit():
			Kill = int(self.KValue.text)
		Location = 1
		if self.LValue.text.isdigit():
			Location = int(self.LValue.text)
		IsDamage = self.IsDamage.active
		IsHeal = self.IsHeal.active
		Burn = self.Burn.active
		Daze = self.Daze.active
		Penetration = None
		if self.Penetration.text.isdigit():
			Penetration = int(self.Penetration.text)
		Engulf = self.Engulf.active
		Electrocute = self.Electrocute.active
		if IsHeal == True:
			if Engulf == True:
				self.Parent.Participants[self.I].Heal(Shock+Kill,1,Engulf = 1)
			elif Engulf == False:
				self.Parent.Participants[self.I].Heal(Shock+Kill,Location,Engulf = None)
		if (IsDamage == True or (IsDamage == False and IsHeal == False)) and Electrocute == False and Burn == False:
			if Engulf == True:
				self.Parent.Participants[self.I].Damaged(Shock,Kill,Location,Pierced = Penetration,Engulf = 1,Burn = None)
			elif Engulf == False:
				self.Parent.Participants[self.I].Damaged(Shock,Kill,Location,Pierced = Penetration,Engulf = None,Burn = None)
		elif (IsDamage == True or (IsDamage == False and IsHeal == False)) and Electrocute == True and Burn == False:
			self.Parent.Participants[self.I].Electrocuted(Shock,Kill,Location,PP = Penetration)
		elif Burn == True:
			self.Parent.Participants[self.I].Damaged(Shock,Kill,Location,Pierced = None,Engulf = None,Burn = 1)
		self.ImportValues(self.Parent,self.GrandParent)
	def ClickOnSet(self,instance,value):
		i = 9-int(value)
		Nbr = self.Tallied[i][0]
		height = self.Tallied[i][1]-1
		self.Parent.Participants[self.I].Rolled[height] = 0
		self.ImportValues(self.Parent,self.GrandParent)
	def ExitWiggleMenu(self,instance):
		if self.Parent.Participants[self.I].WD == 0:
			self.ColLayout.remove_widget(self.WiggleFrame)
			self.ColLayout.add_widget(self.BonusFrame)
			self.ColLayout.add_widget(self.DealHPFrame)
			self.ColLayout.add_widget(self.HPFrame)
	def UseGobble(self,instance):
		if self.Parent.Participants[self.I].InstantDefence > 0:
			print "Use 1 Gobble"
			self.Parent.Participants[self.I].InstantDefence -= 1
			self.ImportValues(self.Parent,self.GrandParent)

class EndRoundConfirmation():
	def __init__(self,parent,grandparent,s):
		self.Parent = parent
		self.GrandParent = grandparent
		self.ConfLabel = Label(text='End round?',font_size = 20,bold = True,size = (200,40)\
			,pos_hint = {'center_x':0.5,'top':0.9},color = [0.9,0.9,0.9,1],size_hint = (0,0))
		self.Back = Button(text='Cancel',font_size = 20,size = (75,30),pos_hint = {'x':0.1,'y':0.1},size_hint=(0,0))
		self.Confirm = Button(text='Ok',font_size = 20,size = (75,30),pos_hint = {'right':0.9,'y':0.1},size_hint=(0,0))
		self.MenuLayout = RelativeLayout(size = s,pos_hint={'x':0,'y':0},size_hint=(1,1))
		with self.MenuLayout.canvas:
			Color(0.3,0.3,0.3)
			Rectangle(pos = (0,0),size = self.MenuLayout.size)
			Line(points = [0,0,0,s[1],s[0],s[1],s[0],0,0,0],width = 10)
		self.MenuLayout.add_widget(self.Back)
		self.MenuLayout.add_widget(self.Confirm)
		self.MenuLayout.add_widget(self.ConfLabel)
		self.TotalLayout = BoxLayout(size = s,pos_hint = {'center_x':0.5,'center_y':0.5},size_hint = (0,0))
		self.TotalLayout.add_widget(self.MenuLayout)
		self.Back.bind(on_press=self.Nothing)
		self.Confirm.bind(on_press=self.ClearBoard)
	def Nothing(self,instance):
		self.TotalLayout.clear_widgets()
		self.Parent.Clearing = 0
	def ClearBoard(self,instance):
		self.Parent.Clearing = 0
		if self.Parent.TotalLayout.pos == [0,0]:
			self.GrandParent.MenuInit.TotalLayout.pos = [0,5000]
			self.GrandParent.MenuDeclaration.TotalLayout.pos = [0,0]
			self.Parent.TotalLayout.pos = [0,5000]
		self.GrandParent.WhichRound += 1
		self.Parent.TopLabel.text = 'Round %i'%self.GrandParent.WhichRound
		self.TotalLayout.clear_widgets()

class RoundLayout():
	def StartNewRound(self):
		self.Participants = []
		for Char in self.Parent.Roaster:
			if Char.Nature != "Char" and Char.Alive != 0:
				self.Participants.append(Char)
		self.NBR = len(self.Participants)
		for i in range(0,self.NBR):
			self.Participants[i].Roll()
		self.MidLayout.clear_widgets()
		self.MidLayout.width = 350*len(self.Participants)+1
		self.ResolutionColumn = [RoundColumns(self,self.Parent,i,350) for i in range(0,self.NBR)]
		for i in range(0,self.NBR):
			self.MidLayout.add_widget(self.ResolutionColumn[i].ColLayout)
			self.ResolutionColumn[i].ImportValues(self,self.Parent)
	def ReturnToDeclaration(self,instante):
		for i in range(0,self.NBR):
			Order = self.Participants[i].Order
			self.Parent.Roaster[Order] = self.Participants[i]
		self.Parent.MenuDeclaration.LoadRoaster(self.Parent)
		if self.Clearing == 0:
			self.Clearing = 1
			self.MenuRoundClear = EndRoundConfirmation(self,self.Parent,(200,100))
			self.Parent.TotalLayout.add_widget(self.MenuRoundClear.TotalLayout)
	def BackToDeclaration(self,instance):
		for i in range(0,self.NBR):
			Order = self.Participants[i].Order
			self.Parent.Roaster[Order] = self.Participants[i]
		self.Parent.MenuDeclaration.LoadRoaster(self.Parent)
		if self.TotalLayout.pos == [0,0]:
			self.Parent.MenuInit.TotalLayout.pos = [0,5000]
			self.Parent.MenuDeclaration.TotalLayout.pos = [0,0]
			self.TotalLayout.pos = [0,5000]
	def HSliderSelect(self,instance,value):
		fenl = self.TotalLayout.width
		L = self.MidLayout.width
		DeltaL = L-fenl
		fenh = self.TotalLayout.height
		H = self.MidLayout.height
		DeltaH = L-fenl
		if L > fenl and H > fenh:
			self.MidLayout.pos_hint = {'x':(-(value/100.0)*DeltaL)/fenl,'top':(-(value/100.0)*DeltaH)/fenh}
		if L > fenl and H <= fenh:
			self.MidLayout.pos_hint = {'x':(-(value/100.0)*DeltaL)/fenl,'top':0.93}
	def __init__(self,parent,s):
		self.Parent = parent
		self.Clearing = 0
		self.Participants = parent.Roaster
		self.NBR = len(self.Participants)

		self.TopLabel = Label(text='Round %i'%parent.WhichRound,font_size = 30,width = 80, height = 40,size_hint_y = 0\
			,pos_hint= {'x':0,'top':1},color = (1,1,1,1))
		
		self.MidLayout = RelativeLayout(pos_hint={'x':0,'top':0.93},width = 150,\
			height = 450,size_hint = (None,0.75))
		
		self.BotLayout = BoxLayout(orientation='horizontal',size_hint = (1,0),\
			height = 40,pos_hint={'x':0,'y':0})
		
		self.TotalLayout = FloatLayout(size = s, pos=(0,5000))
		
		self.Back = Button(text='Back',font_size = 20)
		self.Next = Button(text='Next',font_size = 20)
		self.BotLayout.add_widget(self.Back)
		self.BotLayout.add_widget(self.Next)
		
		self.Hslider = Slider(orientation='horizontal',pos_hint = {'x':0,'center_y':0.13},height = 20,\
			size_hint = (1,None))
		
		self.ResolutionColumn = [RoundColumns(self,parent,i,300) for i in range(0,25)]
		
		self.TotalLayout.add_widget(self.TopLabel)
		self.TotalLayout.add_widget(self.BotLayout)
		self.TotalLayout.add_widget(self.MidLayout)
		self.TotalLayout.add_widget(self.Hslider)
		
		self.Back.bind(on_press=self.BackToDeclaration)
		self.Next.bind(on_press=self.ReturnToDeclaration)
		self.Hslider.bind(value=self.HSliderSelect)
##############################################################################################################
##############################################################################################################
##############################################################################################################

class ORE_DM_ToolApp(App):
	def build(self):
		self.TotalLayout = FloatLayout(size = (1000,1000))
		
		self.Roaster = []
		self.WhichRound = 1

		#MenuInit and Sub Menus
		self.MenuInit = InitLayout(self,(0,0))
		self.TotalLayout.add_widget(self.MenuInit.TotalLayout)
		
		#MenuDeclaration
		self.MenuDeclaration = DeclarationLayout(self,(0,0))
		self.TotalLayout.add_widget(self.MenuDeclaration.TotalLayout)
		
		#MenuRound
		self.MenuRound = RoundLayout(self,(0,0))
		self.TotalLayout.add_widget(self.MenuRound.TotalLayout)
		
		return self.TotalLayout
	def RunApp(self):
		self.run()
##############################################################################################################
##############################################################################################################
##############################################################################################################

test = ORE_DM_ToolApp()
test.RunApp()
'''
