import jinja2
import pandas as pd
from tabulate import tabulate
from pandas import DataFrame

# open the file and read the contens
df = pd.read_csv("records.txt")

# Q1
'''
def scoreEval(score):
        if score >= 90:
                return 'A'
        elif score >= 80:
                return 'B'
        elif score >= 70:
                return 'C'
        elif sscore >= 60:
                return 'D'
        else:
                return 'F'

df['ece595'] = df['ece595'].apply(scoreEval)
df['ece547'] = df['ece547'].apply(scoreEval)
df['ece354'] = df['ece354'].apply(scoreEval)
print(tabulate(df, showindex=False, headers = df.columns, tablefmt = "grid"))
'''

# Q2
'''
df_score595 = df[df.ece595.eq(df['ece595'].max())].drop(columns = ['ece547', 'ece354'])
df_score595.columns = ['scorer', 'score']
df_score595.insert(0, 'subject', 'ece595')

df_score547 = df[df.ece547.eq(df['ece547'].max())].drop(columns = ['ece595', 'ece354'])
df_score547.columns = ['scorer', 'score']
df_score547.insert(0, 'subject', 'ece547')

df_score354 = df[df.ece354.eq(df['ece354'].max())].drop(columns = ['ece595', 'ece547'])
df_score354.columns = ['scorer', 'score']
df_score354.insert(0, 'subject', 'ece354')

df = pd.DataFrame(data = df_score595)
df = df.append(df_score547)
df = df.append(df_score354)
print(tabulate(df, showindex=False, headers = df.columns, tablefmt = "grid"))
'''

# Q3

def scoreEval(score):
        if score >= 90:
                return 4
        elif score >= 80:
                return 3
        elif score >= 70:
                return 2
        elif score >= 60:
                return 1
        else:
                return 0

df['ece595'] = df['ece595'].apply(scoreEval)
df['ece547'] = df['ece547'].apply(scoreEval)
df['ece354'] = df['ece354'].apply(scoreEval)
df['Gpa'] = df.mean(axis = 1).round(decimals = 3)
df = df.drop(['ece595', 'ece547', 'ece354'], axis = 1)
print(tabulate(df, showindex=False, headers = df.columns, tablefmt = "grid"))
