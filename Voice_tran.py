import googletrans
import speech_recognition
import gtts
import playsound

recog = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Speak...")
    voice = recog.listen(source)
    text = recog.recognize_google(voice, language="fr")
    print(text)
translator = googletrans.Translator()
translation = translator.translate(text, dest="fr")
print(translation.text)
con_audio = gtts.gTTS(translation.text, lang="fr")
con_audio.save("translate.mp4")
playsound.playsound("translate.mp4")
