import os

from assistant_utils import speak, sanitize

# This cog is a special case. 
# I've set up shell scripts to contact my LIFX bulb that are run like:
# $ light off
# $ light blue
# $ light on
# and so on. I'm happy to share them if others are interested

class light:
    def __init__(self):
        self.triggers = ["light"]

    def run(self, raw):
        # raw = sanitize(self.triggers,raw)
        try:
            os.system(raw)
            speak("Ran the command: " + raw)
        except Exception as e:
            speak("We had a problem: " + str(e))
