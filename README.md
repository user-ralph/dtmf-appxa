# DTMF Signal Processing App

This is a web application that generates, analyzes, and visualizes Dual-Tone Multi-Frequency (DTMF) signals. 

![ezgif-4-651dc86fe6](https://github.com/user-attachments/assets/81abbf57-23ab-45b9-bb83-b9db595fcd59)


## Features
- **Audio Playback**: Play the generated DTMF tone.
- **DTMF Tone Generation**: Generate DTMF tones for any key on a standard phone keypad.
- **Time-Domain Analysis**: Display the time-domain signal of the DTMF tone.
- **Frequency-Domain Analysis**: Display the frequency spectrum of the DTMF tone using FFT.
- **DTMF Key Detection**: Automatically detect and display the key based on frequency.


## Dependencies Used

- **Flask**: Web framework for Python
- **NumPy**: For signal processing and generating tones
- **SciPy**: For performing Fast Fourier Transform (FFT) on the signal
- **Matplotlib**: For plotting time-domain and frequency-domain graphs
- **SoundDevice**: For playing the generated DTMF tones
- **Bootstrap**: For frontend styling and layout

