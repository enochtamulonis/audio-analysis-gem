import librosa
import numpy as np
import sys

if len(sys.argv) != 2:
    print("You have to pass in a file path `python3 analysis.py path_to_file.mp3`")
    sys.exit(1)

audio_file = sys.argv[1]

y, sr = librosa.load(audio_file)

# Compute the Chroma Short-Time Fourier Transform (chroma_stft)
chromagram = librosa.feature.chroma_stft(y=y, sr=sr)

# Calculate the mean chroma feature across time
mean_chroma = np.mean(chromagram, axis=1)

# Define the mapping of chroma features to keys
chroma_to_key = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# Find the key by selecting the maximum chroma feature
estimated_key_index = np.argmax(mean_chroma)
estimated_key = chroma_to_key[estimated_key_index]

# Print the detected key
print(estimated_key, end='')