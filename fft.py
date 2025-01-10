from scipy.io.wavfile import read
from noisereduce.noisereduce import reduce_noise
#import noisereduce as nr
# load data
rate, data = wavfile.read("development_set\\EAf\\wav\\EAf1.wav")
# select section of data that is noise
noisy_part = data[10000:15000]
# perform noise reduction
reduced_noise = reduce_noise(audio_clip=data, noise_clip=noisy_part, verbose=True)