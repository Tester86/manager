import win32com.client as wc
speech = wc.Dispatch("Sapi.SpVoice")

def say(msg):
    global speech
    speech.Speak(msg)
