# musical-note-recognition
A Python application to detect the musical note present in .wav samples

## Setup
- Python3.7 and pip required
- Install dependencies using
```
pip install -r requirements.txt
```

## Usage
```
python3.7 note_detection.py path_to_wav_file
```

## References
- Notes and their frequencies: https://pages.mtu.edu/~suits/notefreqs.html
- Reading and handling of wav files: https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.wavfile.read.html#scipy.io.wavfile.read
- Fast Fourier Transform built into the numpy library: https://docs.scipy.org/doc/numpy/reference/generated/numpy.fft.fft.html#numpy.fft.fft
- Matplotlib docs for the generated plots: https://matplotlib.org/
- Math.isclose function to detected notes: https://docs.python.org/3/whatsnew/3.5.html#pep-485-a-function-for-testing-approximate-equality
- Pandas library: https://pandas.pydata.org/
- Test samples: https://freesound.org/people/pinkyfinger/packs/4409/, https://freewavesamples.com/alesis-fusion-nylon-string-guitar-c4
- How to use FFT in Python: https://pythontic.com/visualization/signals/fouriertransform_fft

