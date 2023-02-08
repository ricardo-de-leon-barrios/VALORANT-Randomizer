# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 23:39:57 2020
Last modification on Sun Jul 17 2022

@author: Ricardo de León
"""

import random as rn
from tkinter import *
from PIL import ImageTk,Image

class ValorantRandomChooser:
    
    def __init__(self):
        self.controllers = ['Brimstone', 'Viper', 'Omen', 'Astra', 'Harbor']
        self.sentinels = ['Killjoy', 'Cypher', 'Sage', 'Chamber']
        self.initiators = ['Sova', 'Breach', 'Skye', 'KAY/O', 'Fade']
        self.duelists = ['Phoenix', 'Jett', 'Reyna', 'Raze', 'Yoru', 'Neon']
        self.agents = self.controllers + self.sentinels + self.initiators + self.duelists
        self.sidearms = ['Classic', 'Shorty', 'Frenzy', 'Ghost', 'Sheriff']
        self.cheapWeapons = ['Stinger', 'Spectre', 'Bucky', 'Judge',
                             'Bulldog', 'Marshal', 'Ares']
        self.expensiveWeapons = ['Guardian', 'Phantom', 'Vandal', 'Operator', 'Odin']
        self.knife = ['Tactical Knife']
        self.weapons = self.sidearms + self.cheapWeapons + self.expensiveWeapons
        self.weaponsWKnife = self.weapons + self.knife
        
        self.dictionary = {'Brimstone': 'agent_01',
                           'Viper': 'agent_02',
                           'Omen': 'agent_03',
                           'Killjoy': 'agent_04',
                           'Cypher': 'agent_05',
                           'Sova': 'agent_06',
                           'Sage': 'agent_07',
                           'Phoenix': 'agent_09',
                           'Jett': 'agent_10',
                           'Reyna': 'agent_11',
                           'Raze': 'agent_12',
                           'Breach': 'agent_13',
                           'Skye': 'agent_14',
                           'Yoru': 'agent_15',
                           'Astra': 'agent_16',
                           'KAY/O': 'agent_17',
                           'Chamber': 'agent_18',
                           'Neon': 'agent_19',
                           'Fade': 'agent_20',
                           'Harbor': 'agent_21',
                           'Tactical Knife': 'weapon_00',
                           'Classic': 'weapon_01',
                           'Shorty': 'weapon_02',
                           'Frenzy': 'weapon_03',
                           'Ghost': 'weapon_04',
                           'Sheriff': 'weapon_05',
                           'Stinger': 'weapon_06',
                           'Spectre': 'weapon_07',
                           'Bucky': 'weapon_08',
                           'Judge': 'weapon_09',
                           'Bulldog': 'weapon_10',
                           'Guardian': 'weapon_11',
                           'Phantom': 'weapon_12',
                           'Vandal': 'weapon_13',
                           'Marshal': 'weapon_14',
                           'Operator': 'weapon_15',
                           'Ares': 'weapon_16',
                           'Odin': 'weapon_17'}
        
        window = Tk()
        window.title("VALORANT RULE-TAIM")
        
        frame1 = Frame(window)
        frame1.pack()   
        
        self.guiAgent = IntVar()
        agentLabel = Label(frame1, text = "Choose agents randomly")
        agentEntry = Entry(frame1, textvariable = self.guiAgent, justify = "right")
        agentButton = Button(frame1, text = "Choose", command = lambda: self.agentChooser(self.guiAgent.get()), bg = "white")        
        agentLabel.grid(row = 1, column = 1, sticky = E, pady = 3, padx = 3)        
        agentEntry.grid(row = 1, column = 2, pady = 3, padx = 3)        
        agentButton.grid(row = 1, column = 3, sticky = W, pady = 3, padx = 3)
                
        self.guiWeapon = IntVar()
        weaponLabel = Label(frame1, text = "Choose weapons randomly")
        weaponEntry = Entry(frame1, textvariable = self.guiWeapon, justify = "right")
        weaponButton = Button(frame1, text = "Choose", command = lambda: self.randomWeaponChooser(self.guiWeapon.get(),self.knifeVar.get()), bg = "white")        
        self.knifeVar = IntVar()
        checkKnife = Checkbutton(frame1, text="Knife?", variable=self.knifeVar)
        weaponLabel.grid(row = 2, column = 1, sticky = E, pady = 3, padx = 3)        
        weaponEntry.grid(row = 2, column = 2, pady = 3, padx = 3)        
        weaponButton.grid(row = 2, column = 3, sticky = W, pady = 3, padx = 3)
        checkKnife.grid(row = 2, column = 4, sticky = W, pady = 3, padx = 3)       
       
        self.imgFrame1 = Frame(window)
        self.imgFrame2 = Frame(window)
        self.imgFrame3 = Frame(window)
        self.imgFrame1.pack()
        self.imgFrame2.pack()
        self.imgFrame3.pack()
        
        extraFrame = Frame(window)
        extraFrame.pack()
        ordLabel = Label(extraFrame, text = "Choose agents randomly according to roles")
        ordLabel.grid(pady = 5)
        
        frame2 = Frame(window)
        frame2.pack()
        
        self.guiController = IntVar()
        self.guiDuelist = IntVar()
        self.guiInitiator = IntVar()
        self.guiSentinel = IntVar()
        controllerLabel = Label(frame2, text = "Controllers")
        controllerEntry = Entry(frame2, textvariable = self.guiController, justify = "right")
        duelistLabel = Label(frame2, text = "Duelists")
        duelistEntry = Entry(frame2, textvariable = self.guiDuelist, justify = "right")
        initiatorLabel = Label(frame2, text = "Initiators")
        initiatorEntry = Entry(frame2, textvariable = self.guiInitiator, justify = "right")
        sentinelLabel = Label(frame2, text = "Sentinels")
        sentinelEntry = Entry(frame2, textvariable = self.guiSentinel, justify = "right")
        controllerLabel.grid(row = 1, column = 1, sticky = E, pady = 3, padx = 3)
        duelistLabel.grid(row = 2, column = 1, sticky = E, pady = 3, padx = 3)      
        initiatorLabel.grid(row = 3, column = 1, sticky = E, pady = 3, padx = 3)
        sentinelLabel.grid(row = 4, column = 1, sticky = E, pady = 3, padx = 3)  
        controllerEntry.grid(row = 1, column = 2, pady = 3, padx = 3)
        duelistEntry.grid(row = 2, column = 2, pady = 3, padx = 3)      
        initiatorEntry.grid(row = 3, column = 2, pady = 3, padx = 3)
        sentinelEntry.grid(row = 4, column = 2, pady = 3, padx = 3)
        
        frame3 = Frame(window)
        frame3.pack()
        ordAgentButton = Button(frame3, text = "Choose", command = lambda: self.organizedAgentChooser(self.guiController.get(),self.guiDuelist.get(),self.guiInitiator.get(),self.guiSentinel.get()), bg = "white")
        ordAgentButton.grid(pady = 5)
        
        window.mainloop()
        
    def agentChooser(self, number):
        self.choices = rn.sample(range(len(self.agents)), number)
        self.chosenAgents = []
        self.chosenAgentsImg = []
        self.imgFrame1.config(width=1,height=1)
        self.imgFrame2.config(width=1,height=1)
        self.imgFrame3.config(width=1,height=1)
        for widget in self.imgFrame1.winfo_children():
            widget.destroy()
        for widget in self.imgFrame2.winfo_children():
            widget.destroy()
        for widget in self.imgFrame3.winfo_children():
            widget.destroy()
        for i in range(number):
            self.chosenAgents.append(self.agents[self.choices[i]])
        if number == 1:
            print('The chosen agent is', self.chosenAgents[0]+'.')
            toppy = Toplevel()
            text = 'The chosen agent is '+str(self.chosenAgents[0])+'.'
            label = Label(toppy, text=text).grid()
        elif number > 1:
            print('The chosen agents are', end = ' ')
            toppy = Toplevel()
            text = 'The chosen agents are '
            for j in range(len(self.chosenAgents) - 2):
                print(self.chosenAgents[j], end = ', ')
                text += str(self.chosenAgents[j])+', '
            print(self.chosenAgents[-2], 'and', self.chosenAgents[-1]+'.')
            text += str(self.chosenAgents[-2])+' and '+str(self.chosenAgents[-1])+'.'
            label = Label(toppy, text=text).pack()
        for x in self.chosenAgents:
            img = ImageTk.PhotoImage(Image.open('valorant/agents/'+self.dictionary[x]+'.png'))
            self.chosenAgentsImg.append(img)
        if len(self.chosenAgentsImg) <= 10:
            for x in self.chosenAgentsImg:
                Label(self.imgFrame1, image = x).pack(side = LEFT)
        elif len(self.chosenAgentsImg) > 10:
            for x in range(10):
                Label(self.imgFrame1, image = self.chosenAgentsImg[x]).pack(side = LEFT)
            for x in range(10,len(self.chosenAgentsImg)):
                Label(self.imgFrame2, image = self.chosenAgentsImg[x]).pack(side = LEFT)
                
    def organizedAgentChooser(self, n1, n2, n3, n4):
        self.chosenAgentsImg = []
        self.chosenAgents = []
        self.imgFrame1.config(width=1,height=1)
        self.imgFrame2.config(width=1,height=1)
        self.imgFrame3.config(width=1,height=1)
        for widget in self.imgFrame1.winfo_children():
            widget.destroy()
        for widget in self.imgFrame2.winfo_children():
            widget.destroy()
        for widget in self.imgFrame3.winfo_children():
            widget.destroy()
        self.choices1 = rn.sample(range(len(self.controllers)), n1)
        self.choices2 = rn.sample(range(len(self.duelists)), n2)
        self.choices3 = rn.sample(range(len(self.initiators)), n3)
        self.choices4 = rn.sample(range(len(self.sentinels)), n4)
        self.chosenControllers = []
        self.chosenDuelists = []
        self.chosenInitiators = []
        self.chosenSentinels = []
        for i in range(n1):
            self.chosenControllers.append(self.controllers[self.choices1[i]])
        for j in range(n2):
            self.chosenDuelists.append(self.duelists[self.choices2[j]])
        for k in range(n3):
            self.chosenInitiators.append(self.initiators[self.choices3[k]])
        for l in range(n4):
            self.chosenSentinels.append(self.sentinels[self.choices4[l]])
        self.chosenAgents = self.chosenControllers + self.chosenDuelists + self.chosenInitiators + self.chosenSentinels
        if len(self.chosenAgents) == 1:
            print('The chosen agent is', self.chosenAgents[0]+'.')
            toppy = Toplevel()
            text = 'The chosen agent is '+str(self.chosenAgents[0])+'.'
            label = Label(toppy, text=text).pack()
        elif len(self.chosenAgents) > 1:
            print('The chosen agents are', end = ' ')
            toppy = Toplevel()
            text = 'The chosen agents are '
            for m in range(len(self.chosenAgents) - 2):
                print(self.chosenAgents[m], end = ', ')
                text += str(self.chosenAgents[m])+', '
            print(self.chosenAgents[-2], 'and', self.chosenAgents[-1]+'.')
            text += str(self.chosenAgents[-2])+' and '+str(self.chosenAgents[-1])+'.'
            label = Label(toppy, text=text).pack()                
        for x in self.chosenAgents:
            img = ImageTk.PhotoImage(Image.open('valorant/agents/'+self.dictionary[x]+'.png'))
            self.chosenAgentsImg.append(img)
        if len(self.chosenAgentsImg) <= 10:
            for x in self.chosenAgentsImg:
                Label(self.imgFrame1, image = x).pack(side = LEFT)
        elif len(self.chosenAgentsImg) > 10:
            for x in range(10):
                Label(self.imgFrame1, image = self.chosenAgentsImg[x]).pack(side = LEFT)
            for x in range(10,len(self.chosenAgentsImg)):
                Label(self.imgFrame2, image = self.chosenAgentsImg[x]).pack(side = LEFT)
    
    def randomWeaponChooser(self, weapNumber, knife):
        self.chosenWeapsImg = []
        self.chosenWeaps1 = []
        self.imgFrame1.config(width=1,height=1)
        self.imgFrame2.config(width=1,height=1)
        self.imgFrame3.config(width=1,height=1)
        for widget in self.imgFrame1.winfo_children():
            widget.destroy()
        for widget in self.imgFrame2.winfo_children():
            widget.destroy()
        for widget in self.imgFrame3.winfo_children():
            widget.destroy()
        if knife == 1:
            self.weapChoices = rn.sample(range(len(self.weaponsWKnife)), weapNumber)
            self.usedWeaponsList = self.weaponsWKnife
        elif knife == 0:
            self.weapChoices = rn.sample(range(len(self.weapons)), weapNumber)
            self.usedWeaponsList = self.weapons
        self.chosenWeaps1 = []
        for i in range(weapNumber):
            self.chosenWeaps1.append(self.usedWeaponsList[self.weapChoices[i]])
        if len(self.chosenWeaps1) == 1:
            print('The chosen weapon is the', self.chosenWeaps1[0]+'.')
            toppy = Toplevel()
            text = 'The chosen weapon is the '+str(self.chosenWeaps1[0])+'.'
            label = Label(toppy, text=text).pack()
        elif len(self.chosenWeaps1) > 1:
            print('The chosen weapons are the', end = ' ')
            toppy = Toplevel()
            text = 'The chosen weapons are the '
            for k in range(len(self.chosenWeaps1) - 2):
                print(self.chosenWeaps1[k], end = ', ')
                text += str(self.chosenWeaps1[k])+', '
            print(self.chosenWeaps1[-2], 'and', self.chosenWeaps1[-1]+'.')
            text += str(self.chosenWeaps1[-2])+' and '+str(self.chosenWeaps1[-1])+'.'
            label = Label(toppy, text=text).pack()
        for x in self.chosenWeaps1:
            img = ImageTk.PhotoImage(Image.open('valorant/weapons/'+self.dictionary[x]+'.png'))
            self.chosenWeapsImg.append(img)
        if len(self.chosenWeapsImg) <= 6:
            for x in self.chosenWeapsImg:
                Label(self.imgFrame1, image = x).pack(side = LEFT)
        elif len(self.chosenWeapsImg) > 6 and len(self.chosenWeapsImg) <= 12:
            for x in range(6):
                Label(self.imgFrame1, image = self.chosenWeapsImg[x]).pack(side = LEFT)
            for x in range(6,len(self.chosenWeapsImg)):
                Label(self.imgFrame2, image = self.chosenWeapsImg[x]).pack(side = LEFT)
        elif len(self.chosenWeapsImg) > 12:
            for x in range(6):
                Label(self.imgFrame1, image = self.chosenWeapsImg[x]).pack(side = LEFT)
            for x in range(6,12):
                Label(self.imgFrame2, image = self.chosenWeapsImg[x]).pack(side = LEFT)
            for x in range(12,len(self.chosenWeapsImg)):
                Label(self.imgFrame3, image = self.chosenWeapsImg[x]).pack(side = LEFT)

ValorantRandomChooser()
