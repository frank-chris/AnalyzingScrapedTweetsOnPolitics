"""
Chris Francis (chris.francis@iitgn.ac.in)
Script to save the list of tokens from all tweets
"""
usage = "Usage:\n\n\
\
python3 tokenize_tweets.py CSV_PATH [CSV_PATH ...]\n\n\
\
* CSV_PATH: \n\
path to a main combined csv file\n"

import pandas as pd 
import sys
import re,string
import pickle

dataframe_list = []

for f_path in sys.argv[1:]:
    df = pd.read_csv(f_path, sep='\t', dtype={'place':str})
    dataframe_list.append(df)

data_df = pd.concat(dataframe_list, ignore_index=True)

tweets_list = [str(x) for x in list(data_df['tweet'])]
tweets_str = ' '.join(tweets_list)

tokens_list = tweets_str.split()

open_file = open('tokens_list.pkl', "wb")
pickle.dump(tokens_list, open_file)
open_file.close()