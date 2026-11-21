import speech_recognition as sr
import sounddevice as sd 


recog = sr.Recognizer()

sample_rate = 16000
dur = 7

audio = sd.rec(int(sample_rate*dur), samplerate=sample_rate , channels=1 , dtype="int16")

sd.wait()

audio_data = sr.AudioData(audio.tobytes(), sample_rate, 2)
try:
    text = recog.recognize_google(audio_data,language ="en-IN");
    print(text)
except sr.UnknownValueError:
    print("Unknown value")
except sr.RequestError:
    print("Request Error") 
       


