# VoiceAssistant
A trash voice assistant that can be extended fairly easily

## Setup
* `git clone https://github.com/SomethingGeneric/VoiceAssistant`
* `pip3 install -r requirements.txt`
* If you're not on Arch Linux, edit `assist.py` and remove the `check` and `apply` cogs on line 7
* Install tuxi: https://github.com/Bugswriter/tuxi
    * On arch: `<AUR HELPER> -S tuxi-git`
* Folow instructions [here](https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst#recognizer_instancerecognize_google_cloudaudio_data-audiodata-credentials_json-unionstr-none--none-language-str--en-us-preferred_phrases-unioniterablestr-none--none-show_all-bool--false---unionstr-dictstr-any) to get a credentials json file for the google cloud speech to text api.
* You should be done. Try `python3 assist.py`