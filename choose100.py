"""
Chris Francis (chris.francis@iitgn.ac.in)
Script to pick 100 tweets than meet the required criteria
"""
usage = "Usage:\n\n\
\
python3 choose100.py CSV_PATH\n\n\
\
* CSV_PATH: \n\
path to the main combined csv file\n"

from ast import literal_eval
import pandas as pd
import sys


data_df = pd.read_csv(sys.argv[1], sep='\t', dtype={'place':str})

data_df['hashtags'].fillna(value='[]', inplace=True)
data_df['mentions'].fillna(value='[]', inplace=True)

data_df = data_df.sample(frac=1)

output_df = dict()
output_df['id'] = []
output_df['tweet'] = []
output_df['language'] = []

tweets_chosen = 0

for index, row in data_df.iterrows():
    n_hashtags = len(literal_eval(row['hashtags']))
    n_mentions = len(literal_eval(row['mentions']))

    n_tokens = len(row['tweet'].split())

    if n_tokens - n_hashtags - n_mentions > 8 and row['id'] > 1:
        tweets_chosen += 1
        output_df['id'].append(row['id'])
        output_df['tweet'].append(row['tweet'])
        output_df['language'].append(row['language'])

    if tweets_chosen > 150:
        break

output_df = pd.DataFrame(output_df)

output_df.to_csv(sys.argv[1].replace('.csv', '_100.csv'), index=False)