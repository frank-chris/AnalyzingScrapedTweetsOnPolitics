"""
Chris Francis (chris.francis@iitgn.ac.in)
Script to plot heaps law
"""
usage = "Usage:\n\n\
\
python3 heaps_law.py PKL_PATH\n\n\
\
* PKL_PATH: \n\
path to tokens list pkl file\n"

import pickle
import plotly.graph_objects as go

open_file = open('tokens_list.pkl', "rb")
tokens_list = pickle.load(open_file)
open_file.close()

x = []
y = []

uniq = set()

print(len(tokens_list), 'tokens')

for i, token in enumerate(tokens_list):
    uniq.add(token)
    x.append(i)
    y.append(len(uniq))

fig = go.Figure()

fig.add_trace(go.Scatter(x=x, y=y, name='empirical'))

fig.show()

