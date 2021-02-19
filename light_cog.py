import os

from assistant_utils import speak, sanitize


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
