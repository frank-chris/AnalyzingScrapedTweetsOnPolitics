"""
Chris Francis (chris.francis@iitgn.ac.in)
Script to plot heaps law
"""

import pickle
import plotly.graph_objects as go
from tqdm import tqdm

open_file = open('tokens_list.pkl', "rb")
tokens_list = pickle.load(open_file)
open_file.close()

x = []
y = []

uniq = set()

i = 0
for token in tqdm(tokens_list):
    if not token.startswith('#') and not token.startswith('@'):
        i+=1
        uniq.add(token)
        x.append(i)
        y.append(len(uniq))

fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y, name='empirical'))
fig.show()

