# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 17:56:18 2016

@author: mjm
"""

import pandas as pd
import codecs

my_file = codecs.open(r'DPM_MAM.csv', 'r', "utf8")
raw = pd.read_csv(my_file)
df = pd.DataFrame(raw, columns=["All","Name","Subject","Message","Date","PhoneNumber","Country", "Attachments"])

sLength = df['Message'].str.len()
df.loc[:,'Word_Cnt'] = pd.Series(sLength, index=df.index)

totalwrds = 0

for number in df['Word_Cnt']:
    totalwrds += number

allmsgs = len(df['Message'])

avgwrds = totalwrds/allmsgs

print(allmsgs)
print(avgwrds)
print(totalwrds)