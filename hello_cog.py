from assistant_utils import speak


class hello:
    def __init__(self):
        self.triggers = ["hello"]

    def run(self, raw):
        speak("Hello world!")
