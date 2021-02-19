from assistant_utils import (
    speak,
    sanitize,
)  # check if other util functions might be helpful for you, too


class sample:
    def __init__(self):
        self.triggers = ["hello"]

    def run(self, raw):
        # remove any cog triggers from the raw recognized text
        # mostly useful for cogs split off from main
        # raw = sanitize(self.triggers,raw)
        speak("Hello world!")
