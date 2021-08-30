"""
Chris Francis (chris.francis@iitgn.ac.in)
Script to perform frequency analysis of tokens
"""

import pickle
import pandas as pd

open_file = open('tokens_list.pkl', "rb")
tokens_list = pickle.load(open_file)
open_file.close()

frequencies = pd.Series(tokens_list).value_counts()

print(frequencies[:20])

frequencies.to_csv('word_frequencies.csv')
