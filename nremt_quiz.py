# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 10:48:16 2018

@author: E. Krupczak

A little quiz program for the NREMT
Covers GCS, APGAR, and rule of nines

Requires pandas (quiz info stored as pandas dataframe)
"""

import pandas as pd
import random

#Make compatible with python2
try: 
    get_input = raw_input
except NameError: 
    get_input = input

#Quiz data
GCS = pd.DataFrame( {1: ["Does not open eyes", "Makes no sounds", "Makes no movements"], 
                     2: ["Opens eyes in response to pain", "Incomprehensible sounds", "Extension to pain (decerebrate)"],
                     3: ["Opens eyes in response to voice", "Incoherent words", "Abnormal flexion to pain (decorticate)"],
                     4: ["Opens eyes spontaneously", "Confused/disoriented", "Flexion/withdrawal to pain"],
                     5: [None, "Oriented", "Localizes to painful stimuli"],
                     6: [None, None, "Obeys commands"]}, 
                        index = ["Eyes", "Verbal", "Motor"])


APGAR = pd.DataFrame({0: ["Blue or pale all over", "Absent pulse", "No response to stimulation", "No activity", "No respirations"],
                      1: ["Pink body; blue at extremities (acrocyanosis)", "Pulse <100 bpm", "Grimace on stimulation", "Some flexion", "Weak/irregular/gasping respirations"],
                      2: ["No cyanosis", "Pulse >100 bpm", "Cry on stimulation", "Flexed arms and legs that resist extension", "Strong cry"]}, 
                         index = ["Appearance", "Pulse", "Grimace", "Activity", "Respiration"])

nines_adult = {"Head": 9, "Arm": 9, "Torso": 36, "Leg": 18, "Genitals": 1}
nines_peds = {"Head": 18, "Arm": 9, "Torso": 36, "Leg": 14, "Genitals": 1}


#Quiz mechanism: Provide one element from each row, calculate score from column name
#GCS and APGAR mechanisms are basically the same
def GCS_quiz():
    quizmode = "y"
    while quizmode == "y":
        Eyes = random.randrange(1,5)
        Verbal = random.randrange(1,6)
        Motor = random.randrange(1,7)
    
        print(GCS.loc["Eyes", Eyes],",", GCS.loc["Verbal", Verbal],",", GCS.loc["Motor", Motor])
        score = get_input("Please enter GCS score: ")
        try:
            if int(score) == Eyes+Verbal+Motor: print("Correct!")
            else: print("Incorrect.")
        except ValueError: 
            print("Score must be an integer")
        print("GCS score: ", Eyes, "+", Verbal,"+", Motor, "=", Eyes+Verbal+Motor)
        quizmode = get_input("Enter 'y' for another question, or anything else to exit. ")
        
def APGAR_quiz():
    quizmode = "y"
    while quizmode == "y":
        Ap = random.randrange(0,3)
        P = random.randrange(0,3)
        G = random.randrange(0,3)
        Ac = random.randrange(0,3)
        R = random.randrange(0,3)
        
        print(APGAR.loc["Appearance", Ap],",", APGAR.loc["Pulse", P],",", APGAR.loc["Grimace",G], ",", APGAR.loc["Activity", Ac], ",", APGAR.loc["Respiration", R])
        score = get_input("Please enter APGAR score: ")
        try:
            if int(score) == Ap+P+G+Ac+R: print("Correct!")
            else: print("Incorrect.")
        except ValueError: 
            print("Score must be an integer")
        print("APGAR score: ", Ap, "+", P,"+",G,"+",Ac,"+",R, "=", Ap+P+G+Ac+R)
        quizmode = get_input("Enter 'y' for another question, or anything else to exit. ")
        
#The Rule of Nines quiz mechanism is a little messy. Allows for anterior, posterior or entire surface to be burned.
def nines_quiz():
    quizmode = "y"
    while quizmode == "y":
        planes = ["Anterior", "Posterior", "Entire"]
        sides = ["Left", "Right"]
        parts_list = [" ".join((k,l)) for k in sides for l in ["Arm", "Leg"]]+["Head", "Torso", "Genitals"]
        #parts_list = [" ".join((i,j)) for i in planes for j in ["Head", "Torso"]+[" ".join((k,l)) for k in sides for l in ["Arm", "Leg"]]]
        burned_parts = random.sample(parts_list, random.randrange(1, len(parts_list)))
        #burned_surface = [" ".join((i,j)) for i in random.sample(planes,1) for j in burned_parts]
        burned_surface =[]
        for j in burned_parts:
            burned_surface +=[" ".join((i,j)) for i in random.sample(planes,1)]
        
        #Select peds or adult
        pedsvsadult = random.randrange(0,2) #0=peds, 1 = adult
        burn_score = {}
        if pedsvsadult: #adult
            for part in burned_surface:
                for key in nines_adult.keys():
                    if key in part:
                        if "Entire" in part:
                            burn_score[part] = nines_adult[key]
                        else:
                            burn_score[part] = nines_adult[key]/2.0
        else: #peds
            for part in burned_surface:
                for key in nines_peds.keys():
                    if key in part:
                        if "Entire" in part:
                            burn_score[part] = nines_peds[key]
                        else:
                            burn_score[part] = nines_peds[key]/2.0  
        if pedsvsadult: 
            print("An adult has burned:", ", ".join(burned_surface))
        else:
            print("A child has burned:", ", ".join(burned_surface))
        score = get_input("Please enter the percentage of body burned: ")
        try:
            if float(score) == sum(burn_score.values()): print("Correct!")
            else: print("Incorrect")
        except ValueError:
            print("Burn percentage must be a number")
        print("Percentage burned: ", sum(burn_score.values()))
        for k, v in burn_score.items():
            print(k,":", v)
        quizmode = get_input("Enter 'y' for another question, or anything else to exit. ")

if __name__== "__main__":
    quiz = get_input("Pick a quiz (GCS, APGAR, nines): ")
    if quiz == "GCS":
        GCS_quiz()
    elif quiz == "APGAR":
        APGAR_quiz()
    elif quiz == "nines":
        nines_quiz()
    else: print("Invalid entry. Please try again and enter 'GCS', 'APGAR' or 'nines'.")
