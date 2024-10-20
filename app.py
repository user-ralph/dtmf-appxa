from flask import Flask, render_template, request, jsonify
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
import io
import base64
import sounddevice as sd

app = Flask(__name__)

dtmf_freqs = {
    '1': (697, 1209), '2': (697, 1336), '3': (697, 1477),
    '4': (770, 1209), '5': (770, 1336), '6': (770, 1477),
    '7': (852, 1209), '8': (852, 1336), '9': (852, 1477),
    '*': (941, 1209), '0': (941, 1336), '#': (941, 1477)
}

def generate_dtmf_tone(key, duration=0.5, fs=8000):
    if key not in dtmf_freqs:
        raise ValueError(f"Invalid key: {key}")
    
    low_freq, high_freq = dtmf_freqs[key]
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    signal = np.sin(2 * np.pi * low_freq * t) + np.sin(2 * np.pi * high_freq * t)
    return t, signal

def plot_time_domain(t, signal):
    plt.figure()
    plt.plot(t[:100], signal[:100])  # Plot the first 100 points
    plt.title("Time-Domain Signal (First 100 Samples)")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()
    plt.close()  # Close the plot
    return img

def plot_frequency_spectrum(signal, fs, detected_key=None):
    N = len(signal)
    fft_vals = fft(signal)
    freqs = np.fft.fftfreq(N, 1/fs)
    magnitude = np.abs(fft_vals)

    plt.figure()
    plt.plot(freqs[:N//2], magnitude[:N//2])  # Plot only the positive frequencies
    plt.title("Frequency Spectrum")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")

    # Annotate the detected DTMF key on the plot
    if detected_key is not None:
        plt.annotate(f'Detected DTMF Key: {detected_key}', 
                     xy=(0.5, 0.9), 
                     xycoords='axes fraction', 
                     fontsize=12, 
                     ha='center', 
                     bbox=dict(boxstyle='round,pad=0.3', edgecolor='black', facecolor='lightyellow'))

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()
    plt.close()  # Close the plot
    return img

def identify_dtmf_key(freqs, magnitude, fs=8000):
    N = len(freqs)
    positive_freqs = freqs[:N // 2]
    positive_magnitude = magnitude[:N // 2]
    
    peak_indices = np.argsort(positive_magnitude)[-2:]  
    identified_freqs = np.sort(positive_freqs[peak_indices]) 
    
    for key, (low_freq, high_freq) in dtmf_freqs.items():
        if np.isclose(identified_freqs, [low_freq, high_freq], atol=10).all():
            return key
    return None

def play_dtmf_tone(key, duration=0.5, fs=8000):
    t, signal = generate_dtmf_tone(key, duration, fs)
    sd.play(signal, samplerate=fs)
    sd.wait() 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    key = request.form['key']
    
    t, signal = generate_dtmf_tone(key)
    time_domain_img = plot_time_domain(t, signal)
    detected_key = identify_dtmf_key(np.fft.fftfreq(len(signal), 1/8000), np.abs(fft(signal)))
    frequency_domain_img = plot_frequency_spectrum(signal, fs=8000, detected_key=detected_key)
    play_dtmf_tone(key)

    return jsonify({
        'time_domain_img': time_domain_img,
        'frequency_domain_img': frequency_domain_img,
        'detected_key': detected_key
    })

if __name__ == '__main__':
    app.run()
