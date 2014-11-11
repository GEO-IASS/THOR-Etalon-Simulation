import numpy as np
import scipy as sp
import math
 
# -----------------------------------------------------
# convert degrees to radians
def DegToRad(angle):
	pi = 3.14159
	angleRad = (pi/180)*angle
	return angleRad

# ------------------------------------------------------
# create etalon spectra
# axis 0 (Frequency)
# axis 1 (transmitted intensity)
def calEtalonSpectrum1(fmin,fmax,fstep,n,T,R,theta,c,thickness):
	freqAxis = createFreqAxis(fmin,fmax,fstep)

	# get size of array
	arrayLength = freqAxis.shape[0]

	# initialize final etalon array
	etalonSpectrum = np.zeros((arrayLength,2))

	#copy frequency axis to etalonSpectrum Array
	etalonSpectrum[:,0] = freqAxis

	# calculate delta (make this into its own function later)
	delta = np.zeros((arrayLength,1))
	delta = 2*freqAxis*thickness*math.cos(theta)

	# calculate etalonSpectrum
	etalonSpectrum[:,1] = T*T/(1 + R*R - 2*R*np.cos(delta))

	print etalonSpectrum.shape

	return etalonSpectrum

# ------------------------------------------------------
def getSimpleExpDecaySpectrum(alpha,fmin,fmax,fstep):
	# this function produces an exponential decaying function 
	# versus frequency
	# I = I_0*e-(alpha*freq)
	I_0 = 1.0

	freqAxis = createFreqAxis(fmin,fmax,fstep)

	# get array length
	arrayLength = freqAxis.shape[0]

	# initilize decay spectrum
	decaySpectrum = np.zeros((arrayLength,2)) 

	# copy freq axis to decay spectrum
	decaySpectrum[:,0] = freqAxis

	# calculate decay spectrum 
	decaySpectrum[:,1] = I_0*np.exp((-1.0)*alpha*freqAxis)  #*freqAxis
	print decaySpectrum
	return decaySpectrum

# ------------------------------------------------------
def createFreqAxis(fmin,fmax,fstep):
	fAxis = np.arange(fmin,fmax,fstep)
	return fAxis

# ------------------------------------------------------
def superImposeSpectra(spectrum1,spectrum2):

	# to do &*&*&*&*&*&*&*&&&&&*&*&**&*&
	#make sure spectra have the same freq axis, if not 
	#output an error# &*&*&*&*&*&*&*&*&*&*&

	#get length of spectra
	arrayLength = spectrum1.shape[0]

	# initilize super spectra
	superSpectrum = np.zeros((arrayLength,2))

	# copy frequency spectrum to superSpectra array column 0
	superSpectrum[:,0] = spectrum1[:,0]

	# super impose the spectra
	superSpectrum[:,1] = spectrum1[:,1]*spectrum2[:,1]

	return superSpectrum

# ------------------------------------------------------









