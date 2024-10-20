# DTMF Signal Processing Web App

This is a web application that generates, analyzes, and visualizes Dual-Tone Multi-Frequency (DTMF) signals. It uses Flask for the backend, and provides time-domain and frequency-domain visualizations for the generated DTMF tones. The app also identifies the corresponding key based on the frequency spectrum.

## Features

- **DTMF Tone Generation**: Generate DTMF tones for any key on a standard phone keypad.
- **Time-Domain Visualization**: Display the time-domain signal of the DTMF tone.
- **Frequency-Domain Visualization**: Display the frequency spectrum of the DTMF tone using FFT.
- **DTMF Key Detection**: Automatically detect and display the key based on the signal’s frequency.
- **Audio Playback**: Play the generated DTMF tone.

## Dependencies Used

- **Flask**: Web framework for Python
- **NumPy**: For signal processing and generating tones
- **SciPy**: For performing Fast Fourier Transform (FFT) on the signal
- **Matplotlib**: For plotting time-domain and frequency-domain graphs
- **SoundDevice**: For playing the generated DTMF tones
- **Bootstrap**: For frontend styling and layout

