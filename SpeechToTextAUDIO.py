import speech_recognition as sr
recog = sr.Recognizer()
with sr.AudioData("order.wav",) as audio:
    audio_data = recog.record(audio)
    print('Transcribing')
try:
    text = recog.recognize_amazon(audio_data)
    print(text)
except sr.UnknownValueError:    
    print("unknown val")
except sr.RequestError:
    print("Req error")    