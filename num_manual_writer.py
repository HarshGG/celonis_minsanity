import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

#load csvs into dfs
df_event = pd.read_csv('pizza_event.csv')
df_case = pd.read_csv('Pizza_case.csv')
df_customerinfo = pd.read_csv('customer_info.csv')

case_keys = df_event['_CASE_KEY']
last_case_key = case_keys[len(case_keys)-1]
case_automations = df_event['Automation']

case_manuals = {}
case_automatics = {}

curr_case = 0

for x in range(len(case_keys)):
    if not(case_keys[x] in case_manuals):
        curr_case = case_keys[x]
        case_manuals[case_keys[x]] = 0
        case_automatics[case_keys[x]] = 0
    if(case_automations[x]=='A'):
        case_automatics[curr_case]+=1
    else:
        case_manuals[curr_case]+=1

header = ['_CASE_KEY', 'Automatics', 'Manuals']
toWrite = []

for x in case_manuals:
    arr = []
    arr.append(x)
    arr.append(case_automatics[x])
    arr.append(case_manuals[x])
    toWrite.append(arr)

print(toWrite)

with open('auto_vs_manual.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(toWrite)

