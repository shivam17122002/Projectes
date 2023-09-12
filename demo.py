import gtts
import playsound

text = input("Enter something here: ")

sound = gtts.gTTS(text, lang = "en")

sound.save("assi.mp3")
playsound.playsound("assi.mp3")
