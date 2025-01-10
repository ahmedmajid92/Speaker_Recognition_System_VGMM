from __future__ import division
import numpy as np
import scipy as sp
from scipy.io.wavfile import read
from scipy.io.wavfile import write     # Imported libaries such as numpy, scipy(read, write), matplotlib.pyplot
from scipy import signal

# Replace this with the location of your downloaded file.
(Frequency, array) = read('development_set\\EAf\\wav\\EAf1.wav') # Reading the sound file. 

len(array) # length of our array

FourierTransformation = sp.fft(array) # Calculating the fourier transformation of the signal

scale = sp.linspace(0, Frequency, len(array))

GuassianNoise = np.random.randn(len(FourierTransformation)) # Adding guassian Noise to the signal.

NewSound = GuassianNoise + array

write("New1.wav", Frequency, NewSound) # Saving it to the file.

b,a = signal.butter(5, 1000/(Frequency/2), btype='highpass') # ButterWorth filter 4350

filteredSignal = signal.lfilter(b,a,NewSound)

c,d = signal.butter(5, 380/(Frequency/2), btype='lowpass') # ButterWorth low-filter
newFilteredSignal = signal.lfilter(c,d,filteredSignal) # Applying the filter to the signal

write("New.wav", Frequency, newFilteredSignal) # Saving it to the file.
