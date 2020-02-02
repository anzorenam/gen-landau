#!/usr/bin/env python3.7
# -*- coding: utf8 -*-

import matplotlib as mat
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import ROOT
import root_numpy as rnp
import pylandau

sns.set(rc={"figure.figsize":(8,4)})
sns.set_context('paper',font_scale=1.0,rc={'lines.linewidth':1.0})
sns.set_style('whitegrid')
mat.rc('text',usetex=True)
mat.rc('font',family='serif',serif='palatino')
mat.rcParams['text.latex.preamble']=[r'\usepackage[utf8]{inputenc}',r'\usepackage[T1]{fontenc}',r'\usepackage[spanish]{babel}',r'\usepackage{amsmath,amsfonts,amssymb}',r'\usepackage{siunitx}']

time=np.arange(400,700,0.01)
dtau=ROOT.TF1('tau0','TMath::Landau(x,492.145,7.59229,1)')
tau=rnp.evaluate(dtau,time)
rnd_tau=rnp.random_sample(ROOT.TF1('tau0','TMath::Landau(x,492.145,7.59229,1)',400,700),1000000,seed=1)
c=sns.color_palette(sns.cubehelix_palette(8,start=.25,rot=-.75,reverse=True))
fig,ax=plt.subplots(nrows=1,ncols=1)
plt.plot(time,tau,color=c[0])
sns.distplot(rnd_tau,hist=True,kde=False,rug=False,ax=ax,norm_hist=True,
hist_kws={'histtype':'stepfilled','alpha':0.9},color=c[1])
plt.show()
