from scipy.io.wavfile import read
import numpy as np
import matplotlib.pyplot as plotter
import math
import sys
import pandas
import time
data = pandas.read_csv("notes.csv", header=0)
notes_list = list(data.Note)
frequencies_list = list(data.Frequency)

def stereo_to_mono(data):
    mono_data = []
    for i in range(len(data)):
        d = data[i][0]/2 + data[i][1]/2
        mono_data.append(d)
    return np.array(mono_data, dtype='int16')

def detect_note(detected_frequency):
    # math.isclose(16.35, 16.2, rel_tol=0.01)
    for i in range(len(frequencies_list)):
        if math.isclose(frequencies_list[i], detected_frequency, rel_tol=0.01):
            return notes_list[i]
    return "None"

start_time = time.time()

try:
    filename = sys.argv[1]
except:
    print("Usage: python3.7 note_detection.py path_to_wav_file")
    sys.exit(1)
try:
    rate, data = read(filename)
except:
    print("Could not read file, is the path and format correct?")
    sys.exit(1)

timePeriod  = len(data)/rate
figure, axis = plotter.subplots(2, 1)

try:
    if len(data[0]) > 1:
        # wav is stereo
        mono_data = stereo_to_mono(data)
    else:
        mono_data = data
except:
    mono_data = data

fft_time = time.time()
fourierTransform = np.fft.fft(mono_data)/len(mono_data)           # Normalize amplitude

fourierTransform = fourierTransform[range(int(len(mono_data)/2))] # Exclude sampling frequency

index_max = (np.argmax(abs(fourierTransform), axis = 0))
print("time taken")
print(time.time() - start_time)
print("fft time")
print(time.time() - fft_time)

plotter.subplots_adjust(hspace=1)

axis[0].set_title('Input wave')

samplingInterval = 1/(len(mono_data)/timePeriod)

time = np.arange(0, timePeriod, samplingInterval);

axis[0].plot(time, mono_data)

axis[0].set_xlabel('Time')

axis[0].set_ylabel('Amplitude')



tpCount     = len(mono_data)

values      = np.arange(int(tpCount/2))

frequencies = values/timePeriod

frequency_with_maximum_amplitude = frequencies[index_max]
detected_note = detect_note(frequency_with_maximum_amplitude)

axis[1].set_title('Fourier transform depicting the frequency components \n Note Detected: %s' % detected_note)

axis[1].plot(frequencies, abs(fourierTransform))

axis[1].set_xlabel('Frequency')

axis[1].set_ylabel('Amplitude')

print(frequencies[index_max])
plotter.show()