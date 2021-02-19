from assistant_utils import speak


class sample:
    def __init__(self):
        self.triggers = ["hello"]

    def run(self, raw):
        speak("Hello world!")
