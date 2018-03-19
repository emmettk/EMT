# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 10:48:16 2018

@author: E. Krupczak

A little quiz program for the NREMT exam
Covers GCS, APGAR, and rule of nines

No effort has been made to have the scores in each category correlate,
i.e. don't ask me to explain the infant with no pulse but a strong cry! :) 

"""

import random

#Make input compatible with python2
try: 
    get_input = raw_input
except NameError: 
    get_input = input

#Quiz data
GCS = {"Eyes"  : [("Does not open eyes", 1), ("Opens eyes in response to pain",2), 
                  ("Opens eyes in response to voice",3), ("Opens eyes spontaneously",4)],
       "Verbal": [("Makes no sounds",1), ("Incomprehensible sounds",2), 
                  ("Incoherent words",3), ("Confused/disoriented",4), ("Oriented",5)],
       "Motor" : [("Makes no movements",1), ("Extension to pain (decerebrate)",2),
                  ("Abnormal flexion to pain (decorticate)",3), ("Flexion/withdrawal to pain",4),
                  ("Localizes to painful stimuli",5), ("Obeys commands",6)]}

APGAR = {"Appearance" : [("Blue or pale all over",0), ("Pink body; blue at extremities (acrocyanosis)",1), ("No cyanosis",2)],
         "Pulse"      : [("Absent pulse",0), ("Pulse <100 bpm",1), ("Pulse >100 bpm",2)],
         "Grimace"    : [("No response to stimulation", 0), ("Grimace on stimulation", 1), ("Cry on stimulation", 2)],
         "Activity"   : [("No activity", 0), ("Some flexion", 1), ("Flexed arms and legs that resist extension", 2)],
         "Respiration": [("No respirations",0), ("Weak/irregular/gasping respirations",1), ("Strong cry", 2)]}

nines_adult = {"Head": 9, "Arm": 9, "Torso": 36, "Leg": 18, "Genitals": 1}
nines_peds = {"Head": 18, "Arm": 9, "Torso": 36, "Leg": 14, "Genitals": 1}


def quiz_mechanism(quiz_dict):
    """
    Quiz mechanism for GCS and APGAR 
    Randomly select an element (tuple) from each key in quiz dict
    Return question string, answer string, and answer score
    """   
    question = []
    answer = []
    for k,v in quiz_dict.items():
        element = random.choice(v)
        question.append(element[0])
        answer.append(element[1])
    return ", ".join(question), "+".join([str(i) for i in answer])+"="+str(sum(answer)), sum(answer)

def quiz_display(quiz_dict, name):
    """
    Input/output for a quiz using the given quiz dictionary. 
    Works for GCS and APGAR
    """
    quizmode = "y"
    while quizmode == "y":
        question, answer, answer_score = quiz_mechanism(quiz_dict)
        print(question)
        score = get_input("Please enter "+name+" score for the patient described above: ")
        try:
            if int(score) == answer_score: print("Correct!")
            else: print("Incorrect.")
        except ValueError: 
            print("Score must be an integer")
        print(name+" score: "+answer)
        quizmode = get_input("Enter 'y' for another question, or anything else to exit. ")
        
        
#The Rule of Nines quiz mechanism is a little messy. 
def nines_quiz():
    """
    Rule of Nines quiz.
    Allows for anterior, posterior or entire surface to be burned.
    Randomly selects pediatric or adult.
    """
    quizmode = "y"
    while quizmode == "y":
        planes = ["Anterior", "Posterior", "Entire"]
        sides = ["Left", "Right"]
        #List all possible body parts that can be burned
        parts_list = [" ".join((k,l)) for k in sides for l in ["Arm", "Leg"]]+["Head", "Torso", "Genitals"]
        #Choose which parts are burned
        burned_parts = random.sample(parts_list, random.randrange(1, len(parts_list)))
        #Choose if each part is burned on anterior, posterior or both
        burned_surface =[]
        for j in burned_parts:
            burned_surface +=[" ".join((i,j)) for i in random.sample(planes,1)]
        #Calculate the percentage burned from the list of burned parts
        def get_burn_score(burned_surface, nines_dict):
            burn_score = {}
            for part in burned_surface:
                for key in nines_dict.keys():
                    if key in part:
                        if "Entire" in part: #The whole area is burned
                            burn_score[part] = float(nines_dict[key])
                        else: #Anterior or posterior: half the area is burned
                            burn_score[part] = nines_dict[key]/2.0
            return burn_score
        #Select pediatric or adult
        pedsvsadult = random.randint(0,1) #0=peds, 1 = adult        
        if pedsvsadult: #adult
            burn_score = get_burn_score(burned_surface, nines_adult)
        else: #pediatric
            burn_score = get_burn_score(burned_surface, nines_peds)
        
        #Print the quiz
        if pedsvsadult: 
            print("An adult has burned: "+ ", ".join(burned_surface))
        else:
            print("A child has burned: "+ ", ".join(burned_surface))
        score = get_input("Please enter the percentage of body burned: ")
        try:
            if float(score) == sum(burn_score.values()): print("Correct!")
            else: print("Incorrect")
        except ValueError:
            print("Burn percentage must be a number.")
        print("Percentage burned: "+ str(sum(burn_score.values())))
        for k, v in burn_score.items():
            print(k+": "+ str(v))
        quizmode = get_input("Enter 'y' for another question, or anything else to exit. ")

if __name__== "__main__":
    quiz = get_input("Pick a quiz (GCS, APGAR, nines): ")
    if quiz == "GCS":
        quiz_display(GCS, quiz)
    elif quiz == "APGAR":
        quiz_display(APGAR, quiz)
    elif quiz == "nines":
        nines_quiz()
    else: print("Invalid entry. Please try again and enter 'GCS', 'APGAR' or 'nines'.")
