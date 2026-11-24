# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import scipy.stats as sci
import numpy as np
from scipy.stats._distn_infrastructure import rv_continuous

def getKeyMask():
    continuous_dists = []
    keys = []
    mask = []
    
    acceptableDist = {"alpha": sci.alpha, "anglit": sci.anglit, "arcsine":sci.arcsine, 
                      "arcsin":sci.arcsine,"argus": sci.argus, "beta": sci.beta,
                      "betaprime": sci.betaprime, "bradford":sci.bradford, "burr": sci.burr,
                      "burrtypeiii": sci.burr, "burriii":sci.burr, "burr3": sci.burr,
                      "burr12": sci.burr12,"burrtypexii":sci.burr12, "burrxii": sci.burr12,
                      "cauchy":sci.cauchy, "chi": sci.chi, "chi2":sci.chi2, 
                      "chisquared":sci.chi2, "cosine":sci.cosine, "cos":sci.cosine,
                      "crystalball":sci.crystalball, "dgamma": sci.dgamma, "doublegamma":sci.dgamma,
                      "gamma2":sci.dgamma,  "dpareto_lognorm":sci.dpareto_lognorm,
                      "dparetolognorm":sci.dpareto_lognorm,
                      "dparetolognormal":sci.dpareto_lognorm,"dpareto":sci.dpareto_lognorm, 
                      "doubleparetolognorm":sci.dpareto_lognorm,"doublepareto":sci.dpareto_lognorm,
                      "doubleparetolognormal":sci.dpareto_lognorm,"paretolognormal2":sci.dpareto_lognorm,
                      "paretolognorm2":sci.dpareto_lognorm,"pareto2":sci.dpareto_lognorm, 
                      "dweibull":sci.dweibull,"doubleweibull":sci.dweibull, 
                      "weibull2":sci.dweibull,"erlang":sci.erlang, "expon": sci.expon, 
                      "exponential": sci.expon,"exponnorm": sci.exponnorm, 
                      "exponentialnorm": sci.exponnorm,"exponnormal": sci.exponnorm, 
                      "exponentialnormal": sci.exponnorm,"exponweib": sci.exponweib, 
                      "exponentialweib": sci.exponweib,"exponweibul": sci.exponweib, 
                      "exponentialweibul": sci.exponweib,"exponpow": sci.exponpow, 
                      "exponentialpower":sci.exponpow, "exponentialpow": sci.exponpow, 
                      "exponpower":sci.exponpow,"f": sci.f, "fatiguelife":sci.fatiguelife, 
                      "birnbaumsaunders":sci.fatiguelife,"fisk": sci.fisk, 
                      "foldcauchy":sci.foldcauchy, "foldedcauchy":sci.foldcauchy,
                      "foldnorm": sci.foldnorm, "foldednorm": sci.foldnorm, "foldnormal": sci.foldnorm, 
                      "foldednormal": sci.foldnorm, "genlogistic": sci.genlogistic,
                      "generalizedlogistic":sci.genlogistic, "genlog":sci.genlogistic,
                      "generalizedlog":sci.genlogistic, "gennorm":sci.gennorm, 
                      "generalizednorm":sci.gennorm, "gennormal":sci.gennorm, 
                      "generalizednormal":sci.gennorm, "genpareto": sci.genpareto,
                      "generalizedpareto": sci.genpareto, "genexpon":sci.genexpon, 
                      "generalizedexpon":sci.genexpon, "genexponential":sci.genexpon, 
                      "generalizedexponential":sci.genexpon, "genextreme": sci.genextreme,
                      "generalizedextreme": sci.genextreme, "gausshyper": sci.gausshyper,
                      "gausshypergeom": sci.gausshyper, "gausshypergeometric": sci.gausshyper,
                      "gaussianhyper": sci.gausshyper,"gaussianhypergeom": sci.gausshyper, 
                      "gaussianhypergeometric": sci.gausshyper,"gamma":sci.gamma, 
                      "gengamma":sci.gengamma, "generalizedgamma":sci.gengamma, 
                      "genhalflogistic":sci.genhalflogistic, "genhalflog":sci.genhalflogistic,
                      "generalizedhalflogistic":sci.genhalflogistic, "generalizedhalflog":sci.genhalflogistic, 
                      "genhyperbolic":sci.genhyperbolic, "generalizedhyperbolic":sci.genhyperbolic,
                      "geninvgauss":sci.geninvgauss, "generalizedinvgauss":sci.geninvgauss, 
                      "geninversegauss":sci.geninvgauss, "generalizedinversegauss":sci.geninvgauss, 
                      "geninvgaussian":sci.geninvgauss, "generalizedinvgaussian":sci.geninvgauss, 
                      "geninversegaussian":sci.geninvgauss, "generalizedinversegaussian":sci.geninvgauss,
                      "gibrat":sci.gibrat, "gompertz":sci.gompertz, "truncatedgumbel":sci.gompertz,
                      "gumbel_r":sci.gumbel_r,
                      "gumbelr":sci.gumbel_r, "gumbelright":sci.gumbel_r, "rightskewedgumbel":sci.gumbel_r,
                      "gumbell":sci.gumbel_r, "gumbeleft":sci.gumbel_r, "leftskewedgumbel":sci.gumbel_r,
                      "halfcauchy":sci.halfcauchy, "halflogistic":sci.halflogistic, 
                      "halflog":sci.halflogistic, "halfnorm":sci.halfnorm, 
                      "halfnormal":sci.halfnorm, "halfgennorm":sci.halfgennorm, 
                      "halfgeneralizednorm":sci.halfgennorm, "halfgennormal":sci.halfgennorm,
                      "halfgenerealizednormal":sci.halfgennorm, "hypsecant":sci.hypsecant,
                      "hyperbolicsecant":sci.hypsecant, "hypsec":sci.hypsecant, 
                      "hyperbolicsec":sci.hypsecant, "sech":sci.hypsecant, "invgamma":sci.invgamma, 
                      "invertedgamma":sci.invgamma, "invgauss": sci.invgauss, "inversegauss": sci.invgauss, 
                      "invgaussian": sci.invgauss, "inversegaussian": sci.invgauss, 
                      "invweibull": sci.invweibull, "inverseweibull": sci.invweibull, 
                      "irwinhall": sci.irwinhall, "uniformsum": sci.irwinhall, 
                      "jf_skew_t": sci.jf_skew_t, 
                      "jfskewt": sci.jf_skew_t, "jonesfaddyskewt": sci.jf_skew_t, 
                      "jonesandfaddyskewt": sci.jf_skew_t, "johnsonsb": sci.johnsonsb, 
                      "johnsonsu": sci.johnsonsu, "kappa4": sci.kappa4, "kappa4parameter": sci.kappa4,
                      "kappa3": sci.kappa3, "kappa3parameter": sci.kappa3, "ksone": sci.ksone, 
                      "kolmogorovsmirnovone": sci.ksone, "ks1": sci.ksone, "kolmogorovsmirnov1": sci.ksone,
                      "kstwo": sci.kstwo,"kolmogorovsmirnovtwo": sci.kstwo, "ks2": sci.kstwo,
                      "kolmogorovsmirnov2": sci.kstwo, "ks2bign": sci.kstwo, "kstwobign": sci.kstwo,
                      "kolmogorovsmirnov2bign": sci.kstwo, "kolmogorovsmirnovtwobign": sci.kstwo,
                      "landau": sci.landau, "laplace":sci.laplace, 
                      "laplace_asymmetric": sci.laplace_asymmetric, "laplaceasymmetric": sci.laplace_asymmetric,
                      "asymmetriclaplace": sci.laplace_asymmetric, "levy":sci.levy, "levy_l":sci.levy_l,  
                      "levyl":sci.levy_l, "levyleft":sci.levy_l, "levy_stable":sci.levy_stable,
                      "levystable":sci.levy_stable, "logistic":sci.logistic, 
                      "log":sci.logistic, "logisticgamma":sci.loggamma, "loggamma":sci.loggamma, 
                      "loglaplace":sci.loglaplace, "logisticlaplace":sci.loglaplace, 
                      "lognorm":sci.lognorm, "logisticnorm":sci.lognorm, 
                      "logisticnormal":sci.lognorm, "lognormal":sci.lognorm, "loguniform":sci.loguniform, 
                      "reciprocal":sci.loguniform, "logisticuniform":sci.loguniform, 
                      "lomax":sci.lomax, "secondpareto":sci.lomax, "maxwell":sci.maxwell, 
                      "mielke":sci.mielke, "mielkebetakappa":sci.mielke, "dagum":sci.mielke,  
                      "moyal":sci.moyal, "nakagami":sci.nakagami, "ncx2":sci.ncx2, 
                      "noncentralx2":sci.ncx2, "ncchi2":sci.ncx2, "noncentralchi2":sci.ncx2, 
                      "ncchisquared":sci.ncx2, "noncentralchisquared":sci.ncx2, "ncf":sci.ncf,
                      "noncentralf":sci.ncf, "nct":sci.nct, "noncentralt":sci.nct,
                      "ncstudent\'st":sci.nct, "noncentralstudent\'st":sci.nct, "norm":sci.norm, 
                      "normal":sci.norm, "norminvgauss":sci.norminvgauss, "normalinvgauss":sci.norminvgauss, 
                      "norminversegauss":sci.norminvgauss, "normalinversegauss":sci.norminvgauss, 
                      "norminvgaussian":sci.norminvgauss, "normalinvgaussian":sci.norminvgauss, 
                      "norminversegaussian":sci.norminvgauss, "normalinversegaussian":sci.norminvgauss, 
                      "pareto":sci.pareto, "pearson3":sci.pearson3, "pearsontype3":sci.pearson3,
                      "pearsontypeiii":sci.pearson3, "powerlaw":sci.powerlaw, "power":sci.powerlaw,
                      "powerlognorm":sci.powerlognorm, "powerlogisticnorm":sci.powerlognorm, 
                      "powerlognormal":sci.powerlognorm, "powerlogisticnormal":sci.powerlognorm,
                      "powernorm":sci.powernorm, "powernormal":sci.powernorm, "rdist":sci.rdist, 
                      "rdistributed":sci.rdist, "symmetricbeta":sci.rdist, "rayleigh":sci.rayleigh,
                      "rel_breitwigner":sci.rel_breitwigner, 
                      "relbreitwigner":sci.rel_breitwigner, "relativisticbreitwigner":sci.rel_breitwigner, 
                      "rice":sci.rice, "recipinvgauss":sci.recipinvgauss, "recipinvgaussian":sci.recipinvgauss, 
                      "reciprocalinvgauss":sci.recipinvgauss, "reciprocalinvgaussian":sci.recipinvgauss, 
                      "recipinversegauss":sci.recipinvgauss, "recipinversegaussian":sci.recipinvgauss, 
                      "reciprocalinversegauss":sci.recipinvgauss, "reciprocalinversegaussian":sci.recipinvgauss, 
                      "semicircular":sci.semicircular, "skewcauchy":sci.skewcauchy, 
                      "skewedcauchy":sci.skewcauchy, "skewnorm":sci.skewnorm, "skewnormal":sci.skewnorm,
                      "studentized_range":sci.studentized_range, 
                      "studentizedrange":sci.studentized_range, "t":sci.t, "student\'st":sci.t,
                      "trapezoid":sci.trapezoid, "trapezoidal":sci.trapezoid, "triang":sci.triang,
                      "triangular":sci.triang, "truncexpon":sci.truncexpon, "truncatedexpon":sci.truncexpon, 
                      "truncexponential":sci.truncexpon, "truncatedexponential":sci.truncexpon, 
                      "truncnorm":sci.truncnorm, "truncatednorm":sci.truncnorm, 
                      "truncnormal":sci.truncnorm, "truncatednormal":sci.truncnorm,
                      "truncpareto":sci.truncpareto, "truncatedpareto":sci.truncpareto, 
                      "truncweibull_min":sci.truncweibull_min, 
                      "truncweibullmin":sci.truncweibull_min, "truncatedweibullmin":sci.truncweibull_min, 
                      "truncweibullminimum":sci.truncweibull_min, "truncatedweibullminimum":sci.truncweibull_min, 
                      "tukeylambda":sci.tukeylambda, "uniform":sci.uniform, "vonmises":sci.vonmises,
                      "vonmises_line":sci.vonmises_line, "vonmisesline":sci.vonmises_line, "wald":sci.wald, 
                      "weibull_min":sci.weibull_min, "weibullmin":sci.weibull_min,
                      "weibullminimum":sci.weibull_min, 
                      "weibull_max":sci.weibull_max, "weibullmax":sci.weibull_max, 
                      "weibullmaximum":sci.weibull_max, "wrapcauchy":sci.wrapcauchy,
                      "wrappedcauchy":sci.wrapcauchy
                      }
    keys = acceptableDist.keys()
    
    for name in dir(sci):
        obj = getattr(sci, name)
        if isinstance(obj, rv_continuous):
            continuous_dists.append(name)
            
    for name in keys:
        mask.append(continuous_dists.count(name)==0)    
    
    return keys, mask
    
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
        
