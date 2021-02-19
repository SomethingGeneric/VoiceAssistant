from assistant_utils import speak, sanitize

import os,sys

# These cog(s) are meant for Arch Linux
# if it fails, make sure to install pacman-contrib


class check:
    def __init__(self):
        self.triggers = ["check update", "check updates"]

    def run(self, raw):
        speak("Checking updates.")
        os.system("checkupdates | wc -l > upds")
        speak("There are " + open("upds").read() + " updates for the system.")
        os.remove("upds")


# an example of check for debian based systems
"""
class check:
    def __init__(self):
        self.triggers = ["check updates"]

    def run(self, raw):
        speak("Checking updates.")
        os.system("sudo apt update ; sudo apt list --upgradeable | wc -l > upds")
        speak("There are " + open("upds").read() + " updates for the system.")
        os.remove("upds")
"""


class apply:
    def __init__(self):
        self.triggers = ["host update"]

    def run(self, raw):
        speak("Applying updates")
        speak("You may be prompted for a password")
        os.system("doas pacman -Syu --noconfirm")
        speak("All updates applied.")


# An example of apply for debian systems
"""
class apply:
    def __init__(self):
        self.triggers = ["host update"]

    def run(self, raw):
        speak("Applying updates")
        speak("You may be prompted for a password")
        os.system("sudo apt full-upgrade -y")
        speak("All updates applied.")
"""


class reboot:
    def __init__(self):
        self.triggers = ["restart computer"]

    def run(self, raw):
        speak("Goodbye. System restarting.")
        os.system("reboot")

class update:
    def __init__(self):
        self.triggers = ["update program"]
    def run(self,raw):
        speak("Updating the source code")
        os.system("git pull")
        os.system("git --no-pager log --decorate=short --pretty=oneline -n1 > tmpf")
        msg = open("tmpf").read()
        os.remove("tmpf")
        speak("Git reports the following changes: " + msg)
        speak("Updates are complete. They will have no effect until I am restarted.")
