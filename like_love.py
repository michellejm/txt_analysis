# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 18:15:49 2016

@author: mjm
"""

import pandas as pd
import codecs
import nltk

my_file = codecs.open(r'DPM_MAM.csv', 'r', "utf8")
raw = pd.read_csv(my_file)
df = pd.DataFrame(raw, columns=["All","Name","Subject","Message","Date","PhoneNumber","Country", "Attachments"])

#words = df['Message']
words = raw.Message.to_string()
tokens = nltk.word_tokenize(words)
my_txt = nltk.Text(tokens)

likelove = my_txt.similar("love")

print(likelove)