# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 18:07:32 2016

@author: mjm
"""

import pandas as pd
import codecs
import nltk
from collections import OrderedDict

my_file = codecs.open(r'DPM_MAM.csv', 'r', "utf8")
raw = pd.read_csv(my_file)
df = pd.DataFrame(raw, columns=["All","Name","Subject","Message","Date","PhoneNumber","Country", "Attachments"])

words = raw.Message.to_string()
tokens = nltk.word_tokenize(words)
pos = nltk.pos_tag(tokens)

def commontag(taggedbook):
    tag_dict={}
    for (word, tag) in taggedbook:
        if tag in tag_dict:
            tag_dict[tag]+=1
        else:
            tag_dict[tag] =1
    tag_dict = OrderedDict(sorted(tag_dict.items(), key = lambda t: t[1]))
    print(tag_dict)
    
commontag(pos)

