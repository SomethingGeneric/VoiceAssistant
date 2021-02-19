# VoiceAssistant
A trash voice assistant that can be extended fairly easily

## Setup
* `git clone https://github.com/SomethingGeneric/VoiceAssistant`
* `pip3 install -r requirements.txt`
* If you're not on Arch Linux, edit `assist.py` and remove the `check` and `apply` cogs on the line with `cogs =`
    * Optionally also change the `wake_word` variable.
* Install tuxi: https://github.com/Bugswriter/tuxi
    * On arch: `<AUR HELPER> -S tuxi-git`
* Folow instructions [here](https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst#recognizer_instancerecognize_google_cloudaudio_data-audiodata-credentials_json-unionstr-none--none-language-str--en-us-preferred_phrases-unioniterablestr-none--none-show_all-bool--false---unionstr-dictstr-any) to get a credentials json file for the google cloud speech to text api. (And set `credentials_file` to the saved file path)
* You should be done. Try `python3 assist.py`