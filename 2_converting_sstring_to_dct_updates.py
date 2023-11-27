#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 09:13:44 2023

@author: yuktamehta
"""

import pandas as pd
df=pd.DataFrame(columns=["Disease","Sypmtoms"])
filename= "/Users/yuktamehta/Desktop/MS/Courses/Fall23/Data-270_Data_Analtyical_Processing/Project/output_data/diease_and_data.txt"
 
with open(filename, 'r') as text_file:
    lines = [line.strip() for line in text_file.readlines()]
    # skip first 3 lines
    lines = lines[3:]
    disease_mapping = {}
    key = ""
 
    for index, line in enumerate(lines):
        # read ahead next line
        try:
            next_line = lines[index + 1]
        except IndexError:
            next_line = None
            pass
       
        if line[0].isdigit():
            # if current line is digits only
            continue
 
        if next_line and next_line[0].isdigit():
            # the current line is the key
            disease_mapping[line] = []
            # save the key
            key = line
            continue
 
        # append the symptom
        if key in disease_mapping:
            disease_mapping[key].append(line)

df = pd.DataFrame(columns=['disease','symptoms'])  
for key in disease_mapping:
    row = disease_mapping[key]
    row1 = [key , row]
    df.loc[len(df)] = (row1) 
    #df= df.append({"disease":key,"syptoms":row})

df['symptoms'] = df['symptoms'].apply('|'.join)
df.to_csv("disease_and_spytoms.csv")