keys = ['alpha', 'anglit', 'arcsine', 'arcsin', 'argus', 'beta', 'betaprime', 'bradford', 'burr', 'burrtypeiii', 'burriii', 'burr3', 'burr12', 'burrtypexii', 'burrxii', 'cauchy', 'chi', 'chi2', 'chisquared', 'cosine', 'cos', 'crystalball', 'dgamma', 'doublegamma', 'gamma2', 'dpareto_lognorm', 'dparetolognorm', 'dparetolognormal', 'dpareto', 'doubleparetolognorm', 'doublepareto', 'doubleparetolognormal', 'paretolognormal2', 'paretolognorm2', 'pareto2', 'dweibull', 'doubleweibull', 'weibull2', 'erlang', 'expon', 'exponential', 'exponnorm', 'exponentialnorm', 'exponnormal', 'exponentialnormal', 'exponweib', 'exponentialweib', 'exponweibul', 'exponentialweibul', 'exponpow', 'exponentialpower', 'exponentialpow', 'exponpower', 'f', 'fatiguelife', 'birnbaumsaunders', 'fisk', 'foldcauchy', 'foldedcauchy', 'foldnorm', 'foldednorm', 'foldnormal', 'foldednormal', 'genlogistic', 'generalizedlogistic', 'genlog', 'generalizedlog', 'gennorm', 'generalizednorm', 'gennormal', 'generalizednormal', 'genpareto', 'generalizedpareto', 'genexpon', 'generalizedexpon', 'genexponential', 'generalizedexponential', 'genextreme', 'generalizedextreme', 'gausshyper', 'gausshypergeom', 'gausshypergeometric', 'gaussianhyper', 'gaussianhypergeom', 'gaussianhypergeometric', 'gamma', 'gengamma', 'generalizedgamma', 'genhalflogistic', 'genhalflog', 'generalizedhalflogistic', 'generalizedhalflog', 'genhyperbolic', 'generalizedhyperbolic', 'geninvgauss', 'generalizedinvgauss', 'geninversegauss', 'generalizedinversegauss', 'geninvgaussian', 'generalizedinvgaussian', 'geninversegaussian', 'generalizedinversegaussian', 'gibrat', 'gompertz', 'truncatedgumbel', 'gumbel_r', 'gumbelr', 'gumbelright', 'rightskewedgumbel', 'gumbell', 'gumbeleft', 'leftskewedgumbel', 'halfcauchy', 'halflogistic', 'halflog', 'halfnorm', 'halfnormal', 'halfgennorm', 'halfgeneralizednorm', 'halfgennormal', 'halfgenerealizednormal', 'hypsecant', 'hyperbolicsecant', 'hypsec', 'hyperbolicsec', 'sech', 'invgamma', 'invertedgamma', 'invgauss', 'inversegauss', 'invgaussian', 'inversegaussian', 'invweibull', 'inverseweibull', 'irwinhall', 'uniformsum', 'jf_skew_t', 'jfskewt', 'jonesfaddyskewt', 'jonesandfaddyskewt', 'johnsonsb', 'johnsonsu', 'kappa4', 'kappa4parameter', 'kappa3', 'kappa3parameter', 'ksone', 'kolmogorovsmirnovone', 'ks1', 'kolmogorovsmirnov1', 'kstwo', 'kolmogorovsmirnovtwo', 'ks2', 'kolmogorovsmirnov2', 'ks2bign', 'kstwobign', 'kolmogorovsmirnov2bign', 'kolmogorovsmirnovtwobign', 'landau', 'laplace', 'laplace_asymmetric', 'laplaceasymmetric', 'asymmetriclaplace', 'levy', 'levy_l', 'levyl', 'levyleft', 'levy_stable', 'levystable', 'logistic', 'log', 'logisticgamma', 'loggamma', 'loglaplace', 'logisticlaplace', 'lognorm', 'logisticnorm', 'logisticnormal', 'lognormal', 'loguniform', 'reciprocal', 'logisticuniform', 'lomax', 'secondpareto', 'maxwell', 'mielke', 'mielkebetakappa', 'dagum', 'moyal', 'nakagami', 'ncx2', 'noncentralx2', 'ncchi2', 'noncentralchi2', 'ncchisquared', 'noncentralchisquared', 'ncf', 'noncentralf', 'nct', 'noncentralt', "ncstudent'st", "noncentralstudent'st", 'norm', 'normal', 'norminvgauss', 'normalinvgauss', 'norminversegauss', 'normalinversegauss', 'norminvgaussian', 'normalinvgaussian', 'norminversegaussian', 'normalinversegaussian', 'pareto', 'pearson3', 'pearsontype3', 'pearsontypeiii', 'powerlaw', 'power', 'powerlognorm', 'powerlogisticnorm', 'powerlognormal', 'powerlogisticnormal', 'powernorm', 'powernormal', 'rdist', 'rdistributed', 'symmetricbeta', 'rayleigh', 'rel_breitwigner', 'relbreitwigner', 'relativisticbreitwigner', 'rice', 'recipinvgauss', 'recipinvgaussian', 'reciprocalinvgauss', 'reciprocalinvgaussian', 'recipinversegauss', 'recipinversegaussian', 'reciprocalinversegauss', 'reciprocalinversegaussian', 'semicircular', 'skewcauchy', 'skewedcauchy', 'skewnorm', 'skewnormal', 'studentized_range', 'studentizedrange', 't', "student'st", 'trapezoid', 'trapezoidal', 'triang', 'triangular', 'truncexpon', 'truncatedexpon', 'truncexponential', 'truncatedexponential', 'truncnorm', 'truncatednorm', 'truncnormal', 'truncatednormal', 'truncpareto', 'truncatedpareto', 'truncweibull_min', 'truncweibullmin', 'truncatedweibullmin', 'truncweibullminimum', 'truncatedweibullminimum', 'tukeylambda', 'uniform', 'vonmises', 'vonmises_line', 'vonmisesline', 'wald', 'weibull_min', 'weibullmin', 'weibullminimum', 'weibull_max', 'weibullmax', 'weibullmaximum', 'wrapcauchy', 'wrappedcauchy']
mask = [False, False, False, True, False, False, False, False, False, True, True, True, False, True, True, False, False, False, True, False, True, False, False, True, True, False, True, True, True, True, True, True, True, True, True, False, True, True, False, False, True, False, True, True, True, False, True, True, True, False, True, True, True, False, False, True, False, False, True, False, True, True, True, False, True, True, True, False, True, True, True, False, True, False, True, True, True, False, True, False, True, True, True, True, True, False, False, True, False, True, True, True, False, True, False, True, True, True, True, True, True, True, False, False, True, False, True, True, True, True, True, True, False, False, True, False, True, False, True, True, True, False, True, True, True, True, False, True, False, True, True, True, False, True, False, True, False, True, True, True, False, False, False, True, False, True, False, True, True, True, False, True, True, True, True, False, True, True, False, False, False, True, True, False, False, True, True, False, True, False, True, True, False, False, True, False, True, True, True, False, False, True, False, True, False, False, True, True, False, False, False, True, True, True, True, True, False, True, False, True, True, True, False, True, False, True, True, True, True, True, True, True, False, False, True, True, False, True, False, True, True, True, False, True, False, True, True, False, False, True, True, False, False, True, True, True, True, True, True, True, False, False, True, False, True, False, True, False, True, False, True, False, True, False, True, True, True, False, True, True, True, False, True, False, True, True, True, True, False, False, False, False, True, False, False, True, True, False, True, True, False, True]

print(getUsableDists(keys,mask))