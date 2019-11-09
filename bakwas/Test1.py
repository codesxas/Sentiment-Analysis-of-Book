import pandas as pd, numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('sentiments.xlsx')
pos = df.loc[df['Positive'] == 1, 'Words'].copy().reset_index(drop = True)
pos = pd.concat([pd.DataFrame(pos)], 1)
neg = df.loc[df['Negative'] == 1, 'Words'].copy().reset_index(drop = True)
neg = pd.concat([pd.DataFrame(neg)], 1)
anger = df.loc[df['Anger'] == 1, 'Words'].copy().reset_index(drop = True)
anger = pd.concat([pd.DataFrame(anger)], 1)
fear = df.loc[df['Fear'] == 1, 'Words'].copy().reset_index(drop = True)
fear = pd.concat([pd.DataFrame(fear)], 1)
joy = df.loc[df['Joy'] == 1, 'Words'].copy().reset_index(drop = True)
joy = pd.concat([pd.DataFrame(joy)], 1)
sad = df.loc[df['Sadness'] == 1, 'Words'].copy().reset_index(drop = True)
sad = pd.concat([pd.DataFrame(sad)], 1)
suprise = df.loc[df['Surprise'] == 1, 'Words'].copy().reset_index(drop = True)
suprise = pd.concat([pd.DataFrame(suprise)], 1)
trust = df.loc[df['Trust'] == 1, 'Words'].copy().reset_index(drop = True)
trust = pd.concat([pd.DataFrame(trust)], 1)

print(pos.head())

lens = pos['Words'].str.len()


plt.hist(lens, bins=25)
plt.show()