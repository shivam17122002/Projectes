import googletrans
import speech_recognition
import gtts
import playsound

input_lang = "hi"
output_lang = "fr"
recog = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Speak...")
    voice = recog.listen(source)
    text = recog.recognize_google(voice, language=input_lang)
    print(text)
translator = googletrans.Translator()
translation = translator.translate(text, dest=output_lang)
print(translation.text)
con_audio = gtts.gTTS(translation.text, lang=output_lang)
con_audio.save("translate.mp4")
playsound.playsound("translate.mp4")
