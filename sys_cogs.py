from assistant_utils import speak, sanitize

import os

# These cog(s) are meant for Arch Linux
# if it fails, make sure to install pacman-contrib


class check:
    def __init__(self):
        self.triggers = ["check updates"]

    def run(self, raw):
        speak("Checking updates.")
        os.system("checkupdates | wc -l > upds")
        speak("There are " + open("upds").read() + " updates for the system.")
        os.remove("upds")


class apply:
    def __init__(self):
        self.triggers = ["host update"]

    def run(self, raw):
        speak("Applying updates")
        os.system("doas pacman -Syu --noconfirm")
        speak("All updates applied.")


class reboot:
    def __init__(self):
        self.triggers("restart computer")

    def run(self, raw):
        speak("Goodbye. System restarting.")
        os.system("reboot")
