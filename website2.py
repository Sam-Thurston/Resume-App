# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 12:47:25 2025

@author: sthursto



https://publish.illinois.edu/liangf/files/2016/10/Appendix_D_Dist.pdf
https://docs.scipy.org/doc/scipy/reference/stats.html
"""

#Packages
import streamlit as st
import scipy.stats as sci
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

if st.button("Rerun"):
    st.rerun()
    
#Variables
manualFit = False
imped = False
autFit = False
manualFit = False
rndIns = []
fitIns = []
manIns = []
rndMean = 0.0
rndScl = 0.0
rndSize = 0
maxSlide = 0
smoothness = 100
distObj = sci.norm;
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
           'q','r','s','t','u','v','w','x','y','z']
keys = ['alpha', 'anglit', 'arcsine', 'arcsin', 'argus', 'beta', 'betaprime', 'bradford', 'burr', 'burrtypeiii', 'burriii', 'burr3', 'burr12', 'burrtypexii', 'burrxii', 'cauchy', 'chi', 'chi2', 'chisquared', 'cosine', 'cos', 'crystalball', 'dgamma', 'doublegamma', 'gamma2', 'dpareto_lognorm', 'dparetolognorm', 'dparetolognormal', 'dpareto', 'doubleparetolognorm', 'doublepareto', 'doubleparetolognormal', 'paretolognormal2', 'paretolognorm2', 'pareto2', 'dweibull', 'doubleweibull', 'weibull2', 'erlang', 'expon', 'exponential', 'exponnorm', 'exponentialnorm', 'exponnormal', 'exponentialnormal', 'exponweib', 'exponentialweib', 'exponweibul', 'exponentialweibul', 'exponpow', 'exponentialpower', 'exponentialpow', 'exponpower', 'f', 'fatiguelife', 'birnbaumsaunders', 'fisk', 'foldcauchy', 'foldedcauchy', 'foldnorm', 'foldednorm', 'foldnormal', 'foldednormal', 'genlogistic', 'generalizedlogistic', 'genlog', 'generalizedlog', 'gennorm', 'generalizednorm', 'gennormal', 'generalizednormal', 'genpareto', 'generalizedpareto', 'genexpon', 'generalizedexpon', 'genexponential', 'generalizedexponential', 'genextreme', 'generalizedextreme', 'gausshyper', 'gausshypergeom', 'gausshypergeometric', 'gaussianhyper', 'gaussianhypergeom', 'gaussianhypergeometric', 'gamma', 'gengamma', 'generalizedgamma', 'genhalflogistic', 'genhalflog', 'generalizedhalflogistic', 'generalizedhalflog', 'genhyperbolic', 'generalizedhyperbolic', 'geninvgauss', 'generalizedinvgauss', 'geninversegauss', 'generalizedinversegauss', 'geninvgaussian', 'generalizedinvgaussian', 'geninversegaussian', 'generalizedinversegaussian', 'gibrat', 'gompertz', 'truncatedgumbel', 'gumbel_r', 'gumbelr', 'gumbelright', 'rightskewedgumbel', 'gumbell', 'gumbeleft', 'leftskewedgumbel', 'halfcauchy', 'halflogistic', 'halflog', 'halfnorm', 'halfnormal', 'halfgennorm', 'halfgeneralizednorm', 'halfgennormal', 'halfgenerealizednormal', 'hypsecant', 'hyperbolicsecant', 'hypsec', 'hyperbolicsec', 'sech', 'invgamma', 'invertedgamma', 'invgauss', 'inversegauss', 'invgaussian', 'inversegaussian', 'invweibull', 'inverseweibull', 'irwinhall', 'uniformsum', 'jf_skew_t', 'jfskewt', 'jonesfaddyskewt', 'jonesandfaddyskewt', 'johnsonsb', 'johnsonsu', 'kappa4', 'kappa4parameter', 'kappa3', 'kappa3parameter', 'ksone', 'kolmogorovsmirnovone', 'ks1', 'kolmogorovsmirnov1', 'kstwo', 'kolmogorovsmirnovtwo', 'ks2', 'kolmogorovsmirnov2', 'ks2bign', 'kstwobign', 'kolmogorovsmirnov2bign', 'kolmogorovsmirnovtwobign', 'landau', 'laplace', 'laplace_asymmetric', 'laplaceasymmetric', 'asymmetriclaplace', 'levy', 'levy_l', 'levyl', 'levyleft', 'levy_stable', 'levystable', 'logistic', 'log', 'logisticgamma', 'loggamma', 'loglaplace', 'logisticlaplace', 'lognorm', 'logisticnorm', 'logisticnormal', 'lognormal', 'loguniform', 'reciprocal', 'logisticuniform', 'lomax', 'secondpareto', 'maxwell', 'mielke', 'mielkebetakappa', 'dagum', 'moyal', 'nakagami', 'ncx2', 'noncentralx2', 'ncchi2', 'noncentralchi2', 'ncchisquared', 'noncentralchisquared', 'ncf', 'noncentralf', 'nct', 'noncentralt', "ncstudent'st", "noncentralstudent'st", 'norm', 'normal', 'norminvgauss', 'normalinvgauss', 'norminversegauss', 'normalinversegauss', 'norminvgaussian', 'normalinvgaussian', 'norminversegaussian', 'normalinversegaussian', 'pareto', 'pearson3', 'pearsontype3', 'pearsontypeiii', 'powerlaw', 'power', 'powerlognorm', 'powerlogisticnorm', 'powerlognormal', 'powerlogisticnormal', 'powernorm', 'powernormal', 'rdist', 'rdistributed', 'symmetricbeta', 'rayleigh', 'rel_breitwigner', 'relbreitwigner', 'relativisticbreitwigner', 'rice', 'recipinvgauss', 'recipinvgaussian', 'reciprocalinvgauss', 'reciprocalinvgaussian', 'recipinversegauss', 'recipinversegaussian', 'reciprocalinversegauss', 'reciprocalinversegaussian', 'semicircular', 'skewcauchy', 'skewedcauchy', 'skewnorm', 'skewnormal', 'studentized_range', 'studentizedrange', 't', "student'st", 'trapezoid', 'trapezoidal', 'triang', 'triangular', 'truncexpon', 'truncatedexpon', 'truncexponential', 'truncatedexponential', 'truncnorm', 'truncatednorm', 'truncnormal', 'truncatednormal', 'truncpareto', 'truncatedpareto', 'truncweibull_min', 'truncweibullmin', 'truncatedweibullmin', 'truncweibullminimum', 'truncatedweibullminimum', 'tukeylambda', 'uniform', 'vonmises', 'vonmises_line', 'vonmisesline', 'wald', 'weibull_min', 'weibullmin', 'weibullminimum', 'weibull_max', 'weibullmax', 'weibullmaximum', 'wrapcauchy', 'wrappedcauchy']
mask = [False, False, False, True, False, False, False, False, False, True, True, True, False, True, True, False, False, False, True, False, True, False, False, True, True, False, True, True, True, True, True, True, True, True, True, False, True, True, False, False, True, False, True, True, True, False, True, True, True, False, True, True, True, False, False, True, False, False, True, False, True, True, True, False, True, True, True, False, True, True, True, False, True, False, True, True, True, False, True, False, True, True, True, True, True, False, False, True, False, True, True, True, False, True, False, True, True, True, True, True, True, True, False, False, True, False, True, True, True, True, True, True, False, False, True, False, True, False, True, True, True, False, True, True, True, True, False, True, False, True, True, True, False, True, False, True, False, True, True, True, False, False, False, True, False, True, False, True, True, True, False, True, True, True, True, False, True, True, False, False, False, True, True, False, False, True, True, False, True, False, True, True, False, False, True, False, True, True, True, False, False, True, False, True, False, False, True, True, False, False, False, True, True, True, True, True, False, True, False, True, True, True, False, True, False, True, True, True, True, True, True, True, False, False, True, True, False, True, False, True, True, True, False, True, False, True, True, False, False, True, True, False, False, True, True, True, True, True, True, True, False, False, True, False, True, False, True, False, True, False, True, False, True, False, True, True, True, False, True, True, True, False, True, False, True, True, True, True, False, False, False, False, True, False, False, True, True, False, True, True, False, True]
acceptableDist = {}


#Older version catcher
def getUsableDists(keys, altMask):
    usableDists = {}
    counter = 0
    lastObj = sci.norm
    exists = True
    
    for name in keys:
        obj = getattr(sci, name, None)
        
        if(obj == None):
            if(altMask[counter] and exists):
                usableDists[name] = lastObj
            else:
                exists = False
                
        else:
            usableDists[name] = obj
            exists = True
            lastObj = obj
            
        counter+=1
        
        
    return usableDists
  
acceptableDist = getUsableDists(keys, mask)


#Intro stuff
st.title("Welcome to the continuous distribution grapher.")

st.header("This website allows you to graph any continuous distribution in SciPy version 1.16.2 or earlier.")

inputs, graph = st.columns(2)
#Making sure the distribution exists in this program
distObj = sci.norm
distType = inputs.text_input ("What type of distribution?",
                          value = "Normal")
distType = distType.lower().replace(" ","").replace("-","").replace("_","")

try:
    if(acceptableDist[distType]): pass
except:
    inputs.write("Please enter a valid distribution. Valid distributions are:")
    inputs.write(np.array(list(acceptableDist.keys())))
    inputs.write("Note: Distribution input may include capitals, dashes, and underscores.")
else:
    distObj = acceptableDist[distType]


#User input
impIn, manIn, rndIn = inputs.tabs(["Import CSV","Manual Input","Random Generation"])

#randomly generated graph
with rndIn:
    counter = 0
    while (True and counter < 27):
        try:
            distObj.mean(*rndIns)
        except:
            rndIns.append(1.0)
            rndIns[counter] = st.number_input(f"What is the \'{letters[counter]}\' value? ", 
                                value = 1.0)
        else:
            break
        counter += 1
    
    rndMean = st.number_input("What is the location of the graph? ", 
                                  value = 0.0)
    rndScl = st.number_input("What is the scale of the graph? ",
                                 min_value = 0.0,
                                 value = 1.0)
    rndSize = st.number_input("Generate how many points? ",
                                  min_value = 1, step = 1,
                                  value = 1000)
    
    if st.button("Generate and re-fit"):
        rng = np.random.default_rng()
        st.session_state.data = distObj.rvs(*rndIns, loc=rndMean, scale=rndScl, size=rndSize, random_state=rng)
    try:
        data = st.session_state.data
    except:
        rng = np.random.default_rng()
        st.session_state.data = distObj.rvs(*rndIns, loc=rndMean, scale=rndScl, size=rndSize, random_state=rng)
        data = st.session_state.data
    

#importing a csv file with data
with impIn:
    impFile = st.file_uploader("Upload your data: ", type=["csv"])
    if impFile is not None:
        impRead = pd.read_csv(impFile)
        data = np.ravel(impRead.to_numpy())
        
#manually inputted data
#Be able to copy and paste?
with manIn:
    st.write("Add datapoints to a pre-existing graph")
    st.write("Note: There is a bug in newer versions")
    
    if "manCounter" not in st.session_state:
        st.session_state.manLen = 0
        
    manIn = pd.DataFrame(
            {"Value:":None},
            index = range(st.session_state.manLen)
        )
      
    manEdit = st.data_editor(manIn, num_rows="dynamic", hide_index=True)
    manEdit = np.ravel(manEdit.to_numpy())
    st.session_state.manLen = len(manEdit)
    
    data = np.concatenate((data, manEdit))

#Formatting data based on user input
#NOTE: Fit method returns size (if applicable), then location, then scale
try:
    data = np.array(data[data != None], dtype = float)
    fitting = distObj.fit(data)
    
    #Data formatting
    fig, ax = plt.subplots(2, figsize=[5, 10])
    
    
    #Manual fit sliders
    st.header("Fitting Information:")
    miniColumns = inputs.columns(2)
    autFit = st.button("Automatic Fit")
    counter = 0
    
    if (len(fitting)>2):
        maxSlide = np.max(fitting[:-2])
    
    maxLocSlide = np.max(np.abs(data))
    
    for item in fitting:
        fitIns.append(0.0)
        
        if (counter < len(fitting)-2):
            fitIns[counter] = st.slider(f"Change the \'{letters[counter]}\' value by:",
                                        min_value = -item+0.01,
                                        max_value = 2*maxSlide - item,
                                        value = 0.0)
        elif (counter == len(fitting)-1):
            fitIns[counter] = st.slider("Change the fit scale by:",
                                        min_value = -item+0.01,
                                        max_value = 2*item,
                                        value = 0.0)
        else:
            fitIns[counter] = st.slider("Change the fit location by:",
                                        min_value = -maxLocSlide,
                                        max_value = maxLocSlide,
                                        value = 0.0)
        counter+=1
        
        
        
    smoothness = st.slider("Change the fit smoothness by:",
                                min_value = 2,
                                max_value = 200,
                                value = 100)
 
    
    #Reset when auto-fit button pressed
    if (autFit):
        for i in range(len(fitIns)):
            fitIns[i] = 0.0
    
    #Add manual alterations to original fit
    array = np.array(fitIns)
    fitting+=array
    
    #Graph formatting
    ax[0].plot(data,".k")
    ax[0].set_ylabel('Value')
    ax[0].set_xlabel('Instance')
    
    dist = distObj(*fitting)
    x = np.linspace(*ax[0].get_ylim(), smoothness) #Last number represents smoothness of density curve
    fit = dist.pdf(x)
    
    ax[1].plot(x, fit)
    ax[1].hist(data, bins="auto", density=True);  #Bins is number of histogram plots
    ax[1].set_ylabel('Density')
    ax[1].set_xlabel('Value')
    
    #Actually plot the graphs
    graph.pyplot(fig)
    
    #Determines error of fit
    ks_stat, p_value = sci.kstest(data, distObj.name, args=fitting)
        
    graph.write(f"Parameters: {fitting}")
    graph.write(f"KS statistic: {ks_stat:.4f}")
    graph.write(f"P-value: {p_value:.4f}")
    
except:
    graph.write("Please enter valid parameters")    


