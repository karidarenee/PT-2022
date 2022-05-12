# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 12:37:59 2022

@author: jcarb
"""

import pandas as pd
import numpy as np

# Import the CSV file with only useful columns
# source: https://www.data.gouv.fr/fr/datasets/temperature-quotidienne-departementale-depuis-janvier-2018/
#df = pd.read_csv("temperature-quotidienne-departementale.csv", sep=";", usecols=[0,1,4])

# Rename columns to simplify syntax
#df = df.rename(columns={"date_obs":"Date","code_insee_departement": "Region", "tmax": "Temp"})

# Select 2019 records only
#df = df[(df["Date"]>="2019-01-01") & (df["Date"]<="2019-12-31")]

# Pivot table to get "Date" as index and regions as columns 
#df = df.pivot(index='Date', columns='Region', values='Temp')

# Select a set of regions across France
#df = df[["06","25","59","62","83","85","75"]]

dfx = pd.read_csv("GRFx.csv", sep=",")[1:21]
dfx.set_index("ID", inplace=True)
dfx = dfx.T

dfy = pd.read_csv("GRFy.csv", sep=",")[1:21]
dfy.set_index("ID", inplace=True)
dfy = dfy.T

dfz = pd.read_csv("GRFz.csv", sep=",")[1:21]
dfz.set_index("ID", inplace=True)
dfz = dfz.T


# Convert the Pandas dataframe to a Numpy array with time-series only
fx = dfx.to_numpy().astype(float)
fy = dfy.to_numpy().astype(float)
fz = dfz.to_numpy().astype(float)

# Create a float vector between 0 and 1 for time index
timex = np.linspace(0,1,len(fx))
timey = np.linspace(0,1,len(fy))
timez = np.linspace(0,1,len(fz))



from fdasrsf import fPCA, time_warping, fdawarp, fdahpca

# Functional Alignment
# Align time-series
warp_fx = time_warping.fdawarp(fx, timex)
warp_fy = time_warping.fdawarp(fy, timey)
warp_fz = time_warping.fdawarp(fz, timez)


warp_fx.srsf_align(MaxItr = 10)
warp_fy.srsf_align(MaxItr = 10)
warp_fz.srsf_align(MaxItr = 10)

fPCA_analysisx = fPCA.fdavpca(warp_fx)
fPCA_analysisy = fPCA.fdavpca(warp_fy)
fPCA_analysisz = fPCA.fdavpca(warp_fz)

# Run the FPCA on a 3 components basis 
fPCA_analysisx.calc_fpca(no=3)
fPCA_analysisx.plot()
fPCA_analysisy.calc_fpca(no=3)
fPCA_analysisy.plot()
fPCA_analysisz.calc_fpca(no=3)
fPCA_analysisz.plot()


import plotly.graph_objects as go

# Plot of the 3 functions
fig = go.Figure()

# Add traces
fig.add_trace(go.Scatter(y=fPCA_analysisx.f_pca[:,0,0], mode='lines', name="PC1"))
fig.add_trace(go.Scatter(y=fPCA_analysisx.f_pca[:,0,1], mode='lines', name="PC2"))
fig.add_trace(go.Scatter(y=fPCA_analysisx.f_pca[:,0,2], mode='lines', name="PC3"))

fig.update_layout(
    title_text='<b>Principal Components Analysis Functions - GRFx</b>', title_x=0.5, xaxis_title="Time", yaxis_title = "Principal Components"
)
fig.write_html('GRFx-PCs.html', auto_open=True)


fPCA_coefx = fPCA_analysisx.coef

# Plot of PCs against regions
fig = go.Figure(data=go.Scatter(x=fPCA_coefx[:,0], y=fPCA_coefx[:,1], mode='markers+text', text=dfx.columns))

fig.update_traces(textposition='top center')
fig.update_layout(
    title_text='<b>Functional Principal Components Analysis - GRFx</b>', title_x=0.5, xaxis_title="PC1", yaxis_title = "PC2"
)
fig.write_html('GRFx-Points.html', auto_open=True)



fig = go.Figure()

# Add traces
fig.add_trace(go.Scatter(y=fPCA_analysisy.f_pca[:,0,0], mode='lines', name="PC1"))
fig.add_trace(go.Scatter(y=fPCA_analysisy.f_pca[:,0,1], mode='lines', name="PC2"))
fig.add_trace(go.Scatter(y=fPCA_analysisy.f_pca[:,0,2], mode='lines', name="PC3"))

fig.update_layout(
   title_text='<b>Principal Components Analysis Functions - GRFy</b>', title_x=0.5, xaxis_title="Time", yaxis_title = "Principal Components"
)
fig.write_html('GRFy-PCs.html', auto_open=True)


fPCA_coefy = fPCA_analysisy.coef

# Plot of PCs against regions
fig = go.Figure(data=go.Scatter(x=fPCA_coefy[:,0], y=fPCA_coefy[:,1], mode='markers+text', text=dfy.columns))

fig.update_traces(textposition='top center')
fig.update_layout(
    title_text='<b>Functional Principal Components Analysis - GRFy</b>', title_x=0.5, xaxis_title="PC1", yaxis_title = "PC2"
)
fig.write_html('GRFy-Points.html', auto_open=True)





fig = go.Figure()

# Add traces
fig.add_trace(go.Scatter(y=fPCA_analysisz.f_pca[:,0,0], mode='lines', name="PC1"))
fig.add_trace(go.Scatter(y=fPCA_analysisz.f_pca[:,0,1], mode='lines', name="PC2"))
fig.add_trace(go.Scatter(y=fPCA_analysisz.f_pca[:,0,2], mode='lines', name="PC3"))

fig.update_layout(
    title_text='<b>Principal Components Analysis Functions - GRFz</b>', title_x=0.5, xaxis_title="Time", yaxis_title = "Principal Components"
)
fig.write_html('GRFz-PCs.html', auto_open=True)


fPCA_coefz = fPCA_analysisz.coef

# Plot of PCs against regions
fig = go.Figure(data=go.Scatter(x=fPCA_coefz[:,0], y=fPCA_coefz[:,1], mode='markers+text', text=dfz.columns))

fig.update_traces(textposition='top center')
fig.update_layout(
    title_text='<b>Functional Principal Components Analysis - GRFz</b>', title_x=0.5, xaxis_title="PC1", yaxis_title = "PC2"
)
fig.write_html('GRFz-Points.html', auto_open=True)







'''
import plotly.express as px
fig = px.scatter(x = timex, y=fPCA_analysisx.f_pca[:,0,0])
fig = px.scatter(x = timey, y=fPCA_analysisy.f_pca[:,0,0])
fig.write_html('first_figure.html', auto_open=True)
'''



