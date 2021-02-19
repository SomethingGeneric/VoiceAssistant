# VoiceAssistant
A trash voice assistant that can be extended fairly easily

## Setup
* `git clone https://github.com/SomethingGeneric/VoiceAssistant`
* `pip3 install -r requirements.txt`
* Install tuxi: https://github.com/Bugswriter/tuxi
* Folow instructions [here](https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst#recognizer_instancerecognize_google_cloudaudio_data-audiodata-credentials_json-unionstr-none--none-language-str--en-us-preferred_phrases-unioniterablestr-none--none-show_all-bool--false---unionstr-dictstr-any) to get a credentials json file for the google cloud speech to text api.
* You should be done. Try `python3 assist.py`