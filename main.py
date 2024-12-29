import sounddevice as sd
import numpy as np
import time
import requests
import wave

# Set the sample rate and duration for capturing audio
SAMPLE_RATE = 44100
DURATION = 10  # Duration of audio capture in seconds
CHANNELS = 2  # Stereo channels

# List all devices
print("Available Devices:")
print(sd.query_devices())

# Function to record audio using WASAPI loopback
def record_audio(device_index):
    print("Recording audio...")
    audio_data = sd.rec(int(SAMPLE_RATE * DURATION), samplerate=SAMPLE_RATE, channels=CHANNELS, dtype='float32', device=device_index)  
    sd.wait()  # Wait for the recording to finish
    print("Recording completed.")
    return audio_data

# Function to send audio data to ACRCloud for music recognition
def send_to_acrcloud(audio_data):
    # Convert audio data to a suitable format for ACRCloud (WAV format)
    wav_file = "audio_capture.wav"
    with wave.open(wav_file, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(2)  # 2 bytes per sample (16-bit)
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(audio_data.tobytes())

    # Send to ACRCloud for recognition (replace with your credentials)
    url = 'https://identify-eu-west-1.acrcloud.com/v1/identify'
    params = {
        'access_key': 'YOUR_ACRCLOUD_ACCESS_KEY',
        'access_secret': 'YOUR_ACRCLOUD_SECRET_KEY',
        'audio_file': wav_file
    }

    with open(wav_file, 'rb') as f:
        response = requests.post(url, files={'file': f}, data=params)
        print("Response from ACRCloud: ", response.json())

# Main function to capture and send data
def main():
    # Identify the correct input device index (you can replace this with the correct index from the print output)
    device_index = 1  # Change this index based on your available device
    while True:
        audio_data = record_audio(device_index)
        send_to_acrcloud(audio_data)
        time.sleep(5)  # Delay between recordings

if __name__ == "__main__":
    main()
