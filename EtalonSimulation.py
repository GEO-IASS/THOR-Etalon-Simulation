from math import *
# numpy/scipy
import numpy as np
import scipy as sp

#  plotting assets
import matplotlib
import matplotlib.pyplot as plt

print "Hello, Don"
import THOR2lib as THOR2lib

# etalon equation for transmission:
# T^2/(1 +R^2-2Rcos(delta)).  where delta =2klcos(theta),
# where k = 2n/Lambda (or k = 2nf/c) and l is the thickness of the etalon and c 
# is the speed of light

# we will also want to use Fresnel equations to calculate T and R as we beef up 
# the simululation

# enter constants

n = 3.4
thickness = 0.0001
T = 0.55
R = 0.45
c = 2.998e8
thetaDeg = 90
fmin = 100e9
fmax = 1000e9
fstep = 0.1e9
theta = THOR2lib.DegToRad(thetaDeg)
alpha = 1e-11

# set frequency plotting range
k = np.arange(fmin,fmax,fstep)

# calculate etalon spectrum
etalonSpectrtum = THOR2lib.calEtalonSpectrum1(fmin,fmax,fstep,n,T,R,theta,c,thickness)

# simulate estimated THz spectrum (exponential decay)
SimpleTHzSpectrum = THOR2lib.getSimpleExpDecaySpectrum(alpha,fmin,fmax,fstep)

# super impose THz spectrum and etalon spectrum
simulatedSpectrum = THOR2lib.superImposeSpectra(etalonSpectrtum,SimpleTHzSpectrum)

# make plots of Data ----------------------------------------------------------

figureCount = 0

plt.figure(figureCount)
figureCount = figureCount + 1

plt.plot(etalonSpectrtum[:,0],etalonSpectrtum[:,1],'k')

#plt.axis([Min , Max , -2 , 2])
plt.title("Etalon Spectrum")
plt.ylabel("Transmittance")
plt.xlabel("Frequency (GHz)")
#plt.legend(["Reference Data", "Silicon Wafer Data","Ref Extrema", "Sample Extrema"])

# ------------------------------------------------------------------------------

plt.figure(figureCount)
figureCount = figureCount + 1

plt.plot(SimpleTHzSpectrum[:,0],SimpleTHzSpectrum[:,1],'k')

#plt.axis([Min , Max , -2 , 2])
plt.title("Simple THz Spectrum")
plt.ylabel("Transmittance")
plt.xlabel("Frequency (GHz)")
#plt.legend(["Reference Data", "Silicon Wafer Data","Ref Extrema", "Sample Extrema"])

plt.figure(figureCount)
figureCount = figureCount + 1

plt.plot(simulatedSpectrum[:,0],simulatedSpectrum[:,1],'k')

#plt.axis([Min , Max , -2 , 2])
plt.title("SimulatedSpectrum")
plt.ylabel("Transmittance")
plt.xlabel("Frequency (GHz)")
#plt.legend(["Reference Data", "Silicon Wafer Data","Ref Extrema", "Sample Extrema"])

plt.show()




