"""
Chris Francis (chris.francis@iitgn.ac.in)
Script to plot heaps law
"""

import pickle
import plotly.graph_objects as go
from scipy.optimize import curve_fit
from tqdm import tqdm
import numpy as np

def exp_func(x, k, b):
    return k*(x**b)

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
fig.add_trace(go.Scatter(x=x, y=y, name='empirical curve'))

popt, pcov = curve_fit(exp_func, x, y)
x_fit = np.linspace(min(x), max(x), 1000)
y_fit = [exp_func(x, popt[0], popt[1]) for x in x_fit]

fig.add_trace(go.Scatter(x=x_fit, y=y_fit, name='fitted curve'))

anno = "Parameters of fitted curve: K = " + str(round(popt[0], 3)) + ", Beta = " + str(round(popt[1], 3))

fig.update_layout(title_text="|V| vs N (Heaps' Law) - " + anno, 
                    yaxis_title='|V|', 
                    xaxis_title='N', 
                    font_size = 18)
fig.show()

