from hello_cog import hello
from light_cog import light
from sys_cogs import check, apply, reboot

# Cogs (extensions) to add. We try to match against them first.
cogs = [hello(), light(), check(), apply(), reboot()]
# in theory cogs could have other init args, but why bother?
# ()'s just because Python syntax

credentials_file = "google_creds.json"

# Don't process recognized words unless it starts with:
wake_word = "system"

# End stuff to change (should change, rather)

import os, sys, datetime, subprocess, sys
import speech_recognition as sr
from assistant_utils import speak, log, info, err

cont = ""
r = None

r = sr.Recognizer()

speak("We're starting up")

while True:

    done = False

    with sr.Microphone() as source:
        try:
            audio_text = r.listen(source)
            cont = r.recognize_google_cloud(
                audio_data=audio_text, credentials_json=open(credentials_file).read()
            )
        except Exception as e:
            speak("Google cloud error: " + str(e))

    try:

        # Google apparently tries to capitalize sometimes??
        cont = cont.lower()

        info("Got: " + cont)

        if "system" in cont:
            cont = cont.replace("system ", "")

            # wake word is removed before calling cogs
            for cog in cogs:
                for term in cog.triggers:
                    if term in cont:
                        cog.run(cont)
                        done = True
                        break

            # no matching cog:
            if not done:
                # are we done here?
                if "exit" in cont:
                    speak("Goodbye.")
                    sys.exit(0)
                # use tuxi to see if google can help
                else:
                    os.system('tuxi -r "' + cont + '" > temp')
                    speak(open("temp").read())
                    os.remove("temp")

    except Exception as e:
        err(str(e))
