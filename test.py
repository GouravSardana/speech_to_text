import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print('say something..............')
    r.adjust_for_ambient_noise(source, duration=1)
    r.dynamic_energy_threshold = True
    audio = r.listen(source)
    print('time up')

try:
    print('text: ' + r.recognize_google(audio))
    value = r.recognize_google(audio)

    if str is bytes:
        result = u"{}".format(value).encode("utf-8")

    else:
        result = "{}".format(value)

    with open("outputs.txt", "a") as f:
        f.write(result)
except:
    print('not recognise')