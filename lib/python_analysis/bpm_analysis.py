import librosa
import sys

if len(sys.argv) != 2:
    print("You have to pass in a file path `python3 analysis.py path_to_file.mp3`")
    sys.exit(1)

audio_file = sys.argv[1]
y, sr = librosa.load(audio_file)

# Estimate tempo (BPM)
tempo, _ = librosa.beat.beat_track(y=y, sr=sr)

print(tempo, end='')