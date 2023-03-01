# -*- coding: utf-8 -*-
"""
Created Feb 28 2023 for paramedic exam

@author: E. Krupczak

A little quiz program for the NREMT exam - flashcards 
Covers:
START triage
Abdominal organ quadrants 


"""

import random

#Make input compatible with python2
try: 
    get_input = raw_input
except NameError: 
    get_input = input

#Quiz data
START = {"Green": ["Ambulatory"],
	"Yellow": ["Resp < 30 /min, radial pulse, obey commands, not ambulatory"],
	"Red": ["Resp >= 30 /min, not ambulatory", "Resp < 30/min, no radial pulse, not ambulatory", "Resp < 30/min, radial pulse, does not obey commands, not ambulatory", "Respirations only after airway repositioned."],
	"Black": ["No respirations after airway repositioned."]}


Organs = {"LUQ" : ["Gallbladder", "Duodenum"],
         "RUQ" : ["Spleen", "Liver"],
	 "LLQ" : ["Sigmoid Colon", "Descending Colon"],
         "RLQ" : ["Appendix", "Ascending Colon"],
         "LLQ and RLQ" : ["Reproductive Organs", "Ureter"],
         "LUQ and RUQ": ["Stomach", "Adrenal Glands", "Kidneys", "Pancreas", "Transverse Colon"]}


def quiz_mechanism(quiz_dict):
    """
    Randomly select an element (tuple) from each key in quiz dict
    Return question string, answer string, and answer score
    """   
    answer, prompt_list = random.choice(list(quiz_dict.items()))
    prompt = random.choice(prompt_list)
    return answer, prompt

 

def quiz_display(quiz_dict, name):
    """
    Input/output for a quiz using the given quiz dictionary. 
    Works for GCS and APGAR
    """
    quizmode = "y"
    while quizmode == "y":
        answer, prompt = quiz_mechanism(quiz_dict)
        print(prompt)
        score = get_input("Please enter the "+name+" for the above: ")
        try:
            if score == answer: print("Correct!")
            else: print("Incorrect. Answer is "+answer)
        except ValueError: 
            print("Score must be an string")
        quizmode = get_input("Enter 'y' for another question, or anything else to exit. ")
        
        

if __name__== "__main__":
    quiz = get_input("Pick a quiz (START Score, Organ Quadrant): ")
    if quiz == "START Score":
        quiz_display(START, quiz)
    elif quiz == "Organ Quadrant":
        quiz_display(Organs, quiz)
    else: print("Invalid entry. Please try again and enter 'START Score' or 'Organ Quadrant' ")